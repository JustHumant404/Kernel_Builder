from telegram import Update, InputFile
from telegram.ext import Application, CommandHandler, ContextTypes
import os

# Replace with your bot token
TOKEN = "7570438190:AAHWWqbu68ceMmpxpb4yRgR_u_Z1Mfl3aj4" 

async def send_document_with_caption(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = "-1002788524849/2"
    
    # Path to your file
    file_path = sys.argv[1:]
    
    # Ensure the file exists
    if not os.path.exists(file_path):
        await context.bot.send_message(chat_id=chat_id, text="File not found!")
        return

    # Open the file in binary read mode
    with open(file_path, 'rb') as document_file:
        # MarkdownV2 formatted caption
        caption = "*This is a bold caption* with _italic text_ and `inline code`."
        
        await context.bot.send_document(
            chat_id=chat_id,
            document=InputFile(document_file),
            caption=caption,
            parse_mode='MarkdownV2'
        )

def main():
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("sendfile", send_document_with_caption))

    application.run_polling()

if __name__ == "__main__":
    main()
