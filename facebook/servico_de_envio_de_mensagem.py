import requests
import json


def enviar_mensagem(mensagem, numro):
    url = "https://graph.facebook.com/v14.0/113018894757357/messages"

    payload = json.dumps({
        "messaging_product": "whatsapp",
        "to": "{{Recipient-WA-ID}}",
        "type": "text",
        "template": {
            "name": "hello_world",
            "language": {
                "code": "en_US"
            }
        }
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': ''
    }

    response = requests.request("POST", url, headers=headers, data=payload)
