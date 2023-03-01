from aiogram import Bot, F, Router
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from errors import errors
from filters.pagination import MoreInfoPaginator
from lexicon.lexicon_en import LEXICON_EN
from media.resources import get_table_image
from models.dao import UserDataAccessObject
from models.models import TestResult
from keyboards.keyboards import (
    sex_keyboard,
    more_info_keyboard,
    get_more_info_pagination_kb,
    calc_result_keyboard,
)
from models.validators import (
    validate_repetitions,
    validate_seconds,
    validate_milliseconds,
)
from states.states import FSMStart, TestResultForm


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


@router.message(Command(commands=["info"]))
async def process_info_command(message: Message):
    """Sends info about FBI PFT test with a button 'More info'."""
    await message.answer(LEXICON_EN["/info"], reply_markup=more_info_keyboard)


@router.callback_query(MoreInfoPaginator())
async def process_more_info(callback: CallbackQuery, page_num: int):
    await callback.answer()
    send_method = callback.message.edit_text

    if callback.data == "more_info_start":
        await callback.message.answer(text=LEXICON_EN["more_info_header"])
        send_method = callback.message.answer

    keyboard = get_more_info_pagination_kb(page_num)
    try:
        await send_method(
            text=LEXICON_EN[f"more_info_page_{page_num}"],
            reply_markup=keyboard,
        )
    except TelegramBadRequest as error:
        if not error.message.startswith("Bad Request: message is not modif"):
            raise


@router.message(Command(commands=["calc"]))
async def process_calc_command(message: Message, state: FSMContext):
    await message.answer(
        text=LEXICON_EN["test_result_form_header"]
        + "\n\n"
        + LEXICON_EN["test_result_form_situps"]
    )
    await state.set_state(TestResultForm.situps)


@router.message(TestResultForm.situps)
async def process_situps(message: Message, state: FSMContext) -> None:
    situps = validate_repetitions(message.text)
    if isinstance(situps, int):
        await state.update_data(situps=situps)
        await state.set_state(TestResultForm.sprint)
        await message.answer(text=LEXICON_EN["test_result_form_sprint"])
    else:
        await message.answer(text=situps)


@router.message(TestResultForm.sprint)
async def process_sprint(message: Message, state: FSMContext) -> None:
    sprint = validate_milliseconds(message.text)
    if isinstance(sprint, int):
        await state.update_data(sprint=sprint)
        await state.set_state(TestResultForm.pushups)
        await message.answer(text=LEXICON_EN["test_result_form_pushups"])
    else:
        await message.answer(text=sprint)


@router.message(TestResultForm.pushups)
async def process_pushups(message: Message, state: FSMContext) -> None:
    pushups = validate_repetitions(message.text)
    if isinstance(pushups, int):
        await state.update_data(pushups=pushups)
        await state.set_state(TestResultForm.running)
        await message.answer(text=LEXICON_EN["test_result_form_running"])
    else:
        await message.answer(text=pushups)


@router.message(TestResultForm.running)
async def process_running(message: Message, state: FSMContext) -> None:
    running = validate_seconds(message.text)
    if isinstance(running, int):
        await state.update_data(running=running)
        await state.set_state(TestResultForm.pullups)
        await message.answer(text=LEXICON_EN["test_result_form_pullups"])
    else:
        await message.answer(text=running)


@router.message(TestResultForm.pullups)
async def process_pullups(message: Message, state: FSMContext) -> None:
    pullups = validate_repetitions(message.text)
    if isinstance(pullups, int):
        await state.update_data(pullups=pullups)
        data = await state.get_data()
        await state.set_state(TestResultForm.save_continue)
        test_result = TestResult(**data)
        user = await UserDataAccessObject.get(message.from_user.id)
        test_result.calculate(sex=user.sex)
        await message.answer(
            text=str(test_result), reply_markup=calc_result_keyboard
        )
    else:
        await message.answer(text=pullups)


@router.callback_query(
    F.data == "result_save", StateFilter(TestResultForm.save_continue)
)
async def process_save_result_buttons_press(
    callback: CallbackQuery, state: FSMContext
):
    await callback.answer()

    data = await state.get_data()
    test_result = TestResult(**data)
    user = await UserDataAccessObject.get(callback.from_user.id)
    test_result.calculate(sex=user.sex)
    user.results.append(test_result)
    await UserDataAccessObject.update(user)

    await state.clear()
    await callback.message.answer(text=LEXICON_EN["result_saved"])


@router.callback_query(
    F.data == "result_continue", StateFilter(TestResultForm.save_continue)
)
async def process_continue_result_buttons_press(
    callback: CallbackQuery, state: FSMContext
):
    await callback.answer(text=LEXICON_EN["continue_pressed"])
    await state.clear()


@router.message(TestResultForm.save_continue)
async def process_save_continue_warning(message: Message, state: FSMContext):
    await message.answer(
        LEXICON_EN["result_save_continue_warning"],
        reply_markup=calc_result_keyboard,
    )
