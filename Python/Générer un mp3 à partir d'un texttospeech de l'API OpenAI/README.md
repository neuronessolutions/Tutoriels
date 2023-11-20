# Tutoriel Générer un mp3 à partir d'une fonction texttospeech de l'API OpenAI 
> Version 2023.11.19.1, Auteur : Dominique Delaire

Dans ce tutoriel, nous allons en quelques lignes de code, générer un mp3 à partir d'un texte et de la fonction texttospeech d'OpenAI.

## Prérequis
* Avoir d'installé sur Windows, Mac ou Linux, une dernière version de Python ainsi que de la dernière version du module de OpenAI (pip install openai)
* Avoir une clé secrète OpenAI générée et valide dans votre profil OpenAI
![Capture d’écran, le 2023-11-19 à 22 41 14](https://github.com/nuage365/Tutoriels/assets/102873102/19bb9ed0-8cb2-4d09-94e3-c645906efea7)

## Créer le code source texttospeech_openai.py

```python
from pathlib import Path
from openai import OpenAI
import os
import sys
import shell_constants
os.environ["OPENAI_API_KEY"] = shell_constants.APIKEYOPENAI
# shell_constants.APIKEYOPENAI peut être remplacé ici par votre clé secrète d'OPENAI :)

client = OpenAI()

speech_file_path = Path(__file__).parent / "test.mp3"
response = client.audio.speech.create(
  model="tts-1",
  voice="alloy",
  input="Bonjour, vous êtes sur le GitHub de Nuage365 ! J'espère que vous allez bien ! J'aimerais vous raconter une histoire : il était une fois..."
)

response.stream_to_file(speech_file_path)
```
## En exécutant le programme texttospeech_openai.py, le fichier test.mp3 est créé !

![Capture d’écran, le 2023-11-19 à 22 29 22](https://github.com/nuage365/Tutoriels/assets/102873102/79b598f2-b96a-42b6-9977-7537fc77e59f)

J'ai converti le fichier audio test.mp3 en mp4 pour pouvoir l'écouter à partir de Github directement :) je joins le fichier test.mp3 avec le source dans les fichiers.

Cliquez sur le lien pour écouter le résultat : 
https://github.com/nuage365/Tutoriels/assets/102873102/d131a524-82aa-473d-a4fd-59480404d7b9


