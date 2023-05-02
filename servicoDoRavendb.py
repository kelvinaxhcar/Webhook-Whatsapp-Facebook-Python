from ravendb import DocumentStore
import os
from dotenv import load_dotenv

load_dotenv()


def obter_store():
    store = DocumentStore(os.environ['link_do_ravendb'], os.environ['nome_do_banco'],certificate="")
    return store.initialize()


def obter_sessao():
    store = obter_store()
    with store.open_session() as session:
        return session
