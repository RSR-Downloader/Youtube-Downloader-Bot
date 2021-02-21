from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"Hello,kei hi YouTube ami video emaw mp3 a download a thawn thei tu ka ni a,YouTube a i download duh kha a link min lo thawn la,ka lo download sak che anga ka rawn thawn leh ang che,tin..Group ah ka hman theih bawk a,mp3 leh video in pek tawn na group vel ah ka tangkai ang,link hi click la i awmma group ah min add anga,admin ah min dah dawn nia  https://telegram.me/miss_mami_bot?startgroup=chat  Hriatthiam loh i neih chuan tah hian min lo be dawn nia,ani hi min siamtu ani e😊👇   @rsrmusic"
    await message.reply_text(helptxt)
