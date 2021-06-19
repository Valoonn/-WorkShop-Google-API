1/ Preparation

    a/ Création d'un compte Google Cloud Platform :

        https://console.cloud.google.com/

    b/ Créer un nouveau projet en haut a gauche

    c/ Activer les API suivante :
        - Google Sheets API
        - Gmail API
        - Geocoding API
        - Places API
        - Google Drive API

    d/ Créer des identifiant
        - Dans la bar à gauche cliquer sur API et services puis dans identifiants
        - Cliquer sur Créer des identifiants en haut de la page puis sur ID client OAuth
        - Type d'application : Application de bureau
        - Nom : laisser par défaut
        - Créer
        - Télécharger le fichier .json en cliquant sur le bouton téléchargé dans la catégories "ID clients OAuth 2.0"
        - renommer ce fichier en "credentials.json" et placer le dossier credentials
    e/
        entrer la commande suivante : "pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib gspread googlemaps"

2/ Exercices
    A partir des 3 libs importé dans main.py : Google Drive / Google Sheet / Google Maps vous devez :

    - créer un dossier sur GoogleDrive
    - upload un fichier sur GoogleDrive
    - supprimer un dossier sur GoogleDrive
    - créer un SpreadSheet dans un dossier "Workshop"
    - remplir un SpreadSheet
    - récuperer des coordonnées les fonction de GoogleMaps
    - récuperer les infos des lieux à proximité avec les coordonnées
    - remplir le sheet avec les infos sur les lieux
