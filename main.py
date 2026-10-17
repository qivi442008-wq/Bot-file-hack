import os
import threading
from flask import Flask, render_template_string
import telebot
from telebot import types

TOKEN = "8743690981:AAHgq1CYm2CzcxnFL1fGJNasR3EACPcn0Ps"
bot = telebot.TeleBot(TOKEN)

ADMIN_USERNAME = "@vietdev999"
ZALO_CONTACT = "0329367512"
TEN_CHU_BOT = "NGUYEN QUANG VIET"
MANG_KEY_HOP_LE = "VIETDEV2026"

LINK_GET_KEY_WEB = "https://bot-file-hack.onrender.com"

KHO_GAME = {
    '8ball': {
        'ten': '8 Ball Pool Aimbot Pro',
        'link_lay_key': LINK_GET_KEY_WEB,
        'link_tai_file': 'https://mega.nz/file/link-tai-file-8ball-that'
    },
    'ff': {
        'ten': 'FreeFire Menu VIP',
        'link_lay_key': LINK_GET_KEY_WEB,
        'link_tai_file': 'https://mega.nz/file/link-tai-file-ff-that'
    }
}

cho_nhap_key = {}

app = Flask(__name__)

HTML_WEB_KEY = """
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hệ Thống Get Key - VietDev</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-950 text-white flex items-center justify-center h-screen m-0">
    <div class="bg-gray-900 border border-gray-800 p-8 rounded-2xl shadow-2xl max-w-md w-full text-center mx-4">
        <h1 class="text-2xl font-bold mb-2 text-white">🔑 XÁC THỰC LẤY KEY</h1>
        <p class="text-gray-400 text-sm mb-6">Hoàn thành đếm ngược để nhận mã key mở khóa file hack.</p>
        
        <div id="step1">
            <button onclick="startCountdown()" class="w-full bg-blue-600 hover:bg-blue-700 text-white font-bold py-3 px-4 rounded-xl">
                🚀 Bấm Vào Để Lấy Key
            </button>
        </div>

        <div id="step2" class="hidden py-4">
            <p class="text-yellow-400 font-medium">Đang tạo mã key... Vui lòng chờ <span id="countdown" class="font-bold text-white text-lg">5</span> giây</p>
        </div>

        <div id="step3" class="hidden">
            <p class="text-gray-300 text-sm mb-2 font-medium">Mã Key của bạn đây:</p>
            <div class="bg-black/50 p-3 rounded-xl border border-gray-800 text-green-400 font-mono text-xl font-bold mb-4">
                {{ key }}
            </div>
            <button onclick="copyKey()" class="w-full bg-green-600 hover:bg-green-700 text-white font-bold py-3 px-4 rounded-xl">
                📋 Sao chép Key ngay
            </button>
        </div>
    </div>

    <script>
        function startCountdown() {
            document.getElementById('step1').classList.add('hidden');
            document.getElementById('step2').classList.remove('hidden');
            let seconds = 5;
            let interval = setInterval(function() {
                seconds--;
                document.getElementById('countdown').innerText = seconds;
                if (seconds <= 0) {
                    clearInterval(interval);
                    document.getElementById('step2').classList.add('hidden');
                    document.getElementById('step3').classList.remove('hidden');
                }
            }, 1000);
        }

        function copyKey() {
            navigator.clipboard.writeText("{{ key }}").then(() => alert("Đã sao chép key thành công! Hãy dán vào Bot Telegram."));
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_WEB_KEY, key=MANG_KEY_HOP_LE)

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

@bot.message_handler(commands=['start'])
def lenh_start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add(
        types.KeyboardButton("🎁 File hack free"),
        types.KeyboardButton("📞 Hỗ trợ / Liên hệ")
    )
    text = f"🤖 **KHO FILE HACK FREE - {TEN_CHU_BOT}** 🤖\n\n👉 Vui lòng chọn chức năng bên dưới:"
    bot.send_message(message.chat.id, text, parse_mode="Markdown", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "🎁 File hack free")
def chon_danh_sach_game(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton("🎱 8 Ball Pool", callback_data='game_8ball'),
        types.InlineKeyboardButton("🔥 FreeFire", callback_data='game_ff')
    )
    bot.send_message(message.chat.id, "🎯 **CHỌN TỰA GAME BẠN MUỐN TẢI:**", parse_mode="Markdown", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "📞 Hỗ trợ / Liên hệ")
def thong_tin_lien_he(message):
    text = (
        f"📞 **THÔNG TIN LIÊN HỆ & HỖ TRỢ**\n\n"
        f"👤 Chủ quản: **{TEN_CHU_BOT}**\n"
        f"📱 Telegram Admin: {ADMIN_USERNAME}\n"
        f"💬 Số Zalo hỗ trợ: `{ZALO_CONTACT}`"
    )
    bot.send_message(message.chat.id, text, parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: call.data.startswith('game_'))
def xu_ly_chon_game(call):
    chat_id = call.message.chat.id
    ma_game = call.data.split('_')[1]
    if ma_game in KHO_GAME:
        game = KHO_GAME[ma_game]
        cho_nhap_key[chat_id] = ma_game
        text = (
            f"📥 **BẠN ĐÃ CHỌN: {game['ten']}**\n\n"
            f"1️⃣ Nhấp vào link để lấy mã Key:\n👉 {game['link_lay_key']}\n\n"
            f"2️⃣ Gửi mã Key đó vào khung chat này để nhận link tải!"
        )
        bot.edit_message_text(text, chat_id, call.message.message_id, parse_mode="Markdown")

@bot.message_handler(func=lambda message: True)
def kiem_tra_ma_key(message):
    chat_id = message.chat.id
    noi_dung_nhan = message.text.strip()
    if chat_id in cho_nhap_key:
        ma_game = cho_nhap_key[chat_id]
        game = KHO_GAME[ma_game]
        if noi_dung_nhan == MANG_KEY_HOP_LE:
            del cho_nhap_key[chat_id]
            thanh_cong = f"✅ **XÁC THỰC THÀNH CÔNG!**\n\nLink tải file **{game['ten']}**:\n👉 {game['link_tai_file']}"
            bot.send_message(chat_id, thanh_cong, parse_mode="Markdown")
        else:
            bot.send_message(chat_id, "❌ **Mã key không hợp lệ!** Vui lòng lấy lại.")
    else:
        bot.send_message(chat_id, "👉 Bấm lệnh `/start` để mở menu chính.", parse_mode="Markdown")

if __name__ == '__main__':
    t = threading.Thread(target=run_flask)
    t.daemon = True
    t.start()
    bot.infinity_polling()
