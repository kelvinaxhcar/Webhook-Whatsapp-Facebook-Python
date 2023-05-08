from flask import Flask, request, jsonify
import servico_de_mensagem
import facebook.servico_do_facebook as servico_do_facebook
from dotenv import load_dotenv
import servicoDoRavendb as servicoDoRavendb
import classes as classes

app = Flask(__name__)
load_dotenv()


@app.route('/webhooks', methods=['GET'])
def webhook_autenticacao():
    return servico_do_facebook.validar_inscricao(request)


@app.route('/webhooks', methods=['POST'])
def webhook_recepcao():
    dados_da_mensagem = servico_de_mensagem.obter_dados_da_mensagem(request)
    sessao = servicoDoRavendb.obter_sessao()

    mensagem_recebida = classes.MensagemRecebida(None, "Ack_numero", dados_da_mensagem)

    sessao.store(mensagem_recebida)
    sessao.save_changes()

    return jsonify({'status': 'ok'})


if __name__ == '__main__': app.run()
