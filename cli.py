import argparse
import os
from dotenv import load_dotenv
from .clockify_client import ClockifyClient
from datetime import datetime, timedelta

def main():
    # Charger les variables d'environnement
    load_dotenv()
    
    # Récupérer la clé API depuis les variables d'environnement
    api_key = os.getenv('CLOCKIFY_API_KEY')
    if not api_key:
        print("Erreur : Clé API Clockify non trouvée. Définissez CLOCKIFY_API_KEY dans .env")
        return
    
    # Créer le client Clockify
    client = ClockifyClient(api_key)
    
    # Configuration du parser d'arguments
    parser = argparse.ArgumentParser(description='Outil de gestion Clockify')
    parser.add_argument('--workspace', type=str, help='ID du workspace')
    parser.add_argument('--action', choices=['list-projects', 'list-tags', 'time-report'], required=True)
    parser.add_argument('--project', type=str, help='ID du projet pour le rapport de temps')
    parser.add_argument('--tags', type=str, nargs='+', help='Liste des tags pour le rapport de temps')
    parser.add_argument('--start-date', type=str, help='Date de début (YYYY-MM-DD)')
    parser.add_argument('--end-date', type=str, help='Date de fin (YYYY-MM-DD)')
    
    args = parser.parse_args()
    
    try:
        if args.action == 'list-projects':
            projects = client.list_projects(args.workspace)
            print("Projets :")
            for project in projects:
                print(f"- {project['name']} (ID: {project['id']})")
        
        elif args.action == 'list-tags':
            tags = client.list_tags(args.workspace)
            print("Tags :")
            for tag in tags:
                print(f"- {tag['name']} (ID: {tag['id']})")
        
        elif args.action == 'time-report':
            # Convertir les dates si fournies
            start_date = datetime.fromisoformat(args.start_date) if args.start_date else None
            end_date = datetime.fromisoformat(args.end_date) if args.end_date else None
            
            time_entries = client.get_time_entries(
                workspace_id=args.workspace,
                project_id=args.project,
                tag_ids=args.tags,
                start_date=start_date,
                end_date=end_date
            )
            
            print("Rapport des entrées de temps :")
            for entry in time_entries:
                print(f"- Projet: {entry.get('project', {}).get('name', 'N/A')}")
                print(f"  Durée: {entry.get('timeInterval', {}).get('duration', 'N/A')}")
                print(f"  Description: {entry.get('description', 'N/A')}")
                print("---")
    
    except Exception as e:
        print(f"Erreur : {e}")

if __name__ == '__main__':
    main()
