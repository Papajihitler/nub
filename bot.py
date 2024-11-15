import requests
import telebot, time
from telebot import types
from gatet import Tele
import os

token = '7225088009:AAGWVDnAiiBhZd3AsZhkPvHK2C3kLmqHEQ0'
bot = telebot.TeleBot(token, parse_mode="HTML")

access_list = {'7190939599': True}

@bot.message_handler(commands=["grant"])
def grant_access(message):
    if str(message.chat.id) == '7190939599':
        try:
            chat_id = message.text.split()[1]
            access_list[chat_id] = True
            bot.reply_to(message, f"Access granted to user {chat_id}.")
        except IndexError:
            bot.reply_to(message, "Please provide a chat ID to grant access.")
    else:
        bot.reply_to(message, "You are not authorized to use this command.")


@bot.message_handler(commands=["revoke"])
def revoke_access(message):
    if str(message.chat.id) == '7190939599':
        try:
            chat_id = message.text.split()[1]
            if chat_id in access_list:
                del access_list[chat_id]
                bot.reply_to(message, f"Access revoked for user {chat_id}.")
            else:
                bot.reply_to(message, f"User {chat_id} does not have access.")
        except IndexError:
            bot.reply_to(message, "Please provide a chat ID to revoke access.")
    else:
        bot.reply_to(message, "You are not authorized to use this command.")


@bot.message_handler(commands=["start"])
def start(message):
    if not access_list.get(str(message.chat.id)):
        bot.reply_to(message, "You cannot use the bot. Contact developers to purchase a bot subscription @nub_kiing")
        return
    bot.reply_to(message, "Send the file now")


@bot.message_handler(content_types=["document"])
def main(message):
    if not access_list.get(str(message.chat.id)):
        bot.reply_to(message, "You cannot use the bot. Contact developers to purchase a bot subscription @nub_kiing")
        return

    dd = 0
    live = 0
    ko = bot.reply_to(message, "Checking Your Cards...⌛").message_id
    ee = bot.download_file(bot.get_file(message.document.file_id).file_path)
    with open("combo.txt", "wb") as w:
        w.write(ee)
    try:
        with open("combo.txt", 'r') as file:
            lino = file.readlines()
            total = len(lino)
            for cc in lino:
                current_dir = os.getcwd()
                for filename in os.listdir(current_dir):
                    if filename.endswith(".stop"):
                        bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='𝗦𝗧𝗢𝗣𝗣𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @Rein_696')
                        os.remove('stop.stop')
                        return
                try:
                    data = requests.get('https://lookup.binlist.net/' + cc[:6]).json()
                except:
                    pass
                try:
                    bank = (data['bank']['name'])
                except:
                    bank = ('unknown')
                try:
                    emj = (data['country']['emoji'])
                except:
                    emj = ('unknown')
                try:
                    cn = (data['country']['name'])
                except:
                    cn = ('unknown')
                try:
                    dicr = (data['scheme'])
                except:
                    dicr = ('unknown')
                try:
                    typ = (data['type'])
                except:
                    typ = ('unknown')
                try:
                    url = (data['bank']['url'])
                except:
                    url = ('unknown')

                try:
                    last = str(Tele(cc))
                except Exception as e:
                    print(e)
                    last = "ERROR"
                if 'risk' in last:
                    last = 'declined'
                elif 'Duplicate' in last:
                    last = 'Approved'
                mes = types.InlineKeyboardMarkup(row_width=1)
        cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
        status = types.InlineKeyboardButton(f"{last}", callback_data='u8')
        cm3 = types.InlineKeyboardButton(f"• Hits ✅ ➜ [ {live} ] •", callback_data='x')
        cm4 = types.InlineKeyboardButton(f"• Declined ❌ ➜ [ {dd} ] •", callback_data='x')
        cm5 = types.InlineKeyboardButton(f"• Total 👻 ➜ [ {total} ] •", callback_data='x')
        stop=types.InlineKeyboardButton(f"[ 𝐒𝐓𝐎𝐏 ]", callback_data='stop')
        mes.add(cm1,status, cm3, cm4, cm5, stop)
        bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''Wait for processing 
