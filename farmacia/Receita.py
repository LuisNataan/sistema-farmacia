class Receita:

    def __init__(self, dados_receita: dict):
        self.medicamento = dados_receita["medicamento"]
        self.validade = dados_receita["validade"]
        self.quantidade = dados_receita["quantidade"]
        self.nome = dados_receita["nome"]
