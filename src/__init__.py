"""
Package Clockify Time Tracker

Ce module fournit des outils pour interagir avec l'API Clockify
et générer des rapports de temps.
"""

__version__ = "0.1.0"
__author__ = "Votre Nom"

from .clockify_client import ClockifyClient
from .cli import main

__all__ = ['ClockifyClient', 'main']