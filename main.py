import servico_de_mensagem
import facebook.servico_do_facebook as servico_do_facebook
import servicoDoRavendb as servicoDoRavendb
import classes as classes
import facebook.servico_de_envio_de_mensagem as servico_de_envio_de_mensagem
from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv
import servico_ngrok

app = Flask(__name__)
load_dotenv()


@app.route('/webhook', methods=['GET'])
def webhook_autenticacao():
    return servico_do_facebook.validar_inscricao(request)


@app.route('/webhook', methods=['POST'])
def webhook_recepcao():
    dados_da_mensagem = servico_de_mensagem.obter_dados_da_mensagem(request)

    mensagem_recebida = classes.HistoricoDeMensagemRecebida(None, dados_da_mensagem)
    servico_de_envio_de_mensagem.enviar_mensagem_de_texto(dados_da_mensagem.mensagem, dados_da_mensagem.contato)

    servicoDoRavendb.salvar_objeto(mensagem_recebida)
    return jsonify({'status': 'ok'})


port = int(os.getenv("PORTA"))
if __name__ == '__main__':
    if port != 0:
        if os.environ['GERAR_LINK_NGROK'].lower() == 'sim':
            servico_ngrok.iniciar_ngrok()
        app.run(host='0.0.0.0', port=port)
