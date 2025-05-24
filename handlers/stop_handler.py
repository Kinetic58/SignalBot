from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext

from handlers.start_handler import SessionState

router = Router()

@router.message(F.text == "СТОП")
async def stop_session(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        "Надеюсь ваша торговая сессия прошла успешно ☑️",
        reply_markup=ReplyKeyboardRemove()
    )
