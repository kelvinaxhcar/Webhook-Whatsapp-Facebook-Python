import json
import constantes_do_servico_de_mensagem


def converter_request_para_objeto(request):
    request.get_data()
    raw_request_body = request.data.decode('utf-8')
    return json.loads(raw_request_body)


def obter_dados_da_mensagem(request):
    json_convertido = converter_request_para_objeto(request)

    valor = json_convertido[constantes_do_servico_de_mensagem.entry][constantes_do_servico_de_mensagem.zero][
        constantes_do_servico_de_mensagem.changes][constantes_do_servico_de_mensagem.zero][constantes_do_servico_de_mensagem.value]
    tipo = valor[constantes_do_servico_de_mensagem.messages][constantes_do_servico_de_mensagem.zero][constantes_do_servico_de_mensagem.type]
    message = valor[constantes_do_servico_de_mensagem.messages][constantes_do_servico_de_mensagem.zero][
        constantes_do_servico_de_mensagem.text][constantes_do_servico_de_mensagem.body]
    contact = valor[constantes_do_servico_de_mensagem.contacts][constantes_do_servico_de_mensagem.zero][constantes_do_servico_de_mensagem.wa_id]

    return {"tipo": tipo, "message": message, "contato": contact}
