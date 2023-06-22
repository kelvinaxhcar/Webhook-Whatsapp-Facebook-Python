import os
import subprocess
import sys


def iniciar_ngrok():
    project_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, os.pardir))
    ngrok_path = os.path.join(project_directory.replace("src\\Tunel", ""), "src", "ngrok.exe")
    auth_token = "2CnojNQ4fMlfsf2S3rfwHfchNMv_oDqjtcLmKi27NQHPM8BB"

    for process in get_processes_by_name("ngrok"):
        process.kill()

    configure_auth_token(ngrok_path, auth_token)

    local_server_port = 7105
    ngrok_process = subprocess.Popen([ngrok_path, f"http https://localhost:{local_server_port}"])

    print("Túnel do ngrok iniciado. Pressione qualquer tecla para encerrar.")
    input()

    ngrok_process.terminate()


def get_processes_by_name(name):
    if sys.platform == 'win32':
        cmd = ['tasklist']
    else:
        cmd = ['ps', '-ef']

    output = subprocess.check_output(cmd).decode('utf-8').lower()
    return [line.split()[0] for line in output.splitlines() if name.lower() in line.lower()]


def configure_auth_token(ngrok_path, auth_token):
    ngrok_config_process = subprocess.Popen([ngrok_path, f"config authtoken {auth_token}"])
    ngrok_config_process.wait()

