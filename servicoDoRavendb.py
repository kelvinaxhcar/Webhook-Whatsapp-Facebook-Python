from ravendb import DocumentStore
import os
from dotenv import load_dotenv

load_dotenv()


def obter_store():
    store = DocumentStore(os.environ['LINK_DO_RAVENDB'], os.environ['NOME_DO_BANCO'])
    store.certificate_pem_path = os.environ['CERT_PATH']
    return store.initialize()


def obter_sessao():
    store = obter_store()
    with store.open_session() as session:
        return session
