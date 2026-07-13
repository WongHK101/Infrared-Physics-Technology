$ErrorActionPreference = 'Stop'

Push-Location $PSScriptRoot
try {
    latexmk -xelatex -interaction=nonstopmode -halt-on-error -outdir=build_zh paper_zh.tex
    Copy-Item -LiteralPath 'build_zh\paper_zh.pdf' -Destination 'paper_zh.pdf' -Force
}
finally {
    Pop-Location
}
