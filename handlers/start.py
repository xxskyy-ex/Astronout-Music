from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_USERNAME
from config import START_IMG as banner


@Client.on_message(filters.command(["start", "start@GroupMusicPlayBot"]) & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        text="**Hello ðð» {}!**\n\nI **Can Play Music In Voice Chats of Telegram Groups.**I Have A **lot of cool feature that will amaze You!**\n\n**Click /cmdlist For More Help On My Usage â¤**".format(message.from_user.mention),
        reply_markup=InlineKeyboardMarkup(
            [[
            InlineKeyboardButton("â Add To Your Group â", url="https://t.me/astronoutmusicBot?startgroup=true")
            ],[
            InlineKeyboardButton("ð¬ Group Chat", url="https://t.me/virtuallbullshit"),
            InlineKeyboardButton("Support Channel ð", url="https://t.me/astronoutupdate")
            ],[
            InlineKeyboardButton("Commands ð ", url="https://telegra.ph/Music-Bot-05-07")
            ],[
            InlineKeyboardButton("Managed Byð", url="https://t.me/sokapgblg")
            ]]

        ),
        disable_web_page_preview=True
    )
        
@Client.on_message(filters.command(["start", "start@GroupMusicPlayBot"]) & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
    await message.reply_text(
        text="**Music Bot Is Online â**",
        reply_markup=InlineKeyboardMarkup(
            [[
            InlineKeyboardButton(text="ðï¸ Support Group ðï¸", url="https://t.me/MusicBotSupports")
            ]]
        )
    )


@Client.on_message(filters.command(["cmdlist", "start@astronoutmusicbot"]) & filters.private & ~filters.channel)
async def cmdlist(_, message: Message):
    await message.reply_text(
        text="""**Group Music Bot : Help Menu**

__Ã First Add Me To Your Group..
Ã Promote Me As Admin In Your Group With All Permission..__

**ð· Common Commands.**

â¢ `/play` - Song Name : __Plays Via Youtube__
â¢ `/dplay` - Song Name : __Play Via Deezer__
â¢ `/splay` - Song Name : __Play Via Jio Saavn__
â¢ `/playlist` - __Show now playing list__
â¢ `/current` - __Show now playing__

â¢ `/song` - Song Name : __Get The Song From YouTube__
â¢ `/vid` - Video Name : __Get The Video From YouTube__
â¢ `/deezer` - song name : __download songs you want quickly via deezer__
â¢ `/saavn` - song name : __download songs you want quickly via saavn__
â¢ `/search` - YouTube Title : __(Get YouTube Search Query)__

**ð· Group Admin Commands.**

â¢ `/skip` : __Skips Music__
â¢ `/pause` : __Pause Playing Music__
â¢ `/resume` : __Resume Playing Music__
â¢ `/end` : __Stops playing Music__
â¢ `/reload` : __Reloads Admin List__
â¢ `/userbotjoin` : __Assistant Joins The Group__
â¢ `/userbotleave` : __Assistant Leaves From The Group.__""",
        reply_markup=InlineKeyboardMarkup(
              [[
              InlineKeyboardButton(text="ðï¸ Support Group ðï¸", url="https://t.me/astronoutupdate")
              ]]
          )
      )
