import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()


def enviar_mensagem(mensagem, numero):
    url = f"https://graph.facebook.com/v14.0/{os.environ['IDENTIFICACAO_DO_NUMERO_DE_TELEFONE']}/messages"

    payload = json.dumps({
        "messaging_product": "whatsapp",
        "to": '5562998010102',
        "type": "template",
        "template": {
            "name": "hello_world",
            "language": {
                "code": "en_US"
            }
        }
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': F"Bearer {os.environ['TOKEN_DE_ENVIO_DE_MENSAGEM']}"
    }

    response = requests.request("POST", url, headers=headers, data=payload)
