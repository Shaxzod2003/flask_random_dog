from telegram.ext import CommandHandler, Updater,MessageHandler,Filters
import handlers
from dotenv import load_dotenv
import os
load_dotenv()
TOKEN=os.environ.get("TOKEN")

def main():
    updater=Updater(token=TOKEN)
    dp=updater.dispatcher
    dp.add_handler(CommandHandler(["start","boshlash"],handlers.start))
    dp.add_handler(handler=MessageHandler(filters=Filters.text("🦮Dog"),callback=handlers.photo_dog))


    updater.start_polling()

    updater.idle()
if __name__=="__main__":
    main()