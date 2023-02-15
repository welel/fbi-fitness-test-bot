from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from lexicon.lexicon_en import LEXICON_EN
from media.resources import get_table_image


router: Router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    """Sends start informations about the bot."""
    await message.answer(text=LEXICON_EN["/start"])


@router.message(Command(commands=["table"]))
async def process_start_command(message: Message):
    image_file = get_table_image()
    print(image_file)
    await message.answer(LEXICON_EN["table_caption"])
    # await message.send_photo(message.chat.id, image_file)
