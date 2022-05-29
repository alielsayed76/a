from cache.admins import admins
from pyrogram import Client, filters
from config import  IMG_3, UPDATES_CHANNEL, OWNER_NAME
from time import time
from driver.filters import command, other_filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

@Client.on_message(command(["لاوامر", "وامر", "لاوامر", "م"]) & other_filters)
async def nftb(client: Client, message: Message):
    await message.reply_photo(
        photo=f"{IMG_3}",
        caption=f"""🌀 ها هي اوامر البوت :
━━━━━━━━━━━━
⇦اوامر تشغيل البوت في المجموعات⇨
⇦ ✪『 تشغيل 』✪➢ ➕ 「اسم الأغنية او / رابط」تشغيل الصوت mp3
⇦ ✪『 فيديو 』✪➢ ➕ 「اسم الفديو او / رابط الفيديو」 تشغيل الفيديو داخل المكالمة 
⇦ ✪『 ايقاف او انهاء』✪➢ ☆ لايقاف التشغيل
⇦ ✪『 وقف 』✪➢ ☆ ايقاف التشغيل موقتآ 
⇦ ✪『 تقدم 』✪➢ ☆ تخطي الئ التالي
⇦ ✪『 مواصله 』✪➢ ☆ استئناف التشغيل 
⇦ ✪『 ميوت 』✪➢ ☆ لكتم البوت
⇦ ✪『 الغاء الكتم』✪➢ ☆ لرفع كتم البوت
━━━━━━━━━━━━
⇦اوامر التحكم بلبوت خارج وداخل المجموعات⇨
⇦ ✪『 تحكم 』✪➢ ☆ ↤ تظهر لك قائمة التشغيل
⇦ ✪『 بحث 』✪➢ ➕ «اي شيء تريد البحث عنه بليوتيوب»
⇦ ✪『 الصوت 』✪➢ ➕ «كتابه» الرقم لضبط مستوئ الصوت
⇦ ✪『 تحديث 』✪➢ ☆ لتحديث البوت و قائمة المشرفين
⇦ ✪『 انضم 』✪➢ ☆ لاستدعاء حساب المساعد
⇦ ✪『 مغادرة 』✪➢ ☆ لطرد حساب المساعد 
━━━━━━━━━━━━
⇦اوامر تحكم المطور⇨
⇦ ✪『 مسح 』✪➢ ☆ لمسح جميع الملفات المستخدمه
⇦ ✪『 معلومات  』✪➢ ☆ لرؤيه معلومات النظام 
⇦ ✪『 ترقيه 』✪➢ ☆ لترقيه البوت لاخر اصدار من السورس
━━━━━━━━━━━━━━
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("𝐒𝐎𝐔𝐑𝐂𝐄🌀", url=f"https://t.me/{UPDATES_CHANNEL}"),
                ],
                [
                InlineKeyboardButton("Programmer", url=f"https://t.me/{OWNER_NAME}"),
                ],
            ]
        ),
    )
    
    

