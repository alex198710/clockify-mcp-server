import os
import json
from typing import Dict, Any
from jsonrpcserver import method, serve
from src.clockify_client import ClockifyClient

class ClockifyMCPServer:
    def __init__(self):
        # Récupérer les variables d'environnement
        api_key = os.getenv('CLOCKIFY_API_KEY')
        workspace_id = os.getenv('WORKSPACE_ID')
        
        if not api_key or not workspace_id:
            raise ValueError("CLOCKIFY_API_KEY et WORKSPACE_ID doivent être définis")
        
        self.client = ClockifyClient(api_key)
        self.workspace_id = workspace_id

    @method
    def list_tools(self) -> Dict[str, Any]:
        """
        Liste des outils disponibles pour le serveur MCP
        """
        return {
            "tools": [
                {
                    "name": "Clockify Projects",
                    "description": "Liste des projets Clockify",
                    "method": "list_projects"
                },
                {
                    "name": "Clockify Tags",
                    "description": "Liste des tags Clockify",
                    "method": "list_tags"
                },
                {
                    "name": "Clockify Time Entries",
                    "description": "Rapport des entrées de temps",
                    "method": "get_time_entries"
                }
            ]
        }

    @method
    def list_projects(self) -> Dict[str, Any]:
        """
        Récupère la liste des projets du workspace
        """
        try:
            projects = self.client.list_projects(self.workspace_id)
            return {
                "projects": [
                    {
                        "id": project['id'],
                        "name": project['name']
                    } for project in projects
                ]
            }
        except Exception as e:
            return {"error": str(e)}

    @method
    def list_tags(self) -> Dict[str, Any]:
        """
        Récupère la liste des tags du workspace
        """
        try:
            tags = self.client.list_tags(self.workspace_id)
            return {
                "tags": [
                    {
                        "id": tag['id'],
                        "name": tag['name']
                    } for tag in tags
                ]
            }
        except Exception as e:
            return {"error": str(e)}

    @method
    def get_time_entries(self, 
                          project_id: str = None, 
                          tag_ids: list = None, 
                          start_date: str = None, 
                          end_date: str = None) -> Dict[str, Any]:
        """
        Récupère les entrées de temps avec des filtres optionnels
        """
        try:
            from datetime import datetime
            
            # Convertir les dates si fournies
            start = datetime.fromisoformat(start_date) if start_date else None
            end = datetime.fromisoformat(end_date) if end_date else None
            
            time_entries = self.client.get_time_entries(
                workspace_id=self.workspace_id,
                project_id=project_id,
                tag_ids=tag_ids,
                start_date=start,
                end_date=end
            )
            
            return {
                "time_entries": [
                    {
                        "project": entry.get('project', {}).get('name', 'N/A'),
                        "duration": entry.get('timeInterval', {}).get('duration', 'N/A'),
                        "description": entry.get('description', 'N/A')
                    } for entry in time_entries
                ]
            }
        except Exception as e:
            return {"error": str(e)}

def start_server():
    """
    Démarre le serveur MCP
    """
    server = ClockifyMCPServer()
    serve(server)

if __name__ == '__main__':
    start_server()
