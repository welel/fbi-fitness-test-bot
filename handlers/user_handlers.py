from aiogram import Bot, F, Router, Dispatcher
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from errors import errors
from lexicon.lexicon_en import LEXICON_EN
from media.resources import get_table_image
from models.dao import UserDataAccessObject
from keyboards.keyboards import sex_keyboard
from states.states import FSMStart


router: Router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message, state: FSMContext):
    """Sends start informations about the bot."""
    user_id = message.from_user.id
    try:
        await UserDataAccessObject.get(user_id)
        await message.answer(LEXICON_EN["start_warning"])
    except errors.UserDoesNotExists:
        await message.answer(
            text=LEXICON_EN["/start"], reply_markup=sex_keyboard
        )
        await state.set_state(FSMStart.fill_sex)
        print(state)


@router.callback_query(FSMStart.fill_sex, F.data.startswith("btn_sex"))
async def process_sex_buttons_press(
    callback: CallbackQuery, state: FSMContext
):
    sex = "male" if callback.data == "btn_sex_male_pressed" else "female"
    await UserDataAccessObject.create(id=callback.from_user.id, sex=sex)
    await state.clear()
    await callback.answer()
    await callback.message.answer(text=LEXICON_EN["registered"])


@router.callback_query(F.data.startswith("btn_sex"))
async def process_sex_buttons_press_without_state(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer(text=LEXICON_EN["sex_pressed_warning"])


@router.message(FSMStart.fill_sex)
async def warning_not_sex(message: Message, state: FSMContext):
    await message.answer(LEXICON_EN["sex_warning"], reply_markup=sex_keyboard)


@router.message(Command(commands=["table"]))
async def process_table_command(message: Message, bot: Bot):
    """Sends a scoring table image."""
    await message.answer(LEXICON_EN["table_caption"])
    await bot.send_photo(message.chat.id, get_table_image())
