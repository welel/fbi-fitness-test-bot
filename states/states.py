from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup


class FSMStart(StatesGroup):
    fill_sex = State()
