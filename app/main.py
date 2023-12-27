import os
from typing import Final
from bot.ChatBotController import ChatBotController

BOT_TOKEN: Final = os.environ["token"]
BOT_USERNAME: Final = os.environ["BOT_USERNAME"]

if __name__ == '__main__':
    chat_bot = ChatBotController(BOT_TOKEN, BOT_USERNAME)



