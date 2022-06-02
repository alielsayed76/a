import asyncio
import os
import time
import pyrogram
from cache.admins import admins
from pyrogram import Client, filters
from config import IMG_3, UPDATES_CHANNEL, OWNER_NAME, SUDO_USERS, BOT_USERNAME, ALIVE_NAME, BOT_NAME
from driver.filters import command, other_filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message


@Client.on_message(command(["لإعدادات", "لاعدادات", "عدادات", "م", f"nftb@{BOT_USERNAME}"]) & other_filters)
async def nftb(client: Client, message: Message):
    await message.reply_photo(
        photo=f"{IMG_3}",
        caption=f"""🌀 ها هي اوامر الاغاني :
━━━━━━━━━━━━
⇦اوامر تشغيل البوت في المجموعات⇨
⇦ ✪『 `تشغيل` 』✪➢ ➕ 「اسم الأغنية او / رابط」تشغيل الصوت mp3
⇦ ✪『 `فيديو` 』✪➢ ➕ 「اسم الفديو او / رابط الفيديو」 تشغيل الفيديو داخل المكالمة 
⇦ ✪『 `ايقاف او انهاء`』✪➢ ☆ لايقاف التشغيل
⇦ ✪『 `وقف` 』✪➢ ☆ ايقاف التشغيل موقتآ 
⇦ ✪『 `تقدم` 』✪➢ ☆ تخطي الئ التالي
⇦ ✪『 `مواصله` 』✪➢ ☆ استئناف التشغيل 
⇦ ✪『 `ميوت` 』✪➢ ☆ لكتم البوت
⇦ ✪『 `الغاء الكتم`』✪➢ ☆ لرفع كتم البوت
━━━━━━━━━━━━
⇦اوامر التحكم بلبوت خارج وداخل المجموعات⇨
⇦ ✪『 `تحكم` 』✪➢ ☆ ↤ تظهر لك قائمة التشغيل
⇦ ✪『 `بحث` 』✪➢ ➕ «اي شيء تريد البحث عنه بليوتيوب»
⇦ ✪『 `الصوت` 』✪➢ ➕ «كتابه» الرقم لضبط مستوئ الصوت
⇦ ✪『 `تحديث` 』✪➢ ☆ لتحديث البوت و قائمة المشرفين
⇦ ✪『 `انضم` 』✪➢ ☆ لاستدعاء حساب المساعد
⇦ ✪『 `مغادرة` 』✪➢ ☆ لطرد حساب المساعد 
━━━━━━━━━━━━
⇦اوامر تحكم المطور⇨
⇦ ✪『 `مسح` 』✪➢ ☆ لمسح جميع الملفات المستخدمه
⇦ ✪『 `معلومات`  』✪➢ ☆ لرؤيه معلومات النظام 
━━━━━━━━━━━━━━
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("𝐒𝐎𝐔𝐑𝐂𝐄🌀", url=f"https://t.me/{UPDATES_CHANNEL}"),
                ],
                [ 
                 InlineKeyboardButton(
                     ALIVE_NAME, url=f"https://t.me/{OWNER_NAME}"), 
                ],
            ]
        ),
    )
    
    
@Client.on_message(command(["يدي", f"ids@{BOT_USERNAME}"]) & other_filters)
def ids(client: Client, message: Message):
    ali = message.reply_to_message
    if ali:
        message.reply_text(
            f"اسمه 🤓: {message.from_user.mention()}\nايديه ☺️: `{message.from_user.id}`\nيوزره 🌚🙈: @{message.from_user.username}")
    else:
        message.reply(
            f"اسمك 🤓❤️: {message.from_user.mention()}\nايديك ☺️: `{message.from_user.id}`\nيوزرك 🌚🙈: @{message.from_user.username}"
        )


@Client.on_message(command([".", f"vgdg@{BOT_USERNAME}"]) & other_filters)
async def vgdg(client: Client, message: Message):
    await message.reply(
        f""" صلي علي الحبيب ❤️ """
        )


@Client.on_message(command(["جلي", f"nftbs@{BOT_USERNAME}"]) & other_filters)
async def nftbs(client: Client, message: Message):
    await message.reply(
        f"""تتشل يبعيد 😹😹
        """)

    
@Client.on_message(command(["نا مين", f"gghpb@{BOT_USERNAME}"]) & other_filters)
async def gghpb(client: Client, message: Message):
    await message.reply_text(
        f"""💘 ¦ انت روحي » """, 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "انت روح قلبي🐣💘", url=f"tg://settings")
                ]
            ]
        ),
    )
    
    
@Client.on_message(command(["حبك", "بق", "بكك", "حبق", "بقق", "حبكك", f"nftbsa@{BOT_USERNAME}"]) & other_filters)
async def nftbsa(client: Client, message: Message):
    await message.reply(
        f"""{message.from_user.mention()}بموت فيك يروح قلبي 🥺❤️
        """)
    
    
@Client.on_message(command(["ول", f"echo@{BOT_USERNAME}"]) & other_filters)
def echo(client, msg):
    text = msg.text.split(None, 1)[1]
    msg.reply(text)
    
    
@Client.on_message(command(["لمطور", f"motawerf@{BOT_USERNAME}"]) & other_filters)
async def motawerf(client: Client, message: Message):
    await message.reply(
        f"""مطوري الغالي حبيب قلبي 🥺❤️""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "مطوري 🌚❤️", url=f"https://t.me/{OWNER_NAME}")
                ],
                [InlineKeyboardButton("🎧اضافه البوت اللي مجموعتك🎧", url=f"http://t.me/{BOT_USERNAME}?startgroup=new"),              
                ]
            ]
        ),
    )


