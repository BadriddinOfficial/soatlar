from pyrogram import Client, Filters
from pyrogram.api import functions
import datetime
import time
import pytz
api_id = 18977021 #my.telegram.org dan olgan apiidni qoying
api_hash = "668c3af8ca3689e5720b7c15f4b99894" #my.telegram.org dan olgan apihash ni qoying
app = Client("my_account",api_id,api_hash)
app.start()
while True:
    ok = pytz.timezone("Asia/Tashkent")
    x = datetime.datetime.now(tz=ok)
    x = x.strftime("%H:%M")
    app.send(functions.account.UpdateProfile(
    first_name=str(x),
    about="Meni bilgan biladi, Bilmagan o'zi biladi👌😏➢ " +str(x)
    ))
    time.sleep(30)
