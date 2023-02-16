from aiogram import Bot, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from lexicon.lexicon_en import LEXICON_EN
from media.resources import get_table_image
from keyboards.keyboards import sex_keyboard


router: Router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    """Sends start informations about the bot."""
    await message.answer(text=LEXICON_EN["/start"], reply_markup=sex_keyboard)


@router.message(Command(commands=["table"]))
async def process_start_command(message: Message, bot: Bot):
    """Sends a scoring table image."""
    await message.answer(LEXICON_EN["table_caption"])
    await bot.send_photo(message.chat.id, get_table_image())
