# Bot com termos de AI
 
Você pode verificar o bot [aqui](http://t.me/chatrodbot_bot), digite o comando `/start` para receber instruções ou o comando `/term` para receber um termo de AI e o arquivo de audio.

## Prerequisitos

- [Google Text-to-Speech API](https://cloud.google.com/text-to-speech)
- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc)
- [requests](https://requests.readthedocs.io/en/master)
- [pandas](https://pandas.pydata.org/)

Você pode instalar todas bibliotecas usando este comando.

```
pip install -r requirements.txt
```

## Passos
### Preparando o Dataset
Antes de usar o bot, rode primeiro o `database.py` de forma a ter o `dictionary.csv` e os arquivos de audio. Certifique-se que você já configurou a variável de ambiente `GOOGLE_APPLICATION_CREDENTIALS` na sua credential path.

```
python database.py
```

### Rode o bot
Certifique-se de mudar `SEU_BOT_TOKEN` em `main.py` para o token do seu bot antes de rodar o comando abaixo.

```
python main.py
```
