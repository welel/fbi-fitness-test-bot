from dataclasses import dataclass
import os
from pathlib import Path

from dotenv import load_dotenv

from errors.errors import ImproperlyConfigured, NoSuchResource


def get_env_variable(var_name: str) -> str:
    """Get an environment variable or raise an exception.

    Args:
        var_name: a name of a environment variable.

    Returns:
        A value of the environment variable.

    Raises:
        ImproperlyConfigured: if the environment variable is not set.
    """
    try:
        return os.environ[var_name]
    except KeyError:
        raise ImproperlyConfigured(var_name)


@dataclass
class ResourceManager:
    RESOURCES_PATH: str
    resources: dict[str, str]

    def get_path(self, resource_name: str) -> str:
        try:
            return os.path.join(
                self.RESOURCES_PATH, self.resources[resource_name]
            )
        except KeyError:
            raise NoSuchResource(resource_name)


@dataclass
class TelegramBot:
    token: str


@dataclass
class Config:
    tg_bot: TelegramBot
    resource_manager: ResourceManager


def load_config() -> Config:
    # Parse a `.env` file and load the variables into environment valriables
    load_dotenv()

    # Common configuration
    BASE_DIR: str = Path(__file__).resolve().parent.parent

    # Telegram bot configuration
    token: str = get_env_variable("BOT_TOKEN")
    tg_bot: TelegramBot = TelegramBot(token=token)

    # Resource manager configuration
    RESOURCES_PATH: str = os.path.join("resources/")
    resources: dict[str, str] = {"table_image": "fitness_test_table.png"}
    resources_manager: ResourceManager = ResourceManager(
        RESOURCES_PATH=RESOURCES_PATH, resources=resources
    )

    return Config(tg_bot=tg_bot, resource_manager=resources_manager)
