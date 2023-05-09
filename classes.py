import datetime


class HistoricoDeMensagemRecebida:
    def __init__(self, Id: str = None, dados_da_mensagem: str = None):
        self.Id: str = Id
        self.dados_da_mensagem = dados_da_mensagem
        self.data = datetime.datetime.now()


class MensagemRecebidaDoWhatsapp:
    def __init__(self, tipo: str = None, mensagem: str = None, contato: str = None):
        self.tipo: str = tipo
        self.mensagem = mensagem
        self.contato = contato
