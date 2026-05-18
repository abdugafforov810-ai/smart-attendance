import requests

TOKEN = "8510746661:AAH8DWpE6GFxVNmjhP3VNWkwxRpxZq3woZE"

CHAT_ID = "5645708076"

message = "📢 Aqlli Davomat Tizimi ishlayapti 😎"

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

data = {
    "chat_id": CHAT_ID,
    "text": message
}

requests.post(url, data=data)