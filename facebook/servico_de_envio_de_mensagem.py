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
        'Authorization': 'Bearer EAAHgBf19GAQBAOFMlZAp7pZCmsfAd3IxlcZCnkJF4T0r0gPJ2DlfSpkUIIMBp4dGiJ77t61fXZBjacdxCSqVs6rqXJtlRvZAmZCO3uZBTjKNkKZC3Pot4F0n70iwZCWxW4hm7jT7ZAtzHOujuYpZBbvmICTE6St5tIA4DAbgjyLACaqKZCSnbKsWfYFnw32eWrTyPnehKRxh2GPMOwZDZD'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
