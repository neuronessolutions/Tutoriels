# Tuto 02 - Les 3 commandes shellbots pour gérer les instances Dynamics365 Business central
> Version 2024.01.18.1, Auteur : Dominique Delaire

Dans ce second tutoriel, nous allons voir les 3 principales commandes pour gérer les instances Business Central afin d'utiliser par la suite les fonctions pour explorer les données, les structures de données et la génération de code avec nos fonctions d'intelligence artificielle.

![screen1](https://github.com/nuage365/Tutoriels/assets/102873102/30e82b9f-b71e-4c3d-8844-099d6467ba70)


## Prérequis
* Avoir un abonnement valide à Business Central ou une version d'essai
* La dernière version de l'OS Shellbots et le noyau IA framework Shellbots version 1.2023.08.06 avec une licence Entreprise.
* Avoir suivi ou revoir le tutoriel 01 : https://github.com/nuage365/Tutoriels/tree/main/IA%20et%20Dynamics%20365%20Business%20Central/Tuto%2001%20-%20Enregistrer%20une%20application%20li%C3%A9e%20%C3%A0%20Business%20Central%20dans%20le%20portail%20Azure%20et%20dans%20BC
  
  
## Obtenir les instances Dynamics 365 Business Central d'un contexte shellbots

Pour obtenir les instances déjà paramétrées dans un contexte particulier, il suffit de taper la commande **"bc_getinstance"**.
Pour rappel, un contexte est une sorte de Projet. Chaque projet a un contexte et contient une base de données vectorielle qui lui est propre. Elle peut contenir des images, du texte, des données de l'ERP, de l'audio, etc...

![screen2](https://github.com/nuage365/Tutoriels/assets/102873102/17d6ecbf-a222-497a-96f2-40704bfb6343)

## Créer une nouvelle instance business central pour le contexte actuel

Pour ajouter une nouvelle instance de Business central afin de faire le lien avec celle-ci et les fonctions du framework, il suffit de taper la commande **"bc_addinstance**.
La commande demande différentes informations : 
- **Le nom de l'instance** : Le nom que vous souhaitez qui représente votre instance. Par exemple, le type d'environnement prod, dev, etc., la compagnie bc, etc.
- **Le Tenant id** : Celui que vous avez pour votre instance. (Voir Tuto 01) 
- **Le Client id** : Celui que vous avez créé dans le portail azure quand vous avez enregistré votre application. (Voir Tuto 01)
- **Le Secret id** : Celui que vous avez généré dans le portail azure quand vous avez enregistré votre application. (Voir Tuto 01) Quand vous saisissez le Secret Id, l'interface ne le montrera pas à l'écran.
- **L'url de base des api BC** : cela correspond à l'url de base pour accéder aux services web de Business Central. Attention, c'est par Compagnie. Si vous avez plusieurs compagnies, il faut créer une instance par compagnie :) 
  
![screen3](https://github.com/nuage365/Tutoriels/assets/102873102/baddd30b-ac47-45bb-8836-64fcd3d2f03e)

en refaisant un bc_getinstance, on obtient notre instance nouvellement créée dans le contexte actuel.

![screen4](https://github.com/nuage365/Tutoriels/assets/102873102/b0e28834-3944-43a2-a880-491ce9aa8f39)

## Supprimer une instance existante de Business Central

Pour supprimer une instance Business Central dans le contexte actuel, il suffit d'utiliser la commande **"bc_removeinstance"**

![screen5](https://github.com/nuage365/Tutoriels/assets/102873102/42d86457-f57c-4456-b246-d969dacaec2a)

Après suppression et en refaisant un bc_getinstance, l'instance a bien été supprimée. Attention, si l'instance spécifiée avait des objets générés comme du code ou un modèle de machine learning, il faudra utiliser la commande **"bc_objects_export_all"** avant de pouvoir supprimer une instance. Ceci pour éviter de perdre des objets générés par le moteur Ia de shellbots.

![screen6](https://github.com/nuage365/Tutoriels/assets/102873102/98fe7d76-1474-41e8-933a-d6001762ad95)

Si vous avez des questions, n'hésitez pas à m'envoyer une connexion sur Linkedin à https://www.linkedin.com/in/dominiquedelaire/
