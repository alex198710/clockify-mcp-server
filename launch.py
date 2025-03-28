#!/usr/bin/env python3
import os
from dotenv import load_dotenv
import sys
from src.clockify_client import ClockifyClient
from src.clickify_mcp_server import start_server

def validate_configuration():
    """
    Valide la configuration du serveur MCP
    """
    # Charger les variables d'environnement
    load_dotenv()

    # Vérifier les variables d'environnement
    api_key = os.getenv('CLOCKIFY_API_KEY')
    workspace_id = os.getenv('WORKSPACE_ID')

    if not api_key:
        print("Erreur : CLOCKIFY_API_KEY non définie")
        sys.exit(1)
    
    if not workspace_id:
        print("Erreur : WORKSPACE_ID non défini")
        sys.exit(1)

    try:
        # Tenter de se connecter à Clockify
        client = ClockifyClient(api_key)
        workspaces = client.list_workspaces()
        
        # Vérifier que le workspace existe
        workspace_exists = any(ws['id'] == workspace_id for ws in workspaces)
        if not workspace_exists:
            print(f"Erreur : Workspace {workspace_id} non trouvé")
            sys.exit(1)
        
        print("Configuration validée avec succès !")
    except Exception as e:
        print(f"Erreur de validation : {e}")
        sys.exit(1)

def main():
    validate_configuration()
    start_server()

if __name__ == '__main__':
    main()
