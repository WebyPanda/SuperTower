# SuperTower

SuperTower is an action-platformer game developed in Python using Pygame. Originally created as a high school NSI (*Numérique et Sciences Informatiques*) project in 11th grade (*première*), it initially relied on a module that is no longer used today. To make it easier to run the game without installing this legacy environment, a Windows executable was built using an older Python version.

## Download and Play

Ready-to-play build is available at root. Python and Pygame are not required to play using the executable.

## Running from Source

To run the game from source, install Python 3.12, create a virtual environment, and install the dependencies:

```powershell
py -3.12 -m venv build\.venv
.\build\.venv\Scripts\python.exe -m pip install -r packaging\requirements.txt
.\build\.venv\Scripts\python.exe src\Menu.py

```

## Building the Executable

Building the Windows executable requires Python 3.12. From the repository root, run:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\packaging\build_windows.ps1

```

The script creates the build environment in `build\.venv`, verifies game assets, and generates `SuperTower.exe` at the root of the repository.
