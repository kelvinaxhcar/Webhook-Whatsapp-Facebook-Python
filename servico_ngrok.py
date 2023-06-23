import os
import subprocess
import requests


def iniciar_ngrok():
    diretorio_raiz = os.path.dirname(os.path.abspath(__file__))
    giretorio_do_ngrok = os.path.join(diretorio_raiz, "ngrok.exe")
    auth_token = os.environ['AUTH_TOKEN_NGROK']

    subprocess.call(['taskkill', '/F', '/IM', 'ngrok.exe'])
    configure_auth_token(giretorio_do_ngrok, auth_token)

    subprocess.Popen([giretorio_do_ngrok, 'http', f'http://127.0.0.1:{os.getenv("PORTA")}'])

    ngrok_url = get_ngrok_url()
    if ngrok_url:
        print('URL do ngrok:')
        print(ngrok_url)
    else:
        print('Não foi possível obter a URL do ngrok.')


def get_ngrok_url():
    response = requests.get('http://localhost:4040/api/tunnels')
    data = response.json()
    tunnels = data['tunnels']
    if tunnels:
        return tunnels[0]['public_url']
    return None


def configure_auth_token(ngrok_path, auth_token):
    ngrok_config_process = subprocess.Popen([ngrok_path, 'config', 'authtoken', auth_token])
    ngrok_config_process.wait()
