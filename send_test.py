import requests

# Telegram Bot Token
BOT_TOKEN = "8672839322:AAFgVNBHD0RAOBV1ydiuSo9w5xIl8exX-9Y"

# Telegram Chat ID
CHAT_ID = "8291705336"

# Message
message = "✅ Test Successful! Telegram bot is working."

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

payload = {
    "chat_id": CHAT_ID,
    "text": message
}

response = requests.post(url, data=payload)

print(response.text)
