from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
import tg_bot.keyboards as kb

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Это бот в котором появляются заявки на аренду комнаты.' \
    ' Нажимайте галочку если договорились с клиентом и крестик если хотите удалить') #??????


@router.callback_query(F.data == 'aply')
async def inl_aply(callback: CallbackQuery):
    original_message = callback.message.text
    await callback.answer("Вы приняли заказ!", show_alert=True)
    await callback.message.edit_text(f"✅ Вы приняли заказ:\n\n{original_message}", parse_mode='HTML', reply_markup=kb.dismiss)

