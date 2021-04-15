import Receita

class Paciente:
    def __init__(self, receita: Receita, documento):
        self.receita = receita
        self.documento = documento



        dados_paciente = dict(nome=documento["nome"],
                              cpf=documento["cpf"])
