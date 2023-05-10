from flask import Flask, request, jsonify
import servico_de_mensagem
import facebook.servico_do_facebook as servico_do_facebook
import servicoDoRavendb as servicoDoRavendb
import classes as classes
import facebook.servico_de_envio_de_mensagem as servico_de_envio_de_mensagem
from flask import Flask, render_template, make_response, send_from_directory
import os
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()


@app.route('/')
def render_index():
    return render_template('index.html')


@app.route('/webhooks', methods=['GET'])
def webhook_autenticacao():
    return servico_do_facebook.validar_inscricao(request)


@app.route('/webhooks', methods=['POST'])
def webhook_recepcao():
    dados_da_mensagem = servico_de_mensagem.obter_dados_da_mensagem(request)
    sessao = servicoDoRavendb.obter_sessao()

    mensagem_recebida = classes.HistoricoDeMensagemRecebida(None, dados_da_mensagem)
    servico_de_envio_de_mensagem.enviar_mensagem('', dados_da_mensagem.contato)

    sessao.store(mensagem_recebida)
    sessao.save_changes()

    return jsonify({'status': 'ok'})


port = int(os.getenv("PORT", 0))
if __name__ == '__main__':
    if port != 0:
        app.run(host='0.0.0.0', port=port)
    else:
        app.run(debug=True)


if __name__ == '__main__': app.run()

