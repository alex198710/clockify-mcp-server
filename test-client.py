import os
import unittest
from unittest.mock import patch
from src.clockify_client import ClockifyClient

class TestClockifyClient(unittest.TestCase):
    def setUp(self):
        # Utiliser une clé API de test factice
        self.api_key = 'test_api_key'
        self.client = ClockifyClient(self.api_key)
    
    @patch('requests.get')
    def test_list_workspaces(self, mock_get):
        # Simuler une réponse de l'API
        mock_response = mock_get.return_value
        mock_response.json.return_value = [
            {'id': 'workspace1', 'name': 'Test Workspace'}
        ]
        mock_response.raise_for_status.return_value = None

        workspaces = self.client.list_workspaces()
        self.assertEqual(len(workspaces), 1)
        self.assertEqual(workspaces[0]['name'], 'Test Workspace')
    
    @patch('requests.get')
    def test_list_projects(self, mock_get):
        # Simuler une réponse de l'API
        mock_response = mock_get.return_value
        mock_response.json.return_value = [
            {'id': 'project1', 'name': 'Test Project'}
        ]
        mock_response.raise_for_status.return_value = None

        projects = self.client.list_projects('workspace_id')
        self.assertEqual(len(projects), 1)
        self.assertEqual(projects[0]['name'], 'Test Project')

if __name__ == '__main__':
    unittest.main()
