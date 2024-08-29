# Tutoriel Créer un GPT comme aide comptable
> Version 2024.08.28, Auteur : Dominique Delaire

![Capture d’écran, le 2024-08-28 à 21 07 45](https://github.com/user-attachments/assets/9dc760e6-dfe9-43b7-90ec-1c0fea9f4e2f)


Dans ce tutoriel, nous allons créer un simple GPT dédié à la comptabilité que nous nommerons "ComptaBot" permettant la génération d'écritures comptables en fonction de documents comme des factures d'achats ou de ventes, ou des prompts.
Le GPT pourra même consigner les écritures générées dans un fichier excel que nous aurons préalablement bâti avec un certain nombre de colonnes.

# Prérequis
* Avoir un compte ChatGPT entreprise ou ChatGPT Plus pour bénéficier de la fonctionnalité de création de GPTs 

## Etape 1 : Sur ChatGpt Plus ou entreprise, cliquez sur "Create a GPT" et remplir les informations de base de votre "GPT ComptaBot"

Voici ce que j'ai mis dans les instructions : 

![Capture d’écran, le 2024-08-28 à 21 50 56](https://github.com/user-attachments/assets/214d885a-269d-4dab-b000-b7c5d0af4258)

et les différentes options activées :

![Capture d’écran, le 2024-08-28 à 21 52 06](https://github.com/user-attachments/assets/95c24b8e-3857-4549-b1bf-6cd8120895cd)

Vous pourriez ajouter aussi des fichiers supplémentaires en pdf dans la base de connaissances pour suivre une méthode comptable (comptabilité d'exercice vs comptabilité de caisse) ou un plan comptable spécifique !

## Etape 2 : On sauvegarde ensuite notre GPT.
Il y a plusieurs possibilités :
* On le sauvegarde pour l'utiliser soi même en privé
* On le sauvegarde pour le partager avec ceux qui auront le lien
* On le rend public pour le partager aux plus grands nombres et le distribuer sur le GPT Store

## Etape 3 : Test de notre "ComptaBot" :)

**Premier test, je vais lui dire de me générer des écritures comptables correspondant au pdf suivant :**

### Il s'agit d'une facture d'achat pour les services de l'entreprise Bell

![Capture d’écran, le 2024-08-28 à 22 11 43](https://github.com/user-attachments/assets/e796f523-af63-42e2-b418-28b2afabd969)

### Donc, je lui soumets le document et la facture de bell au format pdf :

![Capture d’écran, le 2024-08-28 à 22 15 31](https://github.com/user-attachments/assets/6982de34-164b-4a68-bd01-22bbe4826601)

![Capture d’écran, le 2024-08-28 à 22 17 00](https://github.com/user-attachments/assets/18e87710-365f-400c-b0de-640c0a1182e3)

### Je lui demande d'utiliser les comptes du plan comptable français de 1982 (c'est celui que j'utilisais pendant mes études en finances et comptabilité :))

![Capture d’écran, le 2024-08-28 à 22 19 01](https://github.com/user-attachments/assets/98303bef-59c2-44d2-92eb-9204c5954a9c)

### Ensuite, j'ai créé un fichier excel vide avec une entête de colonne (date, compte de gl, description, montant débit, etc..) pour lui spécifier ensuite qu'il doit consigner les écritures générées dans ce fichier

![Capture d’écran, le 2024-08-28 à 22 20 37](https://github.com/user-attachments/assets/9fbd6fb2-fa85-4cc6-9efb-c770ee39b2eb)

### Donc dans le prochain prompt je lui demande de consigner les écritures qu'il a déterminé dans le fichier excel que je lui joins dans le gpt :)

![Capture d’écran, le 2024-08-28 à 22 23 17](https://github.com/user-attachments/assets/6f623694-2724-4a78-a34d-f7e15807bebd)

### Je télécharge le fichier Excel avec les écritures qu'il a consigné et voici le résultat : 

![Capture d’écran, le 2024-08-28 à 22 24 41](https://github.com/user-attachments/assets/2ba579b4-ed8a-47f6-89a4-a4a181079b7d)

### Ensuite, sans lui redonner le fichier excel qu'il a lui même modifié, je lui demande juste de me générer une écriture d'avance sur dividende pour une période donnée sans trop de précision

![Capture d’écran, le 2024-08-28 à 22 26 07](https://github.com/user-attachments/assets/7829bf0f-7d56-42b1-a713-bc1f9a2cbac2)

### Et voici le résultat : 

![Capture d’écran, le 2024-08-28 à 22 30 45](https://github.com/user-attachments/assets/85a10180-6d4d-4afc-bcf2-412f4c697338)

### Ensuite je lui demande de me générer le compte de résultat sans préciser les écritures. Il va prendre toutes les écritures de l'onglet écritures comptables sans que je lui dise. Je lui ai juste précisé qu'il fallait qu'il mette ce compte de résultat dans l'onglet correspondant. Ce qu'il a fait

![Capture d’écran, le 2024-08-28 à 22 31 39](https://github.com/user-attachments/assets/b3018a1c-a623-4557-999a-9f51c32affb9)

### Voici le résultat pour l'instant assez simple vu l'exemple que je lui ai donné : 

![Capture d’écran, le 2024-08-28 à 22 32 36](https://github.com/user-attachments/assets/98c03774-aaa7-4670-bae1-16c6d47fa4dc)

**Cela peut paraître simple mais il suffit de lui donner en amont des documents pour indiquer comment on veut gérer notre comptabilité et cela pourrait être un outil intéressant.
Ici, on en a fait un gpt mais on pourrait faire un outil beaucoup plus complexe et dédié pour automatiser des processus comptables en utilisant aussi l'API d'OpenAI**

**On pourrait lui demander aussi de faire des analyses sur des états financiers ou les soldes intermédiaires de gestion :)**

**Vous pourriez faire la même chose aussi avec Microsoft Copilot Studio pour créer votre propre Copilot :)**

> Comme d'habitude, Si vous avez des questions ou un projet en IA, Dynamics CRM ou PowerApps de Microsoft, vous pouvez me contacter sur [Linkedin](https://www.linkedin.com/in/dominiquedelaire/)
> Notre équipe sénior d'une vingtaine de consultants est là pour vous aider !
> Dominique





