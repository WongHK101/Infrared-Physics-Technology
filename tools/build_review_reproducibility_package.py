"""Build an offline code/evaluation supplement, without images or model weights."""
from __future__ import annotations

import argparse
import hashlib
import io
import json
from pathlib import Path
import re
import subprocess
import zipfile


ROOT = Path(__file__).resolve().parents[1]
TEXT = {".py", ".md", ".txt", ".json", ".csv", ".yml", ".yaml", ".ps1",
        ".sh", ".toml", ".cfg", ".ini"}
FORBIDDEN = re.compile(
    r"(?:(?<![A-Za-z])[A-Za-z]:\\|/home/user[12]/|"
    r"100\.\d{1,3}\.\d{1,3}\.\d{1,3}|"
    r"172\.(?:1[6-9]|2\d|3[01])\.\d{1,3}\.\d{1,3}|"
    r"-----BEGIN (?:OPENSSH|RSA|EC) PRIVATE KEY-----)"
)


def git(repo: Path, *args: str) -> str:
    return subprocess.check_output(
        ["git", "-C", str(repo), *args], encoding="utf-8"
    ).strip()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--code-root", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    code = args.code_root.resolve()
    if args.output.exists():
        raise FileExistsError("Choose a new output filename; existing packages are not overwritten.")
    if git(code, "diff", "--name-only", "HEAD"):
        raise RuntimeError("Commit tracked code changes before packaging.")

    files: dict[str, bytes] = {}
    adapted: list[str] = []

    def add(path: Path, name: str, data: bytes | None = None) -> None:
        if data is None:
            data = path.read_bytes()
        if path.suffix.lower() in TEXT or path.name in {"LICENSE", "NOTICE", "README"}:
            text = data.decode("utf-8-sig")
            # Only documentation examples are made portable; executable code is unchanged.
            if name in {"code/README.md", "code/EXPERIMENT_PLAN.md"}:
                portable = re.sub(r"\b[A-Za-z]:\\UAV-TAlign", "<PROJECT_ROOT>", text)
                if portable != text:
                    adapted.append(name)
                    data = portable.encode("utf-8")
                    text = portable
            scan_text = text
            if name in {
                "code/scripts/server_run_prcv_main_12k_windows.ps1",
                "code/scripts/server_run_prcv_protocol_artifacts_windows.ps1",
            }:
                # Standard Windows installation fallbacks contain no user identity.
                scan_text = scan_text.replace("C:\\ProgramData\\", "<SYSTEM_PROGRAM_DATA>/")
            if name.endswith("scepter/modules/utils/file_clients/utils.py"):
                scan_text = scan_text.replace("C:\\\\Users\\\\a.txt", "<UPSTREAM_PATH_EXAMPLE>")
            if FORBIDDEN.search(scan_text):
                raise ValueError(f"Private/absolute path or credential marker in {name}")
        if "\\" in name or name.startswith("/") or ".." in Path(name).parts:
            raise ValueError(f"Nonportable archive path: {name}")
        files[name] = data

    code_archive = zipfile.ZipFile(io.BytesIO(subprocess.check_output(
        ["git", "-C", str(code), "archive", "--format=zip", "HEAD"]
    )))
    tracked = [name for name in code_archive.namelist() if not name.endswith("/")]
    for name in tracked:
        if not name:
            continue
        path = code / name
        if path.name in {"AGENTS.md", "WORKLOG.md", ".env"}:
            raise ValueError(f"Private collaboration file is tracked: {name}")
        if path.suffix.lower() in {".pth", ".pt", ".ckpt", ".onnx", ".zip", ".jsonl"}:
            raise ValueError(f"Unexpected runtime payload: {name}")
        if name.startswith("third_party/MINIMA/data_engine/figs/"):
            continue
        add(path, f"code/{name}", code_archive.read(name))
    code_archive.close()

    for path in sorted((ROOT / "submission_materials/release_metadata_bundle").iterdir()):
        if path.is_file():
            add(path, f"metadata/{path.name}")
    for path in sorted((ROOT / "supplement/tables").glob("*")):
        if path.is_file():
            add(path, f"evaluation/supplement_tables/{path.name}")
    for path in sorted((ROOT / "figure_reconstruction").glob("fig*/source_data/*.csv")):
        add(path, f"evaluation/figure_sources/{path.parent.parent.name}/{path.name}")
    for name in ("benchmark_master_summary_20260628.csv",
                 "paper_ready_benchmark_tables_20260628.md"):
        add(ROOT / "submission_materials" / name, f"evaluation/{name}")

    provenance = {
        "code_commit": git(code, "rev-parse", "HEAD"),
        "manuscript_base_commit": git(ROOT, "rev-parse", "HEAD"),
        "manifest_canonical_sha256":
            "a092f7ad00c6e02ead3bd39de5c246001f1d4bebbc4105ba715ef37bbb202c6c",
        "candidate_pairs": 6039,
        "official_evaluation_pairs": 6037,
        "joint_dataset_owners": ["Nanning Normal University", "Guangxi University"],
        "documentation_path_adaptations": adapted,
        "excluded_assets": [
            "Raw dataset images", "Model weights", "Experiment JSONL logs",
            "Third-party data-engine example photographs", "Git history",
        ],
        "anonymized": False,
    }
    files["PACKAGE_PROVENANCE.json"] = json.dumps(
        provenance, ensure_ascii=False, indent=2
    ).encode("utf-8")
    files["README_SUPPLEMENT.md"] = (
        "# UAV-TAlign Code and Evaluation Supplement\n\n"
        "This offline package accompanies the manuscript; it is not a dataset deposit.\n"
        "The image archive and pretrained model weights must be obtained separately.\n\n"
        "- `code/`: versioned evaluation and pipeline source, dependency instructions, "
        "and upstream license notices. Begin with `code/README.md`.\n"
        "- `metadata/`: official evaluation manifest and integrity summaries.\n"
        "- `evaluation/`: numerical source tables for the figures and supplementary analyses.\n"
        "- `PACKAGE_PROVENANCE.json`: commits, canonical manifest hash, and exclusions.\n"
        "- `SHA256SUMS.txt`: actual byte hashes of all preceding files.\n\n"
        "All code files are byte-identical to the recorded code commit. Two documentation "
        "files may replace workstation drive examples with `<PROJECT_ROOT>`; any such "
        "adaptations are recorded. Table values and manifest content are unchanged.\n\n"
        "The dataset is jointly owned by Nanning Normal University and Guangxi University "
        "and is designated for release under CC BY 4.0. Original software uses Apache-2.0; "
        "third-party components retain their licenses. This package is not anonymized. "
        "Review the target journal's anonymity requirements before uploading it.\n\n"
        "Preserve the raw dataset as read-only. Use the official manifest and a unique "
        "output root for every new run. No new experiment is needed to inspect these tables.\n"
    ).encode("utf-8")
    files["SHA256SUMS.txt"] = "".join(
        f"{hashlib.sha256(data).hexdigest()}  {name}\n"
        for name, data in sorted(files.items())
    ).encode("utf-8")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(args.output, "x", compression=zipfile.ZIP_DEFLATED) as archive:
        for name, data in sorted(files.items()):
            archive.writestr(name, data)
    with zipfile.ZipFile(args.output) as archive:
        assert archive.testzip() is None
        assert all("\\" not in name for name in archive.namelist())
        for name, expected in files.items():
            assert archive.read(name) == expected
    print(json.dumps({
        "output": str(args.output),
        "files": len(files),
        "size_bytes": args.output.stat().st_size,
        "sha256": hashlib.sha256(args.output.read_bytes()).hexdigest(),
        "code_commit": provenance["code_commit"],
        "documentation_path_adaptations": adapted,
    }, indent=2))


if __name__ == "__main__":
    main()
