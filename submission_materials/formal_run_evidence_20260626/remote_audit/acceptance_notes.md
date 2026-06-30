# P2-D Acceptance Notes

- Main experiment output root: `G:\UAV-TAlign\UAV-TAlign\outputs\ipt_p0c_12k_main`
- Protocol closure output root: `G:\UAV-TAlign\UAV-TAlign\outputs\ipt_p0d_protocol_closure`
- Main experiment launcher summary recorded `exit_code=0`.
- Main experiment validator recorded `ok=true`.
- The protocol launcher under the isolated experiment prefix failed because `pandas` was absent in `G:\UAV-TAlign\uav_talign_envs\uav-talign-e10a8be-py310`.
- Protocol closure was then generated read-only with `D:\anaconda\python.exe` using the same input directory, without modifying the raw main-experiment outputs.
- This audit folder stores copied key artifacts plus a SHA256 manifest for the source evidence files.
