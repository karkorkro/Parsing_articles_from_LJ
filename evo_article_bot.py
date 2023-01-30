import telebot
import requests
from ljparsing import find_random_evo_article, show_tags

# токен придется поменять после получения оценки
TOKEN = '5963285639:AAEahwhPPYukAtLuGYOP2nvw2yw-JBfFFIw'
bot = telebot.TeleBot(TOKEN)
MAIN_URL = f'https://api.telegram.org/bot{TOKEN}'
url = f'{MAIN_URL}/getMe'
result = requests.get(url)
print(result.status_code)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, """Этот бот может искать статьи по запросу из блога Evo-lutio на LiveJournal. Доступны только статьи, находящиеся в публичном доступе в данном блоге. Бот сделан исключительно для удобства чтения, все авторские
права соблюдены""")


@bot.message_handler(commands=['help'])
def help_command(message):
    text = '''/random - команда для получения рандомной статьи
    /showtags - команда для получения списка тегов'''
    bot.reply_to(message, '/random - команда для получения рандомной статьи')


@bot.message_handler(commands=['random'])
def pull_random_article(message):
    bot.reply_to(message, find_random_evo_article())


@bot.message_handler(commands=['showtags'])
def show_tags(message):
    bot.reply_to(message, show_tags())


@bot.message_handler(content_types=['text'])
def respond_to_text(message):
    text = 'Бот реагирует только на команды, список команд можно посмотреть в меню или нажав /help'
    bot.reply_to(message, text)


bot.polling()