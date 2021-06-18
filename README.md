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
        - renomer ce fichier en "credentials.json" et placer le a la base du repo
    e/
        entrer la commande suivante : "pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib gspread"

2/ Lancer un programme

    Toujours lancer les programmes quand vous etes dans le fichier de ce dernier
