from telegram.ext import Updater, CommandHandler
import pandas as pd
import logging


# Função de log que printa a mensagem de erro ocorrida
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s - %(message)s')
logger = logging.getLogger()
logger.setLevel(logging.ERROR)


def send_term(update, context):
  
  # Lê o dataset e seleciona uma palavra aleatória
  dictionary = pd.read_csv('dictionary.csv')
  term = dictionary['term'].sample(1).values[0]
  
  # Recebe o chat_id do usuário para enviar a mensagem de volta
  chat_id = update.message.chat_id
  
  # Envia a palavra e o audio
  context.bot.send_message(chat_id=chat_id, text=term)
  context.bot.send_voice(chat_id=chat_id, voice=open('audio/{}.mp3'.format(term), 'rb'))

def send_start(update, context):

  message = 'Olá! Está a fim de treinar o vocabulário de termos de AI escutando-os em inglês? Então vamos lá! Insira o comando /term que vou selecionar um dos 50 termos de IA extraídos do site https://www.telusinternational.com/insights/ai-data/article/50-beginner-ai-terms-you-should-know e te oferecer a pronúncia correta para você praticar.'
  chat_id = update.message.chat_id
  
  # Envia a palavra e o audio
  context.bot.send_message(chat_id=chat_id, text=message)
  
def main():
  
  # Iniciliza o bot e adiciona um command handler  
  updater = Updater('6263415416:AAHxOZO3WDG9sdnxVUkbqd1qdZKpbyP6k1g', use_context=True)
  updater.dispatcher.add_handler(CommandHandler('term', send_term))
  updater.dispatcher.add_handler(CommandHandler('start', send_start))
  
  # Gerencia o bot
  updater.start_polling()
  updater.idle()
  
if __name__ == '__main__':
  main()