# coding=utf-8
from django_telegrambot.apps import DjangoTelegramBot
from django.views.decorators.csrf import csrf_exempt
import json
import telegram
from telegram.error import TelegramError
from django.http import JsonResponse, HttpResponse
from .models import ShopProductModel
from .utils import get_shop_products

bot_token = '1207325258:AAHnQUKZH82bX8IWrcG2UGrV43JNprOZEYA'


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


def update_shop(request):
    ShopProductModel.objects.all().delete()
    shop_objects = list()
    shop_products = get_shop_products()
    for shop_product in shop_products:
        title, description, link_to_website, image_url, price = shop_product
        price = int(price.split(',')[0])
        shop_product_object = ShopProductModel(title=title, description=description, link_to_website=link_to_website,
                                               image_url=image_url, price=price)
        shop_objects.append(shop_product_object)
    ShopProductModel.objects.bulk_create(shop_objects)
    return HttpResponse('<h1>Data was updated</h1>')
