import asyncio
import logging
import sys
import uuid
import aiohttp
from aiogram import Bot, Dispatcher, types, F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonRequestUser, KeyboardButtonRequestChat

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='User 👤', request_user=KeyboardButtonRequestUser(request_id=1, user_is_bot=False))
        ],
        [
            KeyboardButton(text='Super Group 👥', request_chat=KeyboardButtonRequestChat(request_id=2, chat_is_channel=False, chat_has_username=True, chat_is_created=False,chat_is_forum=False)),
            KeyboardButton(text='Group 👥', request_chat=KeyboardButtonRequestChat(request_id=3, chat_is_channel=False, chat_has_username=False, chat_is_created=False,chat_is_forum=False))
        ],
        [
            KeyboardButton(text='Channel 🔊', request_chat=KeyboardButtonRequestChat(request_id=4, chat_is_channel=True, chat_has_username=True, chat_is_created=False,chat_is_forum=False)),
            KeyboardButton(text='Private Channel 🔊', request_chat=KeyboardButtonRequestChat(request_id=5, chat_is_channel=True, chat_has_username=False, chat_is_created=False,chat_is_forum=False))
        ],
        [
            KeyboardButton(text='Bot 🤖', request_user=KeyboardButtonRequestUser(request_id=6, user_is_bot=True)),
            KeyboardButton(text='Premium 🌟', request_user=KeyboardButtonRequestUser(request_id=7, user_is_bot=False, user_is_premium=True))
        ],
    ],
    resize_keyboard=True
)

TOKEN = "6589406008:AAEx-FiRsycRuvezWc-wRgYlFj05ErrpQ48"

dp = Dispatcher()
bot = Bot(TOKEN, parse_mode=ParseMode.HTML)

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    username = f"@{message.from_user.username}"
    if username == '@None': username = ""
    await message.answer(f"""{username}
Id: {message.from_user.id}
First: {message.from_user.first_name}
Lang: {message.from_user.language_code}""", reply_markup=menu)


@dp.message(F.user_shared)
async def on_user_shared(message: types.Message):
    await message.answer(
        f"User id:  <code>{message.user_shared.user_id}</code>"
    )


@dp.message(F.chat_shared)
async def on_user_shared(message: types.Message):
    await message.answer(
        f"User id:  <code>{message.chat_shared.chat_id}</code>",
        
    )

@dp.message(F.text)
async def command_start_handler(message: Message) -> None:
    username = f"@{message.from_user.username}"
    if username == '@None': username = ""
    await message.answer(f"""{username}
Id: {message.from_user.id}
First: {message.from_user.first_name}
Lang: {message.from_user.language_code}""", reply_markup=menu)

async def main():
    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    finally:
        await bot.session.close()



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())