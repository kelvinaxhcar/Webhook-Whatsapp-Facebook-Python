from nltk.chat.util import Chat, reflections


def conversar(user_input):
    conversas = [
        [
            r"Oi|Olá|E aí",
            ["Olá!", "Oi!", "E aí, como posso ajudar?"]
        ]
    ]

    chatbot = Chat(conversas, reflections)
    return chatbot.respond(user_input)
