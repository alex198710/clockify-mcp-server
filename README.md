# Clockify Time Tracker

## Description
Un outil en ligne de commande pour interagir avec l'API Clockify et gérer vos entrées de temps.

## Prérequis
- Python 3.8+
- Clé API Clockify

## Installation
1. Clonez le dépôt
2. Installez les dépendances :
   ```
   pip install -r requirements.txt
   ```

## Configuration
Créez un fichier `.env` à la racine du projet avec votre clé API :
```
CLOCKIFY_API_KEY=votre_clé_api_clockify
```

## Utilisation

### Lister les projets
```
python -m src.cli --workspace WORKSPACE_ID --action list-projects
```

### Lister les tags
```
python -m src.cli --workspace WORKSPACE_ID --action list-tags
```

### Générer un rapport de temps
```
python -m src.cli --workspace WORKSPACE_ID --action time-report \
    --project PROJECT_ID \
    --tags TAG1 TAG2 \
    --start-date 2024-01-01 \
    --end-date 2024-12-31
```

## Licence
[À définir]
