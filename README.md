1/ Preparation

    a/ Creation d'un compte Google Cloud Platform :

        https://console.cloud.google.com/

    b/ Creer un nouveau projet en haut a gauche

    c/ Activer les API suivante :
        - Google Sheets API
        - Gmail API
        - Geocoding API
        - Places API
        - Google Drive API

    d/ Creer des identifiant
        - Dans la bar a gauche cliquer sur API et services puis dans identifiants
        - Cliquer sur Créer des identifiants en haut de la page puis sur ID client OAuth
        - Type d'application : Application de bureau
        - Nom : laisser par defaut
        - Créer
        - Telecharger le fichier .json en cliquant sur le bouton téléchargé dans la categories "ID clients OAuth 2.0"
        - renomer ce fichier en "credentials.json" et placer le dossier credentials
    e/
        entrer la commande suivante : "pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib gspread googlemaps"

2/ Exercices
    A partir des 3 libs importé dans main.py : Google Drive / Google Sheet / Google Maps vous devez :

    - creer un dossier sur GoogleDrive
    - upload un fichier sur GoogleDrive
    - suprimer un dossier sur GoogleDrive
    - creer un SpreadSheet dans un dossier "Workshop"
    - remplir un SpreadSheet
    - recuperer des coordonées les fonction de GoogleMaps
    - recuperer les infos des lieux à proximité avec les coordonnées
    - remplir le sheet avec les infos sur les lieux
