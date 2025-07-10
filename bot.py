import telebot

TOKEN = "7944017796:AAE-p_wAebHwZKP4YGk0E9LruUOYdJmtxxw"
bot = telebot.TeleBot(TOKEN)

# Customize bot's appearance
@bot.message_handler(commands=['about'])
def about(message):
    bot.reply_to(message, "I'm Mantisatechbot, your friendly bot!")

# Explore Bot API documentation
@bot.message_handler(commands=['docs'])
def docs(message):
    bot.reply_to(message, "Check out the Bot API documentation at https://core.telegram.org/bots/api")

# Test and refine bot
@bot.message_handler(commands=['test'])
def test(message):
    bot.reply_to(message, "Testing 1, 2, 3!")

# Existing commands
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, "Welcome! You can use /menu to view available commands.")

@bot.message_handler(commands=['menu'])
def menu(message):
    bot.reply_to(message, " Menu Commands:\n/menu\n/pair\n/ping\n/about\n/docs\n/test", parse_mode='Markdown')

@bot.message_handler(commands=['pair'])
def pair(message):
    bot.reply_to(message, "Pair command executed!")

@bot.message_handler(commands=['ping'])
def ping(message):
    bot.reply_to(message, "Pong!")

bot.polling()
