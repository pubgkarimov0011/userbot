from pyrogram import Client, filters, types,enums
import requests
import xml.etree.ElementTree as ET

api_id = 24684071 #API_ID : https://my.telegram.org/
api_hash = "4759220b41608bdc2367aab0ac678d85" #API_HASH : https://my.telegram.org/
app = Client("karimov", api_id, api_hash,parse_mode=enums.parse_mode.ParseMode.HTML)




@app.on_message(filters.channel)
async def replyComment(client, message: types.Message):
    chat_id = message.chat.id
    message_id = message.id
    try:
        msg = await app.get_discussion_message(chat_id, message_id)
        await msg.reply("9860350103801766")
    except:
        pass

app.run()

# BU KOD ORQALI BARCHA OBUNA BO'LGAN KANALLARINGIZGA COMMENT QOLDIRASIZ
# DIQQAT: FAQAT KANALDA COMMENT YOZISHGA RUXSAT BERILGAN BO'LSA
# BU KOD @iCoderNet KANALIDA @UzbProMax TOMONIDAN TARQATILDI

# MANBA: @iCoderNet