@Client.on_message(command(["تبتي", f"motaweryj@{BOT_USERNAME}"]) & filters.user(5369052737))
async def motaweryj(client: Client, message: Message):
    await message.reply(
        f"""انت مبرمج السورس حبيب قلبي 🌚🙈""")


@Client.on_message(command(["تبتي", f"motawer@{BOT_USERNAME}"]) & filters.user(5002164804))
async def motawer(client: Client, message: Message):
    await message.reply(
        f"""مبرمج السورس حبيب قلبي 🌚🙈""")


@Client.on_message(command(["وت", f"gghhpbhab@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
async def gghpbhab(client: Client, message: Message):
    await message.reply_text(
        f"""اسمي """, {BOT_NAME}, """يروحي 🌚❤️""", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        ALIVE_NAME, url=f"https://t.me/{OWNER_NAME}")
                ],[
                    InlineKeyboardButton(
                        BOT_NAME, url=f"https://t.me/{BOT_USERNAME}")
                ]
            ]
        ),
    )


@Client.on_message(command(["لي", f"motaweraw@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
async def motaweraw(client: Client, message: Message):
    await message.reply_photo(
        photo = "https://telegra.ph/file/f7a8e5469df132cf1d5c1.jpg",
       caption =f"""مبرمج السورس حبيب قلبي 🌚🙈""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ꞏ𝘿𝙀𝙑 𝘼𝙇𝙄 ｢♥｣", url=f"https://t.me/EL_RAYEQ")
                ],[
                    InlineKeyboardButton(
                        "𝐒𝐎𝐔𝐑𝐂𝐄🌀", url=f"https://t.me/{UPDATES_CHANNEL}")
                ]
            ]
    ))
                
                
@Client.on_message(command(["سن", f"motawerat@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
async def motawerat(client: Client, message: Message):
    await message.reply_photo(
        photo = "https://telegra.ph/file/7dd0f2755c4bb2ed05b15.jpg",
        caption =f"""مبرمج السورس حبيب قلبي 🌚🙈""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ꞏ𝘿𝙀𝙑 𝘼𝙍𝘽𝘼𝙒𝙔 ｢♥｣", url=f"https://t.me/Dev_Arbawy")
                ],[
                    InlineKeyboardButton(
                        "𝐒𝐎𝐔𝐑𝐂𝐄🌀", url=f"https://t.me/{UPDATES_CHANNEL}")
                ]
            ]
    ))

    
@Client.on_message(command(["ين ضافني", f"nftbst@{BOT_USERNAME}"]) & other_filters)
async def nftbst(client: Client, message: Message):
    await message.reply(
        f"""انت دخلت بالرابط متعملش نفسك غبي 😒""")
    
    
@Client.on_message(command(["😹😹", f"nftbsta@{BOT_USERNAME}"]) & other_filters)
async def nftbsta(client: Client, message: Message):
    await message.reply(
        f"""ضحكتك عسل زيك ياروحي 🌚❤️""")
    
    
