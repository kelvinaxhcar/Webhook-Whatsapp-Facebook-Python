import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()


def enviar_mensagem_de_texto(mensagem, numero):
    url = f"https://graph.facebook.com/v14.0/{os.environ['IDENTIFICACAO_DO_NUMERO_DE_TELEFONE']}/messages"

    payload = json.dumps({
        "messaging_product": "whatsapp",
        "to": adicionar_nove(numero[:4] + '9' + numero[4:]),
        "type": "text",
        "text": {
            "body": mensagem
        }
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': F"Bearer {os.environ['TOKEN_DE_ENVIO_DE_MENSAGEM']}"
    }

    response = requests.request("POST", url, headers=headers, data=payload)


def adicionar_nove(telefone):
    if telefone.isdigit() and len(telefone) == 10:
        return telefone[:5] + '9' + telefone[5:]
    else:
        return telefone