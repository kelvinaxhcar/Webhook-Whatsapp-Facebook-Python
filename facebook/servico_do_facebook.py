import facebook.constantes_do_facebook as constantes_do_facebook


def validar_inscricao(request):
    challenge = request.args.get(constantes_do_facebook.hub_challenge, "")
    return challenge
