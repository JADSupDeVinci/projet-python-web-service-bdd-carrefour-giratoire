# INFORMATIONS

## Auteurs
- Ianice Lange
- Anatole Simonnet

## Utilisateur vues api
- username: user
- password: user

## ENDPOINTS
- **URL**: http://localhost:5000
### Récupérer toutes les couleurs
- **URL**: /getAll/Colors
- **Méthode**: GET
- **Description**: Récupère toutes les couleurs disponibles.

### Récupérer toutes les caractéristiques spéciales
- **URL**: /getAll/SpecialFeatures
- **Méthode**: GET
- **Description**: Récupère toutes les caractéristiques spéciales disponibles.

### Récupérer tous les environnements
- **URL**: /getAll/Environments
- **Méthode**: GET
- **Description**: Récupère tous les environnements disponibles.

### Récupérer tous les éléments
- **URL**: /getAll/Elements
- **Méthode**: GET
- **Description**: Récupère tous les éléments disponibles.

### Récupérer tous les types de dragons
- **URL**: /getAll/DragonTypes
- **Méthode**: GET
- **Description**: Récupère tous les types de dragons disponibles.

### Ajouter une couleur
- **URL**: /add/Color
- **Méthode**: POST
- **Description**: Ajoute une nouvelle couleur.
- **Paramètres**: color_name (string)

### Supprimer une couleur
- **URL**: /delete/Color
- **Méthode**: DELETE
- **Description**: Supprime une couleur existante.
- **Paramètres**: color_id (int)

### Mettre à jour une couleur
- **URL**: /put/Color
- **Méthode**: PUT
- **Description**: Met à jour une couleur existante.
- **Paramètres**: color_id (int), color_name (string)

### Générer un dragon aléatoire
- **URL**: /get/RandomDragon
- **Méthode**: GET
- **Description**: Génère un dragon aléatoire avec des attributs aléatoires.