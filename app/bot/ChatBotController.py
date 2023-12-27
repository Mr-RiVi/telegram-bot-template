from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes


class ChatBotController:
    def __init__(self, bot_token, bot_username):
        print("starting bot........")
        app = Application.builder().token(bot_token).build()

        # Commands handle
        app.add_handler(CommandHandler('start', self.start_command))

        # Messages handle
        app.add_handler(MessageHandler(filters.TEXT, self.handle_message))

        # Error handle
        app.add_error_handler(self.error_handler)

        # Check updates constantly
        print("Polling......")
        app.run_polling(poll_interval=3)

    # Commands
    async def start_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("Hello User")

    # Responses handler
    def handle_response(self, text: str) -> str:
        processed: str = text.lower()

        if 'hello' in processed:
            return 'hey there!'

        if 'how are u' in processed:
            return 'Im good'

        return 'i cant understand sorry'

    async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        # Retrieving chat information and message content
        username: str = update.message.chat.username
        first_name: str = update.message.chat.first_name
        last_name: str = update.message.chat.last_name
        chat_id: str = update.message.chat.id
        chat_type: str = update.message.chat.type
        message: str = update.message.text

        print(f'User ({chat_id}) {first_name} in {chat_type}: "{message}"')

        # Check whether this message comes from a group chat or private chat
        # If the message is from a group chat
        if chat_type == 'group':
            # Check if the bot's username is mentioned in the message
            if self.bot_username in message:
                # Process the message by removing the bot's username and leading/trailing spaces
                processed_message: str = message.replace(self.bot_username, '').strip()

                # Generate a response based on the processed message
                response: str = self.handle_response(processed_message)
            # If the bot's username is not mentioned in the message, do not respond
            else:
                return
        # If the message is from a private chat
        else:
            # Generate a response based on the original message
            response: str = self.handle_response(message)

        # Print the bot's response
        print('Bot:', response)

        # Sending the generated response as a reply to the chat.
        await update.message.reply_text(response)

    def error_handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        print(f'Update {update} caused error {context.error}')
