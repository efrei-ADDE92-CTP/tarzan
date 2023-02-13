# project : Application of Big Data
# Subject : Déployer, au travers d'une API, un modèle entrainé de prediction en utilisant la philosophie DevOps sur un cloud provider

## Etapes de réalisation

### 1. Création d'un compte sur le cloud provider
Credentials a disposition sur l'organisation Github
- AZURE_CREDENTIALS service account pour s'authentifier avec l'API Azure
- REGISTRY_LOGIN_SERVER lien de la registry (efreiprediction.azurecr.io)
- REGISTRY_USERNAME username de la registry
- REGISTRY_PASSWORD password pour la registry
- RESOURCE_GROUP resource group Azure (ADDE92-CTP)

### 2. Création d'un container registry
- Création d'un container registry sur Azure
- Création d'un container registry sur Github

### 3. Training du modèle (Iris avec scikit-learn KNN) et export (joblib.dump)
- Création d'un fichier train.py
- Création d'un fichier requirements.txt
- Création d'un fichier Dockerfile
- Création d'un fichier .dockerignore
- Création d'un fichier .gitignore
- Création d'un fichier .github/workflows/train.yml
- Création d'un fichier .github/workflows/push.yml
- Création d'un fichier .github/workflows/pull_request.yml

### 4. Intégrer son modèle entrainé dans une API
- Création d'un fichier app.py
- Création d'un fichier requirements.txt
- Création d'un fichier Dockerfile
- Création d'un fichier .dockerignore
- Création d'un fichier .gitignore
- Création d'un fichier .github/workflows/push.yml
- Création d'un fichier .github/workflows/pull_request.yml

### Integrate Dockerfile to the project
- Création d'un fichier Dockerfile:  
```dockerfile
# create me my Dockerfile
FROM python:3.8-slim

# install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# set the working directory to /app
WORKDIR /app

# copy the content of the local directory to the working directory
COPY . /app

# Expose port 5000
EXPOSE 5000

# run the command to start app
CMD flask run --host 0.0.0.0 --port=5000
```	
To test the Dockerfile after creating it, run the following command:  
```bash
docker build -t prediction:latest .
# We now have a new image called weatherapp.

# We run our image using the following command:
docker run -p 5000:5000 prediction
```

We will use a linter to check the syntax of our Dockerfile. 
The linter choosed is hadolint.  
```bash
# Install hadolint
docker run --rm -i hadolint/hadolint

# Run hadolint on our dockerfile
docker run --rm -i hadolint/hadolint < Dockerfile
```

### 5. Déploiement de l'API sur le cloud provider
- Création d'un fichier .github/workflows/deploy.yml
- Création d'un fichier .github/workflows/pull_request.yml

### 6. Mise en place d'une pipeline de déploiement
- Création d'un fichier .github/workflows/pull_request.yml

### 7. Mise en place d'une pipeline de déploiement continue
- Création d'un fichier .github/workflows/pull_request.yml

### 8. Test de charge avec l'outil de votre choix et observer l'autoscaling

### 9. Ajouter un endpoint /metrics en utilisant la librairie prometheus-client puis mettre a disposition une/des metriques d'utilisation de l'API
