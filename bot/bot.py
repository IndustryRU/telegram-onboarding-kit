# This this code for demo bot of Telegram Onboarding Kit
#
# Use this code as an example of how to use Telegram Onboarding Kit in your bot:
# 1. How to add URL of your Mini App onboadring to button
# 2. How to get data from Mini App onboadring (e.g. filled in form or product info)
# 3. How to send ivoices and handle successful payments for Telegram Payments/👛 Wallet Pay
#
# Happy coding!


import json
import os
import re
import urllib.parse
import uuid
from typing import Any, Dict, Optional, Tuple
import httpx
from dotenv import load_dotenv

from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    LabeledPrice,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    Update,
    User,
    WebAppInfo,
)
from telegram.constants import ChatAction, ParseMode
from telegram.ext import (
    ApplicationBuilder,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    PreCheckoutQueryHandler,
    filters,
)


# region: helper functions
def get_user_data(user: User) -> Dict[str, Any]:
    """Get user data from user object"""
    return {
        "language_code": user.language_code,
    }


def add_get_params_to_url(url: str, user_data: Dict[str, Any]):
    query_string = urllib.parse.urlencode(user_data)
    return f"{url}?{query_string}"


def remove_html_tags(text: str) -> str:
    """Remove html tags from a string and replace <br> tags with a space"""
    # replace <br> tags with a space
    text = re.sub("<br.*?>", " ", text)

    # remove all other HTML tags
    return re.sub("<.*?>", "", text)


# endregion: helper functions


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_data = get_user_data(update.effective_user)

    text = (
        f"♥️ Привет! Добро пожаловать в Кафе у моря <a href='https://yalta-fresh.ru/'>YALTA FRESH</a>\n"
        f"\n"
        f"Лучше всего взаимодействовать со мной через 📱 мобильное устройство\n"
    )

    user_data = get_user_data(update.effective_user)

    reply_markup = ReplyKeyboardMarkup.from_column(
        [
            KeyboardButton(
                text="🗒 Меню YALTA FRESH",
                web_app=WebAppInfo(
                    url=add_get_params_to_url(
                        "https://industryru.github.io/telegram-onboarding-kit/", user_data
                    )
                ),
            ),
            KeyboardButton(
                text="✍️ Сделать онлайн предзаказ",
                web_app=WebAppInfo(
                    url=add_get_params_to_url("https://forms.yandex.ru/cloud/68111da390fa7b25283b4f5b/", user_data)
                ),
            ),
            KeyboardButton(
                text="ℹ️ Информация для Вас",
                web_app=WebAppInfo(
                    url=add_get_params_to_url(
                        "https://industryru.github.io/telegram-onboarding-kit/", user_data
                    )
                ),
            ),
            KeyboardButton(
                text="⭐️ Оставить отзыв / предложение",
                web_app=WebAppInfo(
                    url=add_get_params_to_url(
                        "https://forms.yandex.ru/cloud/681172ec505690ca72036f1b", user_data
                    )
                ),
            ),
            KeyboardButton(
                text="❓ О YALTA FRESH",
                web_app=WebAppInfo(
                    url=add_get_params_to_url(
                        "https://yalta-fresh.ru/", user_data
                    )
                ),
            ),
            
        ]
    )

    await update.effective_message.reply_text(
        text=text,
        reply_markup=reply_markup,
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=True,
    )

