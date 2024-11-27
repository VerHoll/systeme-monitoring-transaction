# Image de base avec Python
FROM python:3.11-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers nécessaires
COPY app/ /app/

# Installer les dépendances
RUN pip install --no-cache-dir -r /app/requirements.txt

# Exposer le port 8000 pour FastAPI
EXPOSE 8000

# Démarrer le serveur FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

