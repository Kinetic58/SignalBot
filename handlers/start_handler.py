import random

from aiogram import Router, F
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from asyncio import sleep
from function.signal_generator import generate_signal

router = Router()

class SessionState(StatesGroup):
    active = State()

stop_button = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="СТОП")]],
    resize_keyboard=True
)

@router.message(F.text == "/start")
async def start_session(message: Message, state: FSMContext):
    await message.answer("Ищем точку входа , приготовьтесь…. 🔍", reply_markup=stop_button)
    await state.set_state(SessionState.active)

    while True:
        current_state = await state.get_state()
        if current_state != SessionState.active.state:
            break
        await sleep(random.randint(300, 420))
        await message.answer(generate_signal())
