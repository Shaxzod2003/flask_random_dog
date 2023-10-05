from telegram import Update,ReplyKeyboardMarkup,KeyboardButton
from telegram.ext import CallbackContext
import requests


def start(update: Update,context: CallbackContext):
    welcome=ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="🦮Dog")
            ]
        ],
        resize_keyboard=True
    )
    update.message.reply_text(
        text=f"Hi, {update.effective_user.first_name}! I'm a bot that can send random dog photos.",
        reply_markup=welcome
    )

def random_dog() ->str:
    url='https://random.dog/woof.json'
    response=requests.get(url=url)
    if response.status_code==200:
        return response.json()['url']
    return 
def photo_dog(update:Update,context: CallbackContext):

    picture=random_dog()
    update.message.reply_photo(
        photo=picture

    )
