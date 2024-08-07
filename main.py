import telebot

bot = telebot.TeleBot("7439248998:AAGJDOZNtHeSYhzj4mcOFmQtt4BkToEt10k")


@bot.message_handler(commands=["start"])
def start_handler(message):
    bot.send_message(message.chat.id,
                     "Привет, в данном боте Вы узнаете топ молодых футболистов на евро 2024, и сколько им лет")


@bot.message_handler(commands=["top1"])
def top1_handler(message):
    bot.send_message(message.chat.id,
                     "1-е место — Ламин Ямаль.Испанский забил 1 гол,и отдал 4 передачи. На момент старта турнира ему было 16 лет 11 месяцев 1 день.")


@bot.message_handler(commands=["top2"])
def top2_handler(message):
    bot.send_message(message.chat.id,
                     "2-е место — Уоррен Заир-Эмери.Полузащитнику сборной Франции на начало Евро-2024 было 18 лет 3 месяца 6 дней.")


@bot.message_handler(commands=["top3"])
def top3_handler(message):
    bot.send_message(message.chat.id,
                     "3-е место — Лео Сауэр.Вингеру сборной Словакии на момент старта ЧЕ было 18 лет 5 месяцев 29 дней.")


bot.infinity_polling()