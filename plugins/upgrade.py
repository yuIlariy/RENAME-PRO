from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup, ForceReply)
from pyrogram import Client, filters

# Callback handler for upgrade button
@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot, update):
    text = """**Free Plan User**
Daily Upload limit: 2GB  
Price: 0

**🪙 Basic**  
Daily Upload limit: 20GB  
Price: Rs 49 IND / 🌎 $0.59 per Month

**⚡ Standard**  
Daily Upload limit: 50GB  
Price: Rs 99 IND / 🌎 $1.19 per Month

**💎 Pro**  
Daily Upload limit: 100GB  
Price: Rs 179 IND / 🌎 $2.16 per Month

**💰 Pay Using Crypto**  
TRC20 (USDT): `TRUfcJwrPWb3q5wbETJZDQuQY3WZQbKDGg`  
BEP20 (USDT): `0x42296c74320804b0aa210e79f476e9fd5c148661`

After payment, send a screenshot to Admin @xspes"""
    
    keybord = InlineKeyboardMarkup([
        [InlineKeyboardButton("Contact Admin", url="https://t.me/xspes")],
        [InlineKeyboardButton("Copy TRC20 Address", callback_data="copy_trc20"),
         InlineKeyboardButton("Copy BEP20 Address", callback_data="copy_bep20")],
        [InlineKeyboardButton("Cancel", callback_data="cancel")]
    ])
    
    await update.message.edit(text=text, reply_markup=keybord)

# Command handler for /upgrade
@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot, message):
    text = """**Free Plan User**
Daily Upload limit: 2GB  
Price: 0

**🪙 Basic**  
Daily Upload limit: 20GB  
Price: Rs 49 IND / 🌎 $0.59 per Month

**⚡ Standard**  
Daily Upload limit: 50GB  
Price: Rs 99 IND / 🌎 $1.19 per Month

**💎 Pro**  
Daily Upload limit: 100GB  
Price: Rs 179 IND / 🌎 $2.16 per Month

**💰 Pay Using Crypto**  
TRC20 (USDT): `TRUfcJwrPWb3q5wbETJZDQuQY3WZQbKDGg`  
BEP20 (USDT): `0x42296c74320804b0aa210e79f476e9fd5c148661`

After payment, send a screenshot to Admin☄️ @xspes"""
    
    keybord = InlineKeyboardMarkup([
        [InlineKeyboardButton("Contact Admin", url="https://t.me/xspes")],
        [InlineKeyboardButton("Copy TRC20 Address", callback_data="copy_trc20"),
         InlineKeyboardButton("Copy BEP20 Address", callback_data="copy_bep20")],
        [InlineKeyboardButton("Cancel", callback_data="cancel")]
    ])
    
    await message.reply_text(text=text, reply_markup=keybord)

# Callback handlers for address copy buttons
@Client.on_callback_query(filters.regex("copy_trc20"))
async def send_trc20(bot, update):
    await update.message.reply_text("🔗 TRC20 Address:\n`TRUfcJwrPWb3q5wbETJZDQuQY3WZQbKDGg`")

@Client.on_callback_query(filters.regex("copy_bep20"))
async def send_bep20(bot, update):
    await update.message.reply_text("🔗 BEP20 Address:\n`0x42296c74320804b0aa210e79f476e9fd5c148661`")









# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Developer @JishuDeveloper
