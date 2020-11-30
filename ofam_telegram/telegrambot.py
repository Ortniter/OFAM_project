from random import randint

from django_telegrambot.apps import DjangoTelegramBot
from .utils import creat_menu_markup, send_message_or_photo, get_models_and_its_querysets, sections, \
    get_data_from_json, send_sticker_with_markup, create_shop_markup

from telegram.ext import CommandHandler, InlineQueryHandler, MessageHandler, Filters
from telegram import InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardButton, InlineKeyboardMarkup, \
    ParseMode

from .models import ShopProductModel, MainMenuButtonModel, TelegramUser


def start(update, context):
    # reply_markup = creat_menu_markup(model=MainMenuButtonModel, main_menu=True)
    #
    # telegram_user, _ = TelegramUser.objects.update_or_create(
    #     chat_id=update.message.from_user.id, defaults={'chat_id': update.message.from_user.id,
    #                                                    'username': update.message.from_user.username,
    #                                                    'first_name': update.message.from_user.first_name,
    #                                                    'language_code': update.message.from_user.language_code}
    # )
    # text = get_data_from_json()['welcome_text']
    # context.bot.send_message(update.message.chat_id,
    #                          text=text,
    #                          reply_markup=reply_markup,
    #                          parse_mode=ParseMode.HTML)
    #
    # telegram_user.save()
    context.bot.send_message(update.message.chat_id,
                             text='hello',
                             parse_mode=ParseMode.HTML)


def inline_shop(update, context):
    query = update.inline_query.query
    if 'ofam_shop' in query:
        results = list()
        map_nums = {'1': 0, '2': 20, '3': 40, '4': 60, '5': 80, '6': 100, '7': 120}
        slice_num = map_nums[query[-1]]
        shop_items = ShopProductModel.objects.all()[slice_num:slice_num + 20]
        for item in shop_items:
            item_values = (item.title, item.price, item.description, item.link_to_website, item.image_url)
            name, price, description, link, photo = item_values

            keyboard = [[InlineKeyboardButton("Подивитись на сайті 😎", url=link)]]

            reply_markup = InlineKeyboardMarkup(keyboard)

            results.append(
                InlineQueryResultArticle(
                    id=name.upper()[:randint(15, 24)],
                    title=name,
                    thumb_url=photo,
                    description=f'{price} UAH',
                    reply_markup=reply_markup,
                    input_message_content=InputTextMessageContent(
                        message_text=f'{description}\nPrice: <a href="{photo}">{price} UAH</a>',
                        parse_mode=ParseMode.HTML,
                    )
                )
            )
        context.bot.answer_inline_query(update.inline_query.id, results)


def help(update, context):
    context.bot.sendMessage(update.message.chat_id, text='Help!')


def event(update, context):
    models_and_its_querysets = get_models_and_its_querysets()
    all_detail_titles = [title for queryset in models_and_its_querysets.values() for title in queryset]
    custom_main_menu_buttons = MainMenuButtonModel.objects.all().values_list('title', flat=True)

    if update.message.text in sections:
        model = sections[update.message.text]
        reply_markup = creat_menu_markup(model=model, main_menu=False)
        send_sticker_with_markup(update, context, reply_markup)

    elif update.message.text in all_detail_titles:
        for model, queryset in models_and_its_querysets.items():
            if update.message.text in queryset:
                model = model
                model_instance = model.objects.get(title=update.message.text)
                reply_markup = InlineKeyboardMarkup(
                    [[InlineKeyboardButton(text=model_instance.detail_url_text, url=model_instance.detail_url)]])
                send_message_or_photo(context,
                                      update,
                                      model_instance.image_url,
                                      model_instance.description,
                                      reply_markup)
                break

    elif update.message.text in custom_main_menu_buttons:
        model_instance = MainMenuButtonModel.objects.get(title=update.message.text)
        if update.message.text == 'Магазин 🛍':
            reply_markup = create_shop_markup()
        else:
            reply_markup = InlineKeyboardMarkup(
                [[InlineKeyboardButton(text=model_instance.detail_url_text, url=model_instance.detail_url)]])
        send_message_or_photo(context, update, model_instance.image_url, model_instance.description, reply_markup)

    elif update.message.text == 'Назад':
        reply_markup = creat_menu_markup(model=MainMenuButtonModel, main_menu=True)
        send_sticker_with_markup(update, context, reply_markup)


def main():
    dp = DjangoTelegramBot.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', help))
    dp.add_handler(MessageHandler(Filters.text, event))
    dp.add_handler(InlineQueryHandler(inline_shop))
