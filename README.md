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

### 5. Déploiement de l'API sur le cloud provider
- Création d'un fichier .github/workflows/deploy.yml
- Création d'un fichier .github/workflows/pull_request.yml

### 6. Mise en place d'une pipeline de déploiement
- Création d'un fichier .github/workflows/pull_request.yml

### 7. Mise en place d'une pipeline de déploiement continue
- Création d'un fichier .github/workflows/pull_request.yml

### 8. Test de charge avec l'outil de votre choix et observer l'autoscaling

### 9. Ajouter un endpoint /metrics en utilisant la librairie prometheus-client puis mettre a disposition une/des metriques d'utilisation de l'API
