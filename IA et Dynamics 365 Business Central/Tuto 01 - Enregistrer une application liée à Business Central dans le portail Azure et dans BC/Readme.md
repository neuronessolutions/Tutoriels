# Tuto 01 - Enregistrer une application liée à Business Central et ses API dans le portail Azure et dans BC
> Version 2023.11.25.1, Auteur : Dominique Delaire

Dans ce premier tutoriel, nous allons apprendre comment enregistrer nos applis et services qui seront liés à Microsoft Dynamics 365 Business Central et à ses API pour créer des services d'intelligence artificielle à partir de Shellbots ou apps externes en lien avec l'ERP. 

**Pourquoi as t'on besoin d'enregistrer des applications lorsque nous voulons utiliser des données de notre ERP préféré ?**
En fait, avant il n'était pas nécessaire de s'authentifier ainsi. il était possible juste avec son nom d'utilisateur et une web api key paramétréé directement dans Business Central de se connecter aux API BC. Pour des raisons de sécurité et d'optimisation, **il faut maintenant enregistrer chacune de ses applications qui vont utiliser les API BC dans le portail Microsoft Azure et aussi maintenant dans Business central, une fois l'enregistrement fait dans Azure.**

## Prérequis
* Avoir un abonnement valide à Business Central ou une version d'essai
* Avoir un compte microsoft ou un compte microsoft avec un accès au portail Azure (vous pouvez obtenir un compte et des crédits gratuits si vous n'en avez pas encore !)

## Exemple et objectif du Tutoriel

Dans Business Central, nous avons différentes API disponibles et nous pouvons aussi définir les nôtres.

![Capture d’écran, le 2023-11-22 à 11 00 52](https://github.com/nuage365/Tutoriels/assets/102873102/d85e07e6-59d7-4214-8c31-482db4db9be9)

Pour nos tests, nous allons utiliser une API standard de Business Central qui fait référence aux clients de l'ERP. Enregistrer une application permet d'utiliser n'importe quelle API ou future API que nous pourrions publier :)

Voici ce que nous allons choisir pour nos tests comme web service : **allez dans l'écran Web services.**

![Capture d’écran, le 2023-11-22 à 11 01 21](https://github.com/nuage365/Tutoriels/assets/102873102/e586a529-d77f-4917-8c94-a29750f6cc85)

![Capture d’écran, le 2023-11-22 à 11 01 59](https://github.com/nuage365/Tutoriels/assets/102873102/db8dc20c-2194-421f-9502-faabe05f9a0f)

**Sélectionner la ligne comprenant la Page 22 Customers**

![Capture d’écran, le 2023-11-22 à 11 03 11](https://github.com/nuage365/Tutoriels/assets/102873102/f4910ee9-94f8-4197-8947-fec5856701eb)

**Et faites un copier coller de la valeur de la colonne "OData V4 Url" dans un fichier texte ou autre et qui nous servira plus tard pour les tests**

![Capture d’écran, le 2023-11-22 à 11 05 26](https://github.com/nuage365/Tutoriels/assets/102873102/017a149f-6f6e-4184-9260-ea2d6f2ecf6c)

**Cela devrait ressembler au même format que la ligne ci-dessous :**

![Capture d’écran, le 2023-11-22 à 11 06 06](https://github.com/nuage365/Tutoriels/assets/102873102/962e5728-65cc-4c16-8e02-61aa19cb330f)

## Enregistrement de notre application dans le portail Azure 
Nous allons maintenant passer aux choses sérieuses :)

> **Pour commencer, allez sur le portail de microsoft azure : [https://azure.microsoft.com/](https://azure.microsoft.com/)**

![Capture d’écran, le 2023-11-22 à 11 11 55](https://github.com/nuage365/Tutoriels/assets/102873102/bef57aa2-b4dc-4220-92f3-4f092d5ba25f)

> **Puis choisir le module "Inscription d'applications" et cliquez sur le bouton "+ Nouvelle inscription"**

![Capture d’écran, le 2023-11-22 à 11 17 23](https://github.com/nuage365/Tutoriels/assets/102873102/4d83175e-70c7-46b8-b173-f68242370f21)

> **Donnez lui un nom d'application** et qui reflète ce que vos applications ou services vont faire en lien avec Business Central.

> Puis dans **"Types de comptes pris en charge", indiquer "Comptes dans cet annuaire d'organisation uniquement"**
> Puis **dans l'écran "URI de redirection" choisissez Web et tapez l'adresse suivante : "https://businesscentral.dynamics.com/OAuthLanding.htm"**

> Ce fichier htm est utilisé pour gérer les échanges entre Business Central et les autres services à travers Azure Active Directory ou maintenant avec la nouvelle appellation "Microsoft Entra ID"

![Capture d’écran, le 2023-11-22 à 11 18 17](https://github.com/nuage365/Tutoriels/assets/102873102/c246ffb7-d64c-4ee7-bb2d-930e1315fd09)

> **Cliquez ensuite sur le bouton "S'inscrire"**

![Capture d’écran, le 2023-11-22 à 11 18 36](https://github.com/nuage365/Tutoriels/assets/102873102/47c75dd7-e4f1-4acf-8043-0879ea70c137)

> **Vous obtenez ainsi déjà votre "Client ID" (ID D'application (client)) que nous utiliserons plus tard dans le tutoriel.**
> **L'id de l'annuaire aussi est important pour se connecter à notre instance**

![Capture d’écran, le 2023-11-22 à 11 19 08](https://github.com/nuage365/Tutoriels/assets/102873102/dce71d59-f525-48b4-a4c0-28eba661088a)

> **Maintenant, nous allons générer aussi un "Secret ID" que nous utiliserons dans nos applications avec le Client ID et l'Id de l'annuaire.**
> **Pour cela, allez dans le menu "Certificats et Secrets" ou cliquez sur "Ajouter un certificat ou un secret".**

![Capture d’écran, le 2023-11-22 à 11 19 41](https://github.com/nuage365/Tutoriels/assets/102873102/ee8e9a90-26db-4d8b-a8ad-e4a72e767372)

> **Cliquez ensuite sur "Nouveau secret Client"**

![Capture d’écran, le 2023-11-22 à 11 20 00](https://github.com/nuage365/Tutoriels/assets/102873102/793cccea-e03d-40b0-93f8-086cacff25bb)

> **Ajoutez ensuite une description puis une date d'expiration. Ici, nous avons indiqué 6 mois mais vous pouvez personnaliser votre date d'expiration. A l'échéance, vous pourrez regénérer une clé afin que votre ou vos applications puissent fonctionner de nouveau et s'authentifier.**

![Capture d’écran, le 2023-11-22 à 11 20 57](https://github.com/nuage365/Tutoriels/assets/102873102/21618997-32d0-4475-8a93-2c04590192ae)

> **On obtient le secret Client dans la colonne "Valeur". Vous pouvez aussi la copier et la mettre quelque part, elle nous servira plus tard pour nos tests d'authentification.**

![Capture d’écran, le 2023-11-22 à 11 21 38](https://github.com/nuage365/Tutoriels/assets/102873102/0768e734-6cfe-482e-8a8d-c11681490924)

> **On peut générer plusieurs valeurs de Secret client pour chaque application ou par groupe d'applications si on le désire.**

![Capture d’écran, le 2023-11-22 à 11 22 32](https://github.com/nuage365/Tutoriels/assets/102873102/990ac474-4834-4d01-94b1-ce0557fc7b81)

> **Ensuite, il faut indiquer des autorisations pour compléter notre enregistrement d'application(s).**
> 
> **Allez dans le menu "API autorisées" puis cliquez sur le bouton "Ajouter une nouvelle autorisation"**

![Capture d’écran, le 2023-11-22 à 11 24 44](https://github.com/nuage365/Tutoriels/assets/102873102/7146c870-8f24-4fb9-9027-43906488f6ff)

> **Sélectionnez API "Dynamics 365 Business Central"**

![Capture d’écran, le 2023-11-22 à 11 24 59](https://github.com/nuage365/Tutoriels/assets/102873102/e067f4e1-64f0-4865-8da7-1f04a1de1f85)

> **Ensuite, il faut sélectionner le type d'autorisation : choisir "Autorisations d'application"**

![Capture d’écran, le 2023-11-22 à 11 25 37](https://github.com/nuage365/Tutoriels/assets/102873102/825624ef-8cd4-4ad7-82a9-a4c49ff50554)

> **Cochez les 4 autorisations et cliquez sur le bouton "Ajouter des autorisations"**

![Capture d’écran, le 2023-11-22 à 11 26 20](https://github.com/nuage365/Tutoriels/assets/102873102/4bebd678-2ef2-4ab1-a468-1d6e6a2ae3ca)

> **Une fois l'ajout d'autorisations effectuée, il faut ajouter un consentement de l'administrateur.**
> **Pour cela, cliquez sur "Accorder un consentement d'administrateur" (pour votre domaine)**

![Capture d’écran, le 2023-11-22 à 11 27 24](https://github.com/nuage365/Tutoriels/assets/102873102/dd08dc02-5f09-4f4a-91e1-e9cd4a44d315)

> **Un message de confirmation apparaît. Cliquez sur "Oui"**

![Capture d’écran, le 2023-11-22 à 11 27 44](https://github.com/nuage365/Tutoriels/assets/102873102/2ff7ed07-2532-4658-b2df-bf1f4fed3a7e)

> **Une fois effectué, le statut change et le consentement a été validé.**

![Capture d’écran, le 2023-11-22 à 11 28 07](https://github.com/nuage365/Tutoriels/assets/102873102/24429a4a-bf53-471a-95c2-31bf2feabb21)

> **En revenant à l'accueil de votre application, tout est correctement configuré. Vous avez votre "Client Id", votre ou vos "secrets clients" et votre Id de l'annuaire. Notez bien ces valeurs pour nos tests.**

![Capture d’écran, le 2023-11-22 à 11 29 50](https://github.com/nuage365/Tutoriels/assets/102873102/57599eb6-908f-495b-a774-1b68b7c41c44)

## Enregistrement de notre application dans Business Central 
Après avoir enregistré notre ou nos apps dans le portail Microsoft Azure, il est maintenant aussi nécessaire d'enregistrer notre application directement dans 365 Business Central

> **Pour cela, en tant qu'administrateur, dans l'instance BC où vous souhaitez lier votre app, chercher "Azure Active Directory Applications" ou "Microsoft Entrant ID app"**

![Capture d’écran, le 2023-11-22 à 13 38 00](https://github.com/nuage365/Tutoriels/assets/102873102/5b594896-5d48-44f1-9722-77cbf4fb6620)

> **Dans l'écran "Azure Active Directory Applications", créer un nouvel enregistrement.**

![Capture d’écran, le 2023-11-22 à 13 38 38](https://github.com/nuage365/Tutoriels/assets/102873102/befee953-068d-42c1-8ca6-930a26a4e205)

> **Dans le champ "Client ID", indiquez le "Client ID" de votre application enregistrée provenant d'Azure (ID D'application (client))**
> **Et indiquez une description puis la valeur "Enabled" dans le champ "State"**

![Capture d’écran, le 2023-11-22 à 13 43 01](https://github.com/nuage365/Tutoriels/assets/102873102/9db586fa-496d-4901-a0bd-53e41b966b4b)

> **Confirmez en cliquant sur "Oui"**

![Capture d’écran, le 2023-11-22 à 13 43 16](https://github.com/nuage365/Tutoriels/assets/102873102/b6d15b4a-d710-4677-abc6-3ccf9047cbb0)

> **Ensuite, nous allons ajouter un ensemble d'autorisations pour l'enregistrement**
> **Pour cela, cliquez sur "Nouvelle ligne" et choisir l'autorisation "D365 BUS FULL ACCESS"**

![Capture d’écran, le 2023-11-22 à 13 44 08](https://github.com/nuage365/Tutoriels/assets/102873102/4ee0a025-b398-4ec4-8250-f6a500329261)

![Capture d’écran, le 2023-11-22 à 13 44 42](https://github.com/nuage365/Tutoriels/assets/102873102/47b29c41-d8f5-46a8-b2ea-bf41221d83d9)

> **Revenez sur l'écran précédent et votre nouvelle Application Azure Active Directory ou Microsoft Entrant ID a été créée !**
> 
> **Tout est prêt maintenant pour tester nos inscriptions et les API Business Central via 2 méthodes :**
> - Via l'outil **Postman**
> - Via un programme **Python**

![Capture d’écran, le 2023-11-22 à 13 45 46](https://github.com/nuage365/Tutoriels/assets/102873102/c7c4b53b-143f-4c94-9764-af1f3eb82e3e)

## Tests des API Business central via nos 2 applications (Postman et programme Python) 
### Avec l'outil Postman

**L'outil Postman permet de tester des requêtes API et web et de voir les résultats de celles-ci.**

> **Première chose dans Postman, ajouter une requête de type GET, puis copier l'url vue au début qui était dans la colonne "OData V4 Url" représentant l'API Business Central des Clients (Customers)**

![Capture d’écran, le 2023-11-22 à 21 15 06](https://github.com/nuage365/Tutoriels/assets/102873102/8a65500f-f4e1-4457-bb62-7d7e48507dc4)


> **Puis dans l'onglet Authorization, dans la section de droite "Configure New Token", ajouter les éléments suivants :**
> - Token Name : Indiqué un nom (ce que vous voulez comme identifiant de token)
> - Grant Type : "Client Credentials"
> - Access Token Url : Indiquez https://login.microsoftonline.com/VotreIddel'annuaire/oauth2/v2.0/token (Id de l'annuaire dans votre app enregistré sur azure)
> - Client ID : Le client ID de votre app enregistré sur azure
> - Client Secret : Le client Secret de votre app enregistré sur azure
> - Scope : https://api.businesscentral.dynamics.com/.default
> - Client Authentication : Send as Basic Auth header

![Capture d’écran, le 2023-11-22 à 21 20 37](https://github.com/nuage365/Tutoriels/assets/102873102/05b12aba-a6b6-444e-a51a-eb980582675e)

> **Une fois les informations saisies, cliquez sur le bouton "Get new access Token"**

![Capture d’écran, le 2023-11-22 à 21 21 16](https://github.com/nuage365/Tutoriels/assets/102873102/e6307dcc-51d0-4690-903c-69e454dcfb9e)

> **Le Token est obtenu et nous sommes prêts à l'utiliser. Cliquez sur le bouton "Use Token".**

![Capture d’écran, le 2023-11-22 à 21 22 54](https://github.com/nuage365/Tutoriels/assets/102873102/cbfbf4f7-85ce-4bef-8f63-ab14b32f1dc4)

> **Nous sommes prêts à lancer la requête en cliquant sur le bouton "Send". Nous n'avons pas indiqué de paramètres donc nous aurons la liste de tous les clients de l'environnement de dev**

![Capture d’écran, le 2023-11-22 à 21 23 40](https://github.com/nuage365/Tutoriels/assets/102873102/ab1dbf09-58f2-4b9d-b0ba-7e5db992e186)

> **Voici le résultat de la requête au format Json avec la liste des clients. Le fichier Json contient le détail de chaque enregistrement client**

![Capture d’écran, le 2023-11-22 à 21 28 11](https://github.com/nuage365/Tutoriels/assets/102873102/ae995656-93b5-4e69-9e98-3f832445b293)

### Avec un programme Python

**Avec un simple programme en Python, nous sommes capables d'interroger la liste des clients de notre instance Business Central**

> **Même principe que Postman en utilisant les Id obtenus de notre enregistrement d'application effectué sur le portail Azure.**

![Capture d’écran, le 2023-11-22 à 22 09 45](https://github.com/nuage365/Tutoriels/assets/102873102/962724d1-9973-48ba-87c5-5cde532c07c6)

> **Résultat du programme Python à l'exécution**

![Capture d’écran, le 2023-11-22 à 22 55 31](https://github.com/nuage365/Tutoriels/assets/102873102/0242837c-3dbf-41b3-94cd-d19133e5494f)

**Fichier source en Python**

```python
import requests

# Remplacez ces valeurs par les informations de votre environnement Business Central
base_url = "https://api.businesscentral.dynamics.com/v2.0/0da8ae83-7b55-4b77-b6f2-c6b5267c540f/ShellbotsDev/ODataV4/Company('My%20Company')/"
client_id = "f03586ba-5c5c-488f-bd0b-9d4b99facae2"
client_secret = "0408Q~ljJ5RahrfgLXdSxqA-eUQUy~kG15j83aqc"
resource = "https://api.businesscentral.dynamics.com/"

# Demande d'autorisation OAuth
token_url = "https://login.microsoftonline.com/0da8ae83-7b55-4b77-b6f2-c6b5267c540f/oauth2/token"
data = {
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'client_secret': client_secret,
    'resource': resource
}

response = requests.post(token_url, data=data)
token = response.json().get('access_token')

# Interroger l'API pour récupérer la liste des clients
customers_url = base_url + 'Customers'
headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}

response = requests.get(customers_url, headers=headers)

if response.status_code == 200:
    customers = response.json()
    for customer in customers.get('value'):
        print(f"Nom du client : {customer.get('Name')}")
else:
    print(f"Erreur lors de la récupération des clients. Code d'erreur : {response.status_code}")
```

