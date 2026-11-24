import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart, Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo, MenuButtonWebApp

# 1. Вставь сюда токен своего бота от @BotFather
BOT_TOKEN = "9029959011:AAFs5Db9LknGxkr4mDWD6Yw-tzIDyQBp1xo"

# 2. Вставь сюда HTTPS-ссылку на загруженный сайт (например, с GitHub Pages или Vercel)
WEBAPP_URL = "https://bzbulik.github.io/minemaze/"


logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


def get_game_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="⛏️ Играть в MineMaze 3D",
                    web_app=WebAppInfo(url=WEBAPP_URL)
                )
            ]
        ]
    )


@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    user_name = message.from_user.first_name or "Игрок"
    await message.answer(
        f"Привет, <b>{user_name}</b>! 👋\n\n"
        "Добро пожаловать в <b>MineMaze 3D: Echoes in the Mist</b>!\n"
        "• Ориентируйся в 3D-лабиринте по громкости музыки и туману 🎵\n"
        "• Исследуй 3 мира: Руины, Новогоднюю комнату и Джунгли 🎄🌴\n"
        "• Собирай монеты и открывай скины в магазине 🪙\n\n"
        "Нажми на кнопку ниже, чтобы начать:",
        reply_markup=get_game_keyboard(),
        parse_mode="HTML"
    )


@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.answer(
        "<b>Как играть:</b>\n"
        "1. Чем ближе ты к синему маяку выхода, тем тише туман и громче музыка.\n"
        "2. Управляй персонажем с помощью стрелок на экране, свайпов или клавиатуры.\n"
        "3. Весь прогресс и купленные скины сохраняются автоматически!",
        reply_markup=get_game_keyboard(),
        parse_mode="HTML"
    )


async def on_startup():
    # Устанавливаем кнопку запуска игры прямо в меню возле поля ввода
    try:
        await bot.set_chat_menu_button(
            menu_button=MenuButtonWebApp(
                text="Играть",
                web_app=WebAppInfo(url=WEBAPP_URL)
            )
        )
    except Exception as e:
        logging.warning(f"Не удалось обновить кнопку меню: {e}")


async def main():
    #await on_startup()
    print("Бот успешно запущен! Напиши /start своему боту в Telegram.")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
