from google.cloud import texttospeech
from bs4 import BeautifulSoup

import pandas as pd
import requests
import re


def get_terms():

  # Coleta dados do website e armazena a lista de termos
  url = 'https://www.telusinternational.com/insights/ai-data/article/50-beginner-ai-terms-you-should-know'
  print(url)
  page = requests.get(url)
  soup = BeautifulSoup(page.content, 'html.parser')
  result = []
  for term in soup.find_all('b'):
    if term != ' ':
      result += term
  
  while ' ' in result:
    result.remove(' ')
  print(result)

  # Retorna palavras únicas (boa prática, mas denecessário no caso)
  return set(result)


def create_audio(text, language='en-US'):

  # Insancia um cliente
  client = texttospeech.TextToSpeechClient()

  # Define a entrada de texto a ser sintetizada
  synthesis_input = texttospeech.SynthesisInput(text=text)

  # Cria a requisição de voz, seleciona o código da língua ("en-US") e o ssml
  # gênero da voz ("neutral")
  voice = texttospeech.VoiceSelectionParams(
    language_code=language,
    ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL)

  # Seleciona o tipo de arquivo do audio a ser retornado
  audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3)

  # Executa a requisição text-to-speech naentrada de texto com os parâmetros
  # da voz e do tipo de arquivo de audio
  response = client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)

  # A resposta do audio_content é binária.
  with open('audio/{}.mp3'.format(text), 'wb') as out:
    # Salva a resposta no arquivo de saída.
    out.write(response.audio_content)

if __name__ == "__main__":

  # Obtém a lista de termos de IA e obtém o audio para cada palavra ou termo
  terms = get_terms()

  for term in terms:
    create_audio(term)

  # Cria o dataframe de palavras e o salva como arquivo .csv 
  dictionary = pd.DataFrame(terms, columns=['term'])
  dictionary.to_csv('dictionary.csv', index=False)