async def instruction(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_data = get_user_data(update.effective_user)

    text = (
        f"Инструкция по работе с системой <a href='https://marketbox.team/'>MarketBox</a>\n"        
    )

    user_data = get_user_data(update.effective_user)

    reply_markup = ReplyKeyboardMarkup.from_column(
        [
            KeyboardButton(
                text="1️⃣ Быстрый старт",
                web_app=WebAppInfo(
                    url="https://industryru.github.io/telegram-onboarding-kit/"
                ),
            ),
            KeyboardButton(
                text="2️⃣ Для исполнителей",
                web_app=WebAppInfo(
                    url="https://industryru.github.io/telegram-onboarding-kit/?page=1"
                ),
            ),
            KeyboardButton(
                text="3️⃣ Для менеджеров и распределителей",
                web_app=WebAppInfo(
                    url="https://industryru.github.io/telegram-onboarding-kit/?page=2"
                ),
            ),
        ]
    )

    await update.effective_message.reply_text(
        text=text,
        reply_markup=reply_markup,
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=True,
    )

async def task(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_data = get_user_data(update.effective_user)


    text = (
        f"Создавать задачи и заметки могут только зарегистрированые пользователи системы <a href='https://marketbox.team/'>MarketBox</a> с соответствующими правами доступа\n"        
        f"\n"
        f"Нажмите ниже на кнопку ✍️ Создать задачу, при необходимости войдите в систему, заполните форму формирования задачи и подтвердите кнопкой Создать задачу\n"  
    )

    user_data = get_user_data(update.effective_user)

    reply_markup = ReplyKeyboardMarkup.from_column(
        [
            KeyboardButton(
                text="✍️ Создать задачу",
                web_app=WebAppInfo(
                    url=add_get_params_to_url(
                        "https://forms.yandex.ru/cloud/671613e0068ff00274e053ba/", user_data
                    )
                ),
            ),
            KeyboardButton(
                text="🗒 Создать заметку",
                web_app=WebAppInfo(
                    url=add_get_params_to_url(
                        "https://forms.yandex.ru/cloud/6718c34284227c4660549ad1/", user_data
                    )
                ),
            ),
            KeyboardButton(
                text="🍳 Открыть заметки",
                web_app=WebAppInfo(
                    url=add_get_params_to_url(
                        "https://tracker.yandex.ru/issues/7", user_data
                    )
                ),
            ),
        ]
    )

    await update.effective_message.reply_text(
        text=text,
        reply_markup=reply_markup,
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=True,
    )

async def connect(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_data = get_user_data(update.effective_user)


    text = (
        f"Отправить запрос на подключение к системе <a href='https://marketbox.team/'>MarketBox</a> и начать предоставлять свои услуги в связке с командой профессионалов в сфере маркетинга и рекламы достаточно просто!\n"        
        f"\n"
        f"Нажмите ниже на кнопку:\n"  
        f"💻 Заявка на регистрацию в системе\n"  
        f"\n"
        f"Укажите информацию о себе в полях формы и отправьте запрос на подключение.\n"  
        
    )

    user_data = get_user_data(update.effective_user)

    reply_markup = ReplyKeyboardMarkup.from_column(
        [
            KeyboardButton(
                text="💻 Заявка на регистрацию в системе",
                web_app=WebAppInfo(
                    url="https://forms.yandex.ru/cloud/67160daee010db024de89cb0/?iframe=1"
                ),
            ),
            
        ]
    )

    await update.effective_message.reply_text(
        text=text,
        reply_markup=reply_markup,
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=True,
    )

async def info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_data = get_user_data(update.effective_user)


    text = (
        f"<a href='https://marketbox.team/'>MarketBox</a> - интегрированная система, которая <b>решает вопросы бизнеса</b> в сфере маркетинга и рекламы.\n"        
        f"\n"
        f"Система аккумулирует (объединяет) профессионалов и специалистов высокого уровня (<b>WaY BabaY</b>), распределяет, контролирует и анализирует работу над задачами для эффективной и слаженной работы в команде.\n"  
        f"\n"
        f"Для получения более подробной информации посетите наш сайт по кнопке ❓ О MarketBox.\n"  
        
    )

    user_data = get_user_data(update.effective_user)

    reply_markup = ReplyKeyboardMarkup.from_column(
        [
            KeyboardButton(
                text="⭐️ Пройти опрос",
                web_app=WebAppInfo(
                    url=add_get_params_to_url(
                        "https://forms.yandex.ru/cloud/6718d2e9e010db2dae4f22a9/", user_data
                    )
                ),
            ),
            KeyboardButton(
                text="❓ О MarketBox",
                web_app=WebAppInfo(
                    url="https://marketbox.team/"
                ),
            ),
            
        ]
    )

    await update.effective_message.reply_text(
        text=text,
        reply_markup=reply_markup,
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=True,
    )

async def get_data_from_mini_app(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    """This handler is called when user sends data from mini app"""

    data = json.loads(update.effective_message.web_app_data.data)
    payload, product = data["payload"], data["product"]

    # send received payload
    if payload:
        payload_str = json.dumps(payload, indent=4)
        text = f"📦 Got data from onboarding:\n" f"{payload_str}"

        await update.effective_message.reply_text(
            text=text,
            reply_markup=ReplyKeyboardRemove(),
        )

    await send_invoice(update, context, product)


async def send_invoice(
    update: Update, context: ContextTypes.DEFAULT_TYPE, product: Dict
) -> None:
    if product["payment_method"] not in context.bot_data["payment_tokens"]:
        await send_message_that_payment_method_is_not_supported(
            update, context, product["payment_method"]
        )
        return

    if product["payment_method"] == "telegram_payments":
        await send_telegram_payment_invoice(update, context, product)
    elif product["payment_method"] == "wallet_pay":
        await send_wallet_pay_invoice(update, context, product)
    else:
        raise ValueError(f"Unknown payment method: {product['payment_method']}")


async def send_message_that_payment_method_is_not_supported(
    update: Update, context: ContextTypes.DEFAULT_TYPE, payment_method: str
) -> None:
    text = f"🥲 Sorry, <b>{payment_method}</b> payment method is not supported"
    await update.effective_message.reply_text(
        text=text,
        parse_mode=ParseMode.HTML,
    )


async def send_message_about_successful_payment(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    await update.effective_message.delete()  # delete message with invoice

    await update.effective_message.reply_text(
        text=f"🎉 Successful payment!",
        reply_markup=None,
        parse_mode=ParseMode.HTML,
    )


# region: telegram payments
async def send_telegram_payment_invoice(
    update: Update, context: ContextTypes.DEFAULT_TYPE, product: Dict
) -> None:
    """Send invoice with Telegram Payments. Docs: https://core.telegram.org/bots/payments"""

    text = (
        f"⚠️ It's test mode\n"
        f"You can use test card number <code>4242 4242 4242 4242</code> with any CVC and any future expiration date for testing"
    )
    await update.effective_message.reply_text(
        text=text,
        parse_mode=ParseMode.HTML,
    )

    # telegram invoices don't support html, so let's remove html tags from title and description
    title = remove_html_tags(product["title"])
    description = remove_html_tags(product["description"])

    await update.effective_message.reply_invoice(
        title=title,
        description=description,
        currency=product["currency"],
        prices=[LabeledPrice(title, int(product["price"] * 100))],
        provider_token=context.bot_data["payment_tokens"]["telegram_payments"],
        payload="some_payload_could_be_here",
    )


async def telegram_payment_pre_checkout(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    await update.pre_checkout_query.answer(ok=True)


async def successful_telegram_payment(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    await send_message_about_successful_payment(update, context)


# endregion: telegram payments


# region: wallet pay
async def send_wallet_pay_invoice(
    update: Update, context: ContextTypes.DEFAULT_TYPE, product: Dict
) -> None:
    """Send invoice with Wallet Pay. Docs: https://docs.wallet.tg/pay"""

    await update.effective_chat.send_action(
        ChatAction.TYPING
    )  # send typing action here, because wallet pay request could take some time

    async def create_invoice() -> Tuple[str, str]:
        url = "https://pay.wallet.tg/wpay/store-api/v1/order"

        headers = {
            "Wpay-Store-Api-Key": context.bot_data["payment_tokens"]["wallet_pay"],
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

        bot_url = f"https://t.me/{context.bot.username}"
        data = {
            "amount": {
                "amount": product["price"],
                "currencyCode": product["currency"],
            },
            "externalId": str(uuid.uuid4()),
            "customerTelegramUserId": update.effective_user.id,
            "timeoutSeconds": 3600,
            "description": product["title"],
            "returnUrl": bot_url,
            "failReturnUrl": bot_url,
            "customData": "",
        }

        async with httpx.AsyncClient() as client:
            result = await client.post(url, headers=headers, data=json.dumps(data))

        result_json = result.json()
        if result_json["status"] != "SUCCESS":
            raise Exception(
                f"Wallet Pay create invoice status != SUCCESS. Reason: {result_json['message']}"
            )

        return result_json["data"]["directPayLink"], result_json["data"]["id"]

    # create invoice
    direct_pay_link, order_id = await create_invoice()

    # send invoice
    ## remove html tags from title and description to avoid bad markup
    title = remove_html_tags(product["title"])
    description = remove_html_tags(product["description"])

    text = (
        f"<b>{title}</b> ({product['price']} {product['currency']})\n"
        f"{description}\n"
        f"\n"
        f"Tap <b>👛 Wallet Pay</b> button to pay. After you pay, tap <b>Check payment status</b> button\n"
        f"\n"
        f"⚠️ Note: there is no test mode, all payments are carried out in real assets!"
    )

    reply_markup = InlineKeyboardMarkup.from_column(
        [
            InlineKeyboardButton(
                text="👛 Wallet Pay",
                url=direct_pay_link,
            ),
            InlineKeyboardButton(
                text="Check payment status",
                callback_data=f"check_wallet_pay_payment_status|{order_id}",
            ),
        ]
    )

    await update.effective_message.reply_text(
        text=text,
        reply_markup=reply_markup,
        parse_mode=ParseMode.HTML,
    )


async def check_wallet_pay_payment_status(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    order_id = update.callback_query.data.split("|")[1]

    async def check_invoice_status() -> bool:
        url = "https://pay.wallet.tg/wpay/store-api/v1/order/preview"

        headers = {
            "Wpay-Store-Api-Key": context.bot_data["payment_tokens"]["wallet_pay"],
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

        params = {"id": order_id}

        async with httpx.AsyncClient() as client:
            result = await client.get(url, headers=headers, params=params)

        result_json = result.json()
        return result_json["data"]["status"] == "PAID"

    # check invoice status
    is_paid = await check_invoice_status()
    if is_paid:
        await update.callback_query.answer()
        await send_message_about_successful_payment(update, context)
    else:
        await update.callback_query.answer("🥲 Not paid yet")


# endregion: wallet pay


async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    error = context.error

    text = f"🥲 Some error happened...\n" f"<b>Error:</b> {error}"
    await update.effective_message.reply_text(
        text=text,
        parse_mode=ParseMode.HTML,
    )

    raise error


def run_bot(
    bot_token: str,
    telegram_payments_token: Optional[str] = None,
    wallet_pay_token: Optional[str] = None,
) -> None:
    application = (
        ApplicationBuilder()
        .token(bot_token)
        .concurrent_updates(True)
        .http_version("1.1")
        .get_updates_http_version("1.1")
        .build()
    )

    # store payment tokens in bot data
    application.bot_data["payment_tokens"] = {}

    for payment_method, payment_token in [
        ("telegram_payments", telegram_payments_token),
        ("wallet_pay", wallet_pay_token),
    ]:
        if payment_token:
            application.bot_data["payment_tokens"][payment_method] = payment_token

    # handlers
    ## /start
    application.add_handler(CommandHandler("start", start))

    ## /instruction
    application.add_handler(CommandHandler("instruction", instruction))

    ## /task
    application.add_handler(CommandHandler("task", task))

    ## /connect
    application.add_handler(CommandHandler("connect", connect))

    ## /info
    application.add_handler(CommandHandler("info", info))

    ## get data from mini app
    application.add_handler(
        MessageHandler(filters.StatusUpdate.WEB_APP_DATA, get_data_from_mini_app)
    )

    ## payment
    application.add_handler(PreCheckoutQueryHandler(telegram_payment_pre_checkout))
    application.add_handler(
        MessageHandler(filters.SUCCESSFUL_PAYMENT, successful_telegram_payment)
    )

    application.add_handler(
        CallbackQueryHandler(
            check_wallet_pay_payment_status, pattern="^check_wallet_pay_payment_status"
        )
    )

    # error handler
    application.add_error_handler(error_handler)

    # start the bot
    print("Starting the bot...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    load_dotenv()  # load variables from .env file (don't forget to fill it!)

    bot_token = os.getenv("BOT_TOKEN")
    if not bot_token:
        raise ValueError("Invalid BOT_TOKEN in .env file")

    telegram_payments_token = os.getenv("TELEGRAM_PAYMENTS_TOKEN")
    wallet_pay_token = os.getenv("WALLET_PAY_TOKEN")

    run_bot(
        bot_token=bot_token,
        telegram_payments_token=telegram_payments_token if telegram_payments_token else None,
        wallet_pay_token=wallet_pay_token if wallet_pay_token else None,
    )
