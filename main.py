from flask import Flask, request, jsonify
import servico_de_mensagem
import facebook.servico_do_facebook as servico_do_facebook

app = Flask(__name__)


@app.route("/webhooks", methods=["GET"])
def webhook_autenticacao():
    return servico_do_facebook


@app.route("/webhooks", methods=["POST"])
def webhook_recepcao():
    dados_da_mensagem = servico_de_mensagem.obter_dados_da_mensagem(request)

    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run()
