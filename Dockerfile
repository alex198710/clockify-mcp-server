# Image de base Python
FROM python:3.8-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de dépendances
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste du projet
COPY . .

# Installer le projet
RUN pip install .

# Variables d'environnement par défaut (à remplacer lors du déploiement)
ENV CLOCKIFY_API_KEY=""
ENV WORKSPACE_ID=""

# Port pour le serveur JSON-RPC
EXPOSE 5000

# Point d'entrée pour le serveur
CMD ["python", "launch.py"]