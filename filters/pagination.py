from aiogram.filters import BaseFilter
from aiogram.types import CallbackQuery


class MoreInfoPaginator(BaseFilter):
    async def __call__(self, callback: CallbackQuery) -> bool | dict[str, int]:
        if callback.data.startswith("more_info_page_"):
            page_num = int(callback.data.strip("more_info_page_"))
            return {"page_num": page_num}
        elif callback.data == "more_info_start":
            return {"page_num": 1}
        else:
            return False
