from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup


class FSMStart(StatesGroup):
    fill_sex = State()


class TestResultForm(StatesGroup):
    situps = State()
    sprint = State()
    pushups = State()
    running = State()
    pullups = State()
    save_continue = State()
