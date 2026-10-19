import os
import runpy
import sys
from pathlib import Path


ENTRY_SCRIPTS = {"Menu.py", "Regle.py", "Jeux.py", "NiveauFinal.py"}
_DLL_DIRECTORY_HANDLES = []


class _ScreenTransition(Exception):
    def __init__(self, script_name: str) -> None:
        self.script_name = script_name


def _configure_dll_search_path() -> None:
    if os.name != "nt":
        return

    directories = []
    if getattr(sys, "frozen", False):
        bundle_root = Path(sys._MEIPASS)
        directories.extend((bundle_root, bundle_root / "pygame"))

    for directory in directories:
        if directory.is_dir():
            os.environ["PATH"] = str(directory) + os.pathsep + os.environ.get("PATH", "")
            _DLL_DIRECTORY_HANDLES.append(os.add_dll_directory(str(directory)))


_configure_dll_search_path()


def resource_root() -> Path:
    if getattr(sys, "frozen", False):
        bundle_path = getattr(sys, "_MEIPASS", None)
        if not isinstance(bundle_path, str):
            raise RuntimeError("PyInstaller did not provide its bundled resource path.")
        return Path(bundle_path)
    return Path(__file__).resolve().parent.parent


def asset_path(relative_path: str | Path) -> str:
    relative = Path(relative_path)
    candidates = []
    root = resource_root()

    candidates.append((root / relative).resolve())
    if relative.parts and relative.parts[0] == "assets":
        candidates.append((root / Path(*relative.parts[1:])).resolve())

    if getattr(sys, "frozen", False):
        project_root = Path(__file__).resolve().parent.parent
        executable_root = Path(sys.executable).resolve().parent
        candidates.extend(
            [
                (project_root / relative).resolve(),
                (project_root / "assets" / relative).resolve(),
                (project_root / "assets" / Path(*relative.parts[1:])).resolve()
                if relative.parts and relative.parts[0] == "assets"
                else None,
                (executable_root / relative).resolve(),
                (executable_root / "assets" / Path(*relative.parts[1:])).resolve()
                if relative.parts and relative.parts[0] == "assets"
                else None,
            ]
        )

    seen = set()
    for path in candidates:
        if path is None:
            continue
        normalized = path.resolve(strict=False)
        if normalized in seen:
            continue
        seen.add(normalized)
        if normalized.is_file():
            return str(normalized)

    attempted = ", ".join(str(path) for path in seen)
    raise FileNotFoundError(
        f"Game asset not found: {relative}. Searched: {attempted}"
    )


def launch_script(script_name: str) -> None:
    if script_name not in ENTRY_SCRIPTS:
        raise ValueError(f"Unknown game screen: {script_name}")

    raise _ScreenTransition(script_name)


def run_game(initial_script: str) -> None:
    if initial_script not in ENTRY_SCRIPTS:
        raise ValueError(f"Unknown game screen: {initial_script}")

    root = resource_root()
    script_directory = root / "scripts" if getattr(sys, "frozen", False) else root / "src"
    sys.path.insert(0, str(script_directory))

    script_name = initial_script
    while True:
        script_path = script_directory / script_name
        if not script_path.is_file():
            raise FileNotFoundError(f"Game screen not found: {script_path}")
        try:
            runpy.run_path(str(script_path), run_name="__supertower_screen__")
        except _ScreenTransition as transition:
            script_name = transition.script_name
        else:
            return
