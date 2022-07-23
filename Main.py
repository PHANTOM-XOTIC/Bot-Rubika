from rubika.client import Bot,clients
from random import randint
from json import loads, dumps
from requests import post,get
from pathlib import Path

# شناسه اکانتتون
bot = Bot("app_name",auth="AUTH",displayWelcome=False)

#چتی که میخواید فایل در اون آپلود بشه
target = "guid"
