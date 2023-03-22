import telebot
import openai

bot = telebot.TeleBot('6230176688:AAFAdwT0EiXX4cnY0Z8zpwuD8B3MTBEVsaE')
openai.api_key = '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'

messages = [
    {"role": "system", "content": "You are a kind helpful assistant."},
]

@bot.message_handler(func=lambda message: True, content_types=['text'])
def handle_message(message):
    message_text = message.text
    messages.append({"role": "user", "content": message_text})
    chat = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages
    )
    reply = chat.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    bot.reply_to(message, reply)

bot.polling()
