# Utilisez une image Python 3.9 comme image de base
FROM python:3.9

# Créez le répertoire de travail de l'application
WORKDIR /app

# Copiez les fichiers requirements.txt dans le conteneur
COPY requirements.txt .

# Installez les dépendances de l'application
RUN pip install --no-cache-dir -r requirements.txt

# Copiez tout le reste de l'application dans le conteneur
COPY . .

# Exécutez l'application
CMD [ "python", "test.py" ]
