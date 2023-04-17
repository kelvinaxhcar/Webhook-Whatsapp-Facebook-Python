from flask import Flask, request, jsonify
import json

app = Flask(__name__)


@app.route('/webhooks', methods=['GET'])
def webhook_autenticacao():
    challenge = request.args.get('hub.challenge', '')
    return challenge


@app.route('/webhooks', methods=['POST'])
def webhook_recepcao():
    request.get_data()
    raw_request_body = request.data.decode('utf-8')
    res = json.loads(raw_request_body)

    return jsonify({'status': 'ok'})


if __name__ == '__main__': app.run()
