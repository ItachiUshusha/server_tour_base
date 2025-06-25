from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

settings = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="✅", callback_data='aply'),
        InlineKeyboardButton(text="❌", callback_data='dismiss')
    ]
]) 

dismiss = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="❌", callback_data='delete_aply')]
])

async def inline_dismiss():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text="❌", callback_data='delete_aply'))
    return keyboard.as_markup()