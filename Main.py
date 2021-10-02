from telegram.ext import Updater
from telegram.ext import CommandHandler
from CoinmarketCap import GetPrice
from Binance import GetCandleStickInformations
from datetime import *
from time import mktime

telegram_bot_token = "1974825082:AAHbesAlUlHdP57zGvELHNsrHCZ4ziMmC28"

updater = Updater(token=telegram_bot_token, use_context=True)
dispatcher = updater.dispatcher


def A(update, context):
    chat_id = update.effective_chat.id
    symbol = context.args[0].upper()
    response = GetPrice(symbol)

    symbolOfCoin = response['data'][symbol]['symbol']
    nameOfCoin = response['data'][symbol]['name']
    priceOfCoin = response['data'][symbol]['quote']['USD']['price']
    strPriceOfCoin = f"{priceOfCoin:,.2f}"
    if(symbol == 'EFI'):
        strPriceOfCoin += f" ({round(priceOfCoin/0.2, 0):,.2f}X   Bu ay {277.77 * priceOfCoin:,.0f} dolar gelecek)"

    volume24H = '${:,.0f}'.format(
        response['data'][symbol]['quote']['USD']['volume_24h'])

    message = f"Symbol: {symbolOfCoin}\nName: {nameOfCoin}\nPrice: {strPriceOfCoin}\n24H Volume: {volume24H}"

    context.bot.send_message(chat_id=chat_id, text=message)


def B(update, context):
    chat_id = update.effective_chat.id
    symbol = context.args[0].upper()
    response = GetCandleStickInformations(symbol, "15m",  int(mktime((datetime.now(
    ) - timedelta(minutes=30)).timetuple())), int(mktime(datetime.now().timetuple())))

    context.bot.send_message(chat_id=chat_id, text="asdasdasdasdsadasdadsadas")


dispatcher.add_handler(CommandHandler("A", A))
dispatcher.add_handler(CommandHandler("B", B))
updater.start_polling()
