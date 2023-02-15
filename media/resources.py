import os

from aiogram.types import FSInputFile

from config import Config, load_config


config: Config = load_config()


def get_table_image() -> FSInputFile:
    image_path: str = config.resource_manager.get_path("table_image")
    if os.path.isfile(image_path):
        return FSInputFile(image_path)
    else:
        raise FileNotFoundError
