class MensagemRecebida:
    def __init__(self, Id: str = None, numero_de_telefone: str = None, mensagem: str = None):
        self.Id: str = Id
        self.numero_de_telefone = numero_de_telefone
        self.mensagem = mensagem