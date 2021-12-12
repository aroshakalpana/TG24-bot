import os
impot telebot


bot = telebot. TteleBot("081e718b-7183-427e-872f-67307d7369a3")

@bot_message_handler(commands=["start"])
def send_welcome(massage):
    bot.reply_to(massge,"Hello I'm MAD BUDDY's Chat Bot")



@bot.message_handler(commands=["About me"])
def send_message(massage):
    bot.sen_massge(massge,"My name is - Arosha Kalpana"
                          "Age - 13 "
                          "Living - Southern province"
                          "My scholl is - H/Hungama Vijayaba  National School"
                          " My Free fire - Nick name is MAD BADDY"
                          "My Free Fire ID 2592290814 ")
@bot.message_handler(commands=["Grups"])
def send_message(massage):
    bot.sen_massge(massge,https://t.me/slfreefire23


    bot.polling()
