import utils
import time
import telebot
import os

api_key = os.getenv("BOT_API_KEY")

bot = telebot.TeleBot(api_key)


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, f"Выбери валюту и следи за её курсом. "
                                      "Доступные валюты: USD(доллар), EUR(евро), GBP(фунт стрерлинга), CNY(юань)."
                                      "Если выбрал нужную валюту, просто напиши ее обозначение, например USD."
                                      "Если решил остановить, просто блокируй бота, при изменении валюты начни заново."
                                      "Можно выбрать до двух валют одновременно.")


@bot.message_handler()
def send_m(message):
    if message.text in ("USD", "EUR", "GBP", "CNY"):
        current_value = float(utils.get_json(message.text)["value_curr"])
        bot.send_message(message.chat.id, f"1 {message.text} = {current_value} руб.")

        while True:
            time.sleep(60)
            next_value = float(utils.get_json(message.text)["value_curr"])
            if next_value > current_value:
                bot.send_message(message.chat.id,
                                 f"Курс повысился: 1 {message.text} = {current_value} -> {next_value} руб.")
            elif next_value < current_value:
                bot.send_message(message.chat.id,
                                 f"Курс понизился: 1 {message.text} = {current_value} -> {next_value} руб.")


bot.polling(none_stop=True)
