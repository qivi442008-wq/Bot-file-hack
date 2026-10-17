import os
import threading
import random
import string
os.system('pip install pyTelegramBotAPI Flask gunicorn')

from flask import Flask, render_template_string, request, jsonify
import telebot
from telebot import types

TOKEN = "8714010498:AAFicf-XhijjjdLaVPD9CJResmx8O2-FWUA"
bot = telebot.TeleBot(TOKEN)

LINK_GET_KEY_WEB = "https://bot-file-hack.onrender.com"
DATABASE_KEY = {}

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>VIETDEV NEXUS V2.0 - GET KEY</title>
    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        body {
            background-color: #0d0d0d;
            color: #ffffff;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            padding: 20px;
        }
        .container {
            width: 100%;
            max-width: 400px;
            background: #141414;
            border: 1px solid #ff3333;
            border-radius: 12px;
            padding: 25px 20px;
            box-shadow: 0 0 20px rgba(255, 51, 51, 0.2);
            text-align: center;
        }
        .logo {
            width: 100px;
            height: 100px;
            margin: 0 auto 15px;
            border-radius: 50%;
            border: 2px solid #ff3333;
            box-shadow: 0 0 15px rgba(255, 0, 0, 0.5);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 40px;
            background: #1a0000;
        }
        h1 {
            color: #ff3333;
            font-size: 24px;
            font-weight: bold;
            letter-spacing: 1px;
            margin-bottom: 5px;
            text-shadow: 0 0 10px rgba(255, 51, 51, 0.5);
        }
        .subtitle {
            color: #888;
            font-size: 13px;
            margin-bottom: 20px;
        }
        .card {
            background: #1a1a1a;
            border: 1px solid #2a2a2a;
            border-radius: 8px;
            padding: 15px;
            margin-bottom: 12px;
        }
        .card-number {
            color: #ff3333;
            font-size: 26px;
            font-weight: bold;
        }
        .card-label {
            color: #777;
            font-size: 11px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-top: 2px;
        }
        .btn {
            width: 100%;
            padding: 14px;
            margin-top: 10px;
            background: #1a1a1a;
            border: 1.5px solid #ff3333;
            border-radius: 8px;
            color: #ff3333;
            font-size: 15px;
            font-weight: bold;
            cursor: pointer;
            transition: all 0.2s ease;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            text-decoration: none;
        }
        .btn:hover, .btn:active {
            background: #ff3333;
            color: #ffffff;
            box-shadow: 0 0 15px rgba(255, 51, 51, 0.4);
        }
        .btn-secondary {
            border-color: #333;
            color: #aaa;
        }
        .btn-secondary:hover {
            background: #333;
            color: #fff;
            box-shadow: none;
        }
        .key-box {
            display: none;
            background: #220000;
            border: 2px dashed #ff3333;
            padding: 15px;
            border-radius: 8px;
            margin-top: 15px;
            color: #fff;
            font-size: 18px;
            font-weight: bold;
            letter-spacing: 1px;
            word-break: break-all;
        }
    </style>
</head>
<body>
    <div class="container" id="mainPage">
        <div class="logo">⚡</div>
        <h1>VIETDEV NEXUS V2.0</h1>
        <p class="subtitle">Get Key 12h Free System</p>

        <div class="card">
            <div class="card-number">386</div>
            <div class="card-label">KEYS CÒN LẠI</div>
        </div>

        <div class="card">
            <div class="card-number" style="color: #00ff66;">FREE</div>
            <div class="card-label">HOÀN TOÀN MIỄN PHÍ</div>
        </div>

        <button class="btn" onclick="showKeyPage()">🔑 LẤY KEY MIỄN PHÍ</button>
        <a href="https://zalo.me/0329367512" target="_blank" class="btn btn-secondary">👤 LIÊN HỆ ADMIN</a>
        <a href="https://t.me/vietdev999" target="_blank" class="btn btn-secondary">👥 THAM GIA NHÓM</a>
    </div>

    <div class="container" id="keyPage" style="display: none;">
        <div class="logo">🔑</div>
        <h1>KEY ĐÃ SẴN SÀNG</h1>
        <p class="subtitle">Mỗi địa chỉ IP chỉ nhận 1 key duy nhất</p>

        <button class="btn" id="btnGet" onclick="fetchKey()">LẤY KEY</button>
        <div class="key-box" id="keyDisplay">Đang tạo key...</div>
        
        <button class="btn btn-secondary" onclick="showMainPage()" style="margin-top: 15px;">← VỀ TRANG CHỦ</button>
    </div>

    <script>
        function showKeyPage() {
            document.getElementById('mainPage').style.display = 'none';
            document.getElementById('keyPage').style.display = 'block';
        }

        function showMainPage() {
            document.getElementById('keyPage').style.display = 'none';
            document.getElementById('mainPage').style.display = 'block';
        }

        function fetchKey() {
            const btnGet = document.getElementById('btnGet');
            const keyDisplay = document.getElementById('keyDisplay');
            
            btnGet.innerText = "ĐANG TẠO...";
            
            fetch('/get-key')
                .then(response => response.json())
                .then(data => {
                    keyDisplay.style.display = 'block';
                    keyDisplay.innerText = data.key;
                    btnGet.innerText = "ĐÃ LẤY KEY THÀNH CÔNG!";
                    btnGet.style.background = "#ff3333";
                    btnGet.style.color = "#fff";
                })
                .catch(err => {
                    keyDisplay.style.display = 'block';
                    keyDisplay.innerText = "Lỗi kết nối server!";
                });
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/get-key', methods=['GET'])
def get_key_api():
    user_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    if user_ip in DATABASE_KEY:
        assigned_key = DATABASE_KEY[user_ip]
    else:
        random_suffix = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        assigned_key = f"VIETDEV-{random_suffix}"
        DATABASE_KEY[user_ip] = assigned_key
    return jsonify({'key': assigned_key})

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup()
    btn_web = types.InlineKeyboardButton("🔑 Lấy Key Tại Đây", url=LINK_GET_KEY_WEB)
    markup.add(btn_web)
    bot.reply_to(message, f"Xin chào {message.from_user.first_name}!\nBấm vào nút bên dưới để truy cập trang web lấy Key:", reply_markup=markup)

def run_bot():
    try:
        bot.infinity_polling(none_stop=True, interval=0, timeout=20)
    except Exception as e:
        print(f"Bot error: {e}")

if __name__ == "__main__":
    bot_thread = threading.Thread(target=run_bot)
    bot_thread.daemon = True
    bot_thread.start()

    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
