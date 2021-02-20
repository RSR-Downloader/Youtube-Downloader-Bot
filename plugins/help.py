from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"Aw le! Youtube Video Mp3/Mp4 engpawh ka download theia, Mahse, Playlists a theih loh thung. Youtube URL Link lo thawn tawp la aw. Chuan Mp3/Mp4 i duh ilo thlang mai ang,chuan i awmna group ah min add a,admin a min dah bawk chuan group ah pawh hna ka thawk thei e,min add dan tur chu i group Add member tih ah khan kal la,mami4_bot ti in search la,ka lo lang anga min add mai dawn nia. Hriatthiam loh i neih chuan tah hian min lo be dawn nia @rsrmusic"
    await message.reply_text(helptxt)
