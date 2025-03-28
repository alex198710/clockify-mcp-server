import os
import requests
from typing import List, Dict, Optional
from datetime import datetime, timedelta

class ClockifyClient:
    def __init__(self, api_key: str):
        """
        Initialise le client Clockify avec la clé API
        
        :param api_key: Votre clé API Clockify
        """
        self.base_url = "https://api.clockify.me/api/v1"
        self.headers = {
            "X-Api-Key": api_key,
            "Content-Type": "application/json"
        }
    
    def list_workspaces(self) -> List[Dict]:
        """
        Liste tous les workspaces accessibles
        
        :return: Liste des workspaces
        """
        url = f"{self.base_url}/workspaces"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()
    
    def list_projects(self, workspace_id: str) -> List[Dict]:
        """
        Liste les projets d'un workspace donné
        
        :param workspace_id: ID du workspace
        :return: Liste des projets
        """
        url = f"{self.base_url}/workspaces/{workspace_id}/projects"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()
    
    def list_tags(self, workspace_id: str) -> List[Dict]:
        """
        Liste les tags d'un workspace donné
        
        :param workspace_id: ID du workspace
        :return: Liste des tags
        """
        url = f"{self.base_url}/workspaces/{workspace_id}/tags"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()
    
    def get_time_entries(
        self, 
        workspace_id: str, 
        project_id: Optional[str] = None, 
        tag_ids: Optional[List[str]] = None,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None
    ) -> List[Dict]:
        """
        Récupère les entrées de temps selon les critères spécifiés
        
        :param workspace_id: ID du workspace
        :param project_id: ID du projet (optionnel)
        :param tag_ids: Liste des IDs de tags (optionnel)
        :param start_date: Date de début (optionnel)
        :param end_date: Date de fin (optionnel)
        :return: Liste des entrées de temps
        """
        url = f"{self.base_url}/workspaces/{workspace_id}/time-entries"
        
        # Paramètres de requête
        params = {}
        if project_id:
            params['project'] = project_id
        if tag_ids:
            params['tags'] = ','.join(tag_ids)
        if start_date:
            params['start'] = start_date.isoformat() + 'Z'
        if end_date:
            params['end'] = end_date.isoformat() + 'Z'
        
        response = requests.get(url, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()
