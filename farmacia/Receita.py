class Receita:

    def __init__(self, dados_receita):

        informacoes = dict(medicamento=dados_receita["medicamento"],
                             validade=dados_receita["validade"],
                             quantidade=dados_receita["quantidade"])