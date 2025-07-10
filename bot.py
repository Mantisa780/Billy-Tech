import telebot

TOKEN = "7944017796:AAE-p_wAebHwZKP4YGk0E9LruUOYdJmtxxw"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, "Welcome! You can use /menu to view available commands.")

@bot.message_handler(commands=['menu'])
def menu(message):
    bot.reply_to(message, " Menu Commands:\n/menu\n/pair\n/ping", parse_mode='Markdown')

@bot.message_handler(commands=['pair'])
def pair(message):
    bot.reply_to(message, "Pair command executed!")

@bot.message_handler(commands=['ping'])
def ping(message):
    bot.reply_to(message, "Pong!")

bot.polling()
