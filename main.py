from gtts import gTTS
import telebot
# from time import sleep

def getMessage(messages):

    for message in messages:
        userId = message.from_user.id
        userText = message.text

        def bot_send_text(message):
            bot.send_message(userId, message)

        def bot_send_voice(voice):
            bot.send_audio(userId, voice)

        if userText == "/start":
            bot_send_text("Пришлите мне текст, я сделаю из него аудио")
        elif userText:
            bot_send_text("Подождите...")
            newVoice = gTTS(userText, lang="ru")
            newVoice.save(f"voice-{userId}.mp3")
            # sleep(5)
            with open(f"voice-{userId}.mp3", "rb") as voice:
                bot_send_voice(voice)

print("Бот слушает приказаний...")
bot = telebot.TeleBot("TOKEN")
bot.set_update_listener(getMessage)
bot.polling(none_stop=True)

while True:
    pass