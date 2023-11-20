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
