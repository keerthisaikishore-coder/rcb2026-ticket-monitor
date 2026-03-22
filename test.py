import requests

BOT_TOKEN = "8577847140:AAGufo6iYE4jMacG0O7LOML7bbPOQlUcu_c"
CHAT_ID = "851468594"

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

response = requests.post(url, data={
    "chat_id": CHAT_ID,
    "text": "✅ SUCCESS: Your RCB Ticket Bot is working!"
})

print(response.text)
