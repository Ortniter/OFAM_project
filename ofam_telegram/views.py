# coding=utf-8
from django_telegrambot.apps import DjangoTelegramBot
from django.views.decorators.csrf import csrf_exempt
import json
import telegram
from telegram.error import TelegramError
from django.http import JsonResponse

bot_token = '1270547075:AAHb_afunhhW2CWQrZ84NWYCbvHVz-AoYNk'


@csrf_exempt
def index(request):
    bot = DjangoTelegramBot.getBot(bot_id=bot_token, safe=False)
    try:
        data = json.loads(request.body.decode("utf-8"))
    except:
        return JsonResponse({})

    dispatcher = DjangoTelegramBot.getDispatcher(bot_token, safe=False)

    try:
        update = telegram.Update.de_json(data, bot)
        dispatcher.process_update(update)
    except TelegramError as te:
        dispatcher.dispatchError(update, te)

    return JsonResponse({})
