# SuperTower

SuperTower est un jeu d'action et de plateforme réalisé en Python avec Pygame. À l'origine, c'était un projet de NSI réalisé en classe de première. Le projet utilisait alors un module qui n'est plus employé aujourd'hui. Pour faciliter le lancement du jeu sans installer cet ancien environnement, un exécutable Windows a été créé à partir d'une ancienne version de Python.

## Télécharger et jouer

Les versions prêtes à jouer sont disponibles dans la section [Releases](../../releases). Sous Windows, téléchargez `SuperTower.exe` depuis la version souhaitée et lancez-le. Python et Pygame ne sont pas nécessaires pour jouer avec l'exécutable.

## Lancer depuis les sources

Pour exécuter le jeu depuis les sources, installez Python 3.12, puis créez un environnement et installez les dépendances :

```powershell
py -3.12 -m venv build\.venv
.\build\.venv\Scripts\python.exe -m pip install -r packaging\requirements.txt
.\build\.venv\Scripts\python.exe src\Menu.py
```

## Construire l'exécutable

La construction de l'exécutable Windows nécessite Python 3.12. Depuis la racine du dépôt, exécutez :

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\packaging\build_windows.ps1
```

Le script crée l'environnement de compilation dans `build\.venv`, vérifie les ressources du jeu et génère `SuperTower.exe` à la racine du dépôt.

## Publier une version

La publication d'un tag au format `v1.0.0` déclenche l'action GitHub, qui construit l'exécutable Windows et l'ajoute à une nouvelle Release.
