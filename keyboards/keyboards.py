from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from lexicon.lexicon_en import LEXICON_EN


sex_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text=LEXICON_EN["btn_male"],
                callback_data="btn_sex_male_pressed",
            ),
            InlineKeyboardButton(
                text=LEXICON_EN["btn_female"],
                callback_data="btn_sex_female_pressed",
            ),
        ]
    ]
)

more_info_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text=LEXICON_EN["btn_more_info"],
                callback_data="more_info_start",
            )
        ]
    ]
)


calc_result_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text=LEXICON_EN["btn_result_save"], callback_data="result_save"
            ),
            InlineKeyboardButton(
                text=LEXICON_EN["btn_result_continue"],
                callback_data="result_continue",
            ),
        ]
    ]
)


def get_more_info_pagination_kb(current_page: int) -> InlineKeyboardMarkup:
    prev_page = current_page - 1 if current_page - 1 >= 1 else 1
    next_page = current_page + 1 if current_page + 1 <= 5 else 5

    pagination_kb: InlineKeyboardMarkup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="<<",
                    callback_data=f"more_info_page_{prev_page}",
                ),
                InlineKeyboardButton(
                    text=f"{current_page}/5",
                    callback_data=f"more_info_page_{current_page}",
                ),
                InlineKeyboardButton(
                    text=">>",
                    callback_data=f"more_info_page_{next_page}",
                ),
            ]
        ]
    )
    return pagination_kb
