import requests
import json
import time

__config__ = json.load(open('config.json', 'r'))

data = data = {
    "content": f"|| @everyone || || {__config__['lien']} ||",
    "embeds": [
        {
            "title": "Juste imagine",
            "description": f"**vous vous êtes fait raid par `{__config__['auteur']}`**",
            "color": 0,
            "image": {
                "url": "https://i.pinimg.com/originals/16/03/fb/1603fb7077abb9093f4af305b4e5ce79.gif"
            }
        }
    ],
    "username": f"{__config__['auteur']}",
    "avatar_url": "https://i.pinimg.com/736x/65/59/37/6559374e52a921ad76785d2175db21c2.jpg",
    "attachments": []
}

while True:
    for i in range(len(__config__['webhooks'])):
        requests.post(__config__['webhooks'][i], json=data)
    time.sleep(3)
