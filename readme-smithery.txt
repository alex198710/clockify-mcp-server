# Clockify Time Tracker MCP Server

## Compatibilité Smithery
Ce projet est configuré comme un MCP (Minecraft Protocol) server pour Smithery, permettant l'intégration avec Clockify.

### Prérequis Smithery
- Compte Smithery
- Clé API Clockify valide
- ID de Workspace Clockify

### Configuration
1. Créez un fichier `.env` avec :
   ```
   CLOCKIFY_API_KEY=votre_clé_api_clockify
   WORKSPACE_ID=votre_workspace_id
   ```

### Déploiement sur Smithery
1. Poussez le dépôt sur GitHub
2. Connectez votre dépôt à Smithery
3. Configurez les variables d'environnement dans Smithery

### Endpoints disponibles
- `/projects`: Liste les projets Clockify
- `/tags`: Liste les tags Clockify
- `/time-entries`: Récupère les entrées de temps

## Développement et Tests
```bash
# Installer les dépendances
pip install -r requirements.txt

# Lancer les tests
python -m unittest discover tests
```
