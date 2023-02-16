from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from lexicon.lexicon_en import LEXICON_EN


sex_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text=LEXICON_EN["btn_male"], callback_data="btn_male_pressed"
            ),
            InlineKeyboardButton(
                text=LEXICON_EN["btn_female"],
                callback_data="btn_female_pressed",
            ),
        ]
    ]
)