𝒃𝒚 ➜ @nub_kiing ''', reply_markup=mes)
        msg = f'''◆ 𝑪𝑨𝑹𝑫  ➜ {cc} 
◆ 𝑺𝑻𝑨𝑻𝑼𝑺 ➜ Charged! 🔥
◆ 𝑹𝑬𝑺𝑼𝑳𝑻 ➜ Thanks for purchasing! 
◆ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➜ 𝙎𝙏𝙍𝙄𝙋𝙀 $1
━━━━━━━━━━━━━━━━━
◆ 𝑩𝑰𝑵 ➜ {cc[:6]} - {dicr} - {typ} 
◆ 𝑪𝑶𝑼𝑵𝑻𝑹𝒀 ➜ {cn} - {emj} 
◆ 𝑩𝑨𝑵𝑲 ➜ {bank}
◆ 𝑼𝑹𝑳 ➜ {url}
━━━━━━━━━━━━━━━━━
◆ 𝑩𝒀: @nub_kiing
◆𝑷𝑹𝑶𝑿𝒀𝑺: 𝑷𝑹𝑶𝑿𝒀 𝑳𝑰𝑽𝑬 ✅ '''
        print(last)
        if 'Thank you for your message.' in last or 'Thank you for your message. We will get in touch with you shortly' in last:
          live += 1
          bot.reply_to(message, msg)
        elif 'security code is incorrect' in last or 'security code is invalid' in last or "Your card's security code is incorrect." in last:
          msg = f'''◆ 𝑪𝑨𝑹𝑫  ➜ {cc} 
◆ 𝑺𝑻𝑨𝑻𝑼𝑺 ➜ Approved! ✅
◆ 𝑹𝑬𝑺𝑼𝑳𝑻 ➜ Security code incorrect 
◆ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➜ 𝙎𝙏𝙍𝙄𝙋𝙀 $1
━━━━━━━━━━━━━━━━━
◆ 𝑩𝑰𝑵 ➜ {cc[:6]} - {dicr} - {typ} 
◆ 𝑪𝑶𝑼𝑵𝑻𝑹𝒀 ➜ {cn} - {emj} 
◆ 𝑩𝑨𝑵𝑲 ➜ {bank}
◆ 𝑼𝑹𝑳 ➜ {url}
━━━━━━━━━━━━━━━━━
◆ 𝑩𝒀: @nub_kiing
◆𝑷𝑹𝑶𝑿𝒀𝑺: 𝑷𝑹𝑶𝑿𝒀 𝑳𝑰𝑽𝑬 ✅ '''
          live += 1
          bot.reply_to(message, msg)
        elif 'insufficient funds' in last or 'Your card has insufficient funds' in last:
          msg = f'''◆ 𝑪𝑨𝑹𝑫  ➜ {cc} 
◆ 𝑺𝑻𝑨𝑻𝑼𝑺 ➜ Approved! ✅
◆ 𝑹𝑬𝑺𝑼𝑳𝑻 ➜ Insufficient Funds!
◆ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➜ 𝙎𝙏𝙍𝙄𝙋𝙀 $1
━━━━━━━━━━━━━━━━━
◆ 𝑩𝑰𝑵 ➜ {cc[:6]} - {dicr} - {typ} 
◆ 𝑪𝑶𝑼𝑵𝑻𝑹𝒀 ➜ {cn} - {emj} 
◆ 𝑩𝑨𝑵𝑲 ➜ {bank}
◆ 𝑼𝑹𝑳 ➜ {url}
━━━━━━━━━━━━━━━━━
◆ 𝑩𝒀: @nub_kiing
◆𝑷𝑹𝑶𝑿𝒀𝑺: 𝑷𝑹𝑶𝑿𝒀 𝑳𝑰𝑽𝑬 ✅ '''
          live += 1
          bot.reply_to(message, msg)
        else:
          dd += 1
          time.sleep(1)
  except Exception as e:
    print(e)
  bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='𝗕𝗘𝗘𝗡 𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @nub_kiing')
@bot.callback_query_handler(func=lambda call: call.data == 'stop')
def menu_callback(call):
  with open("stop.stop", "w") as file:
    pass
print("+-----------------------------------------------------------------+")
bot.polling()
