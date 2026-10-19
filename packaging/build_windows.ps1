param(
    [string]$PythonPath
)

$ErrorActionPreference = "Stop"
$Root = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
Set-Location $Root

$BuildDirectory = Join-Path $Root "build"
New-Item -ItemType Directory -Path $BuildDirectory -Force | Out-Null
$BuildEnvironment = Join-Path $BuildDirectory ".venv"
$BuildPython = Join-Path $BuildEnvironment "Scripts\python.exe"
if (-not (Test-Path -LiteralPath $BuildPython)) {
    if ($PythonPath) {
        & $PythonPath -m venv $BuildEnvironment
    }
    else {
        if (-not (Get-Command py -ErrorAction SilentlyContinue)) {
            throw "Python 3.12 is required. Install it or pass -PythonPath to its executable."
        }
        & py -3.12 -m venv $BuildEnvironment
    }
    if ($LASTEXITCODE -ne 0) {
        throw "Could not create the build environment."
    }
}

& $BuildPython -m pip install -r (Join-Path $PSScriptRoot "requirements-build.txt")
if ($LASTEXITCODE -ne 0) {
    throw "Could not install the build requirements."
}

& $BuildPython (Join-Path $PSScriptRoot "verify_paths.py")
if ($LASTEXITCODE -ne 0) {
    throw "Source asset path verification failed."
}

$Stage = Join-Path $BuildDirectory "package_data"
$ScriptsStage = Join-Path $Stage "scripts"
$AssetsStage = Join-Path $Stage "assets"
if (Test-Path -LiteralPath $Stage) {
    Remove-Item -LiteralPath $Stage -Recurse -Force
}
New-Item -ItemType Directory -Path $ScriptsStage, $AssetsStage -Force | Out-Null

Get-ChildItem -LiteralPath (Join-Path $Root "src") -File -Filter "*.py" |
    Copy-Item -Destination $ScriptsStage

$AssetDirectories = @("Img", "Images", "Musiques", "image_etoile")
foreach ($Directory in $AssetDirectories) {
    $Source = Join-Path (Join-Path $Root "assets") $Directory
    if (-not (Test-Path -LiteralPath $Source -PathType Container)) {
        throw "Required game assets are missing: $Source"
    }
    Copy-Item -LiteralPath $Source -Destination $AssetsStage -Recurse
}

$Arguments = @(
    "-m", "PyInstaller",
    "--noconfirm",
    "--clean",
    "--onefile",
    "--windowed",
    "--name", "SuperTower",
    "--distpath", $Root,
    "--workpath", (Join-Path $BuildDirectory "pyinstaller"),
    "--specpath", $BuildDirectory,
    "--hidden-import", "pygame",
    "--collect-all", "pygame",
    "--add-data", "$ScriptsStage;scripts",
    "--add-data", "$AssetsStage;assets"
)

$Arguments += (Join-Path $Root "src\Menu.py")
& $BuildPython @Arguments
if ($LASTEXITCODE -ne 0) {
    throw "PyInstaller failed to build the game."
}

$Executable = Join-Path $Root "SuperTower.exe"
if (-not (Test-Path -LiteralPath $Executable -PathType Leaf)) {
    throw "PyInstaller finished without creating $Executable"
}

$PreviousAudioDriver = $env:SDL_AUDIODRIVER
$env:SDL_AUDIODRIVER = "dummy"
try {
    & $Executable --verify-bundle
    if ($LASTEXITCODE -ne 0) {
        throw "The executable failed its bundled resources or music check."
    }
}
finally {
    if ($null -eq $PreviousAudioDriver) {
        Remove-Item Env:\SDL_AUDIODRIVER -ErrorAction SilentlyContinue
    }
    else {
        $env:SDL_AUDIODRIVER = $PreviousAudioDriver
    }
}

Write-Host "Windows game ready: $Executable"
