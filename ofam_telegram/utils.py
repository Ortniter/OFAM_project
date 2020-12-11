import json
import csv
import os
from random import choice

from telegram.error import BadRequest
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, KeyboardButton, ReplyKeyboardMarkup

from .models import ShopProductModel, EventModel, ExhibitionModel, VisitModel, TelegramUser

folder_path = os.path.dirname(os.path.abspath(__file__))


def get_data_from_json():
    with open(f'{folder_path}/static/menu_data.json', 'r') as json_file:
        menu_data_dict = json.load(json_file)
        return menu_data_dict


def get_shop_products():
    with open(f'{folder_path}/ofm_shop_items.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            yield row


def get_random_sticker():
    stickers_list = get_data_from_json()['stickers']
    return choice(stickers_list)


def creat_menu_markup(model, main_menu):
    button_titles = model.objects.all().values_list('title', flat=True)
    keyboard = [KeyboardButton(text=title) for title in button_titles]
    if main_menu:
        first_three_buttons = [KeyboardButton(text=title) for title in sections.keys()]
        keyboard = first_three_buttons + keyboard
    keyboard = [keyboard[i:i + 2] for i in range(0, len(keyboard), 2)]
    if not main_menu:
        keyboard.append([KeyboardButton(text='Назад')])
    reply_markup = ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)
    return reply_markup


def send_message_or_photo(context, update, photo, text, reply_markup):
    if update.message.text in sections:
        context.bot.delete_message(update.message.chat_id, update.message.message_id)
    if len(text) > 1020:
        context.bot.send_message(update.message.chat_id,
                                 text=text,
                                 reply_markup=reply_markup,
                                 parse_mode=ParseMode.HTML)
    else:
        context.bot.send_photo(update.message.chat_id,
                               photo=photo,
                               caption=text,
                               reply_markup=reply_markup,
                               parse_mode=ParseMode.HTML)  # parse_mode=ParseMode.HTML


sections = {
    'Події 🧐': EventModel,
    'Виставки 🖼': ExhibitionModel,
    'Візит 🎩': VisitModel
}


def get_models_and_its_querysets():
    models_and_its_querysets = dict()
    for model in sections.values():
        titles = model.objects.all().values_list('title', flat=True)
        models_and_its_querysets[model] = titles
    return models_and_its_querysets


def send_sticker_with_markup(update, context, reply_markup):
    telegram_user = TelegramUser.objects.get(chat_id=update.message.chat_id)
    previous_sticker_message = telegram_user.sticker_message

    context.bot.delete_message(update.message.chat_id, update.message.message_id)

    message = context.bot.send_sticker(update.message.chat_id,
                                       sticker=get_random_sticker(),
                                       reply_markup=reply_markup)
    try:
        context.bot.delete_message(update.message.chat_id,
                                   previous_sticker_message)  # telegram can delete only recent messages
    except BadRequest:  # if we try to delete old message it could cast BadRequest
        pass

    telegram_user.sticker_message = message.message_id
    telegram_user.save()


def create_shop_markup():
    keyboard = list()
    shop_items = ShopProductModel.objects.all()
    i = 0
    emoji_set = ('🟡', '🟠')
    for _ in shop_items[::20]:
        i += 1
        keyboard.append([InlineKeyboardButton(text=f'{emoji_set[i % 2]} Набор товарів - {i}',
                                              switch_inline_query_current_chat=f'ofam_shop_pack_{i}')])
    reply_markup = InlineKeyboardMarkup(keyboard)
    return reply_markup
