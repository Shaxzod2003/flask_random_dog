from flask import Flask,request
from telegram import Update, Bot
from telegram.ext import CommandHandler,MessageHandler,Dispatcher,Filters
import handlers
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN=os.environ.get("TOKEN")
bot=Bot(token=TOKEN)
dp=Dispatcher(bot, None, workers=0)


app=Flask(__name__)
@app.route("/webhook",methods=["GET","POST"])
def main():
    if request.method=="GET":
        return "runing"
    if request.method=="POST":
        body=request.get_json()
        update=Update.de_json(body,bot)
        dp.add_handler(CommandHandler(["start", "boshlash"],handlers.start))
        dp.add_handler(MessageHandler(filters=Filters.text("🦮Dog"),callback=handlers.photo_dog))
        dp.process_update(update)

        return {"message","ok"}
    
if __name__=="__main__":
    app.run(debug=True)
    
    