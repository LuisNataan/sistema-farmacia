import Receita

class Paciente:
    def __init__(self, nome: str, cpf: str, idade: int):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade

    def __eq__(self, other) -> bool:
        if self.nome == other.nome and self.cpf == other.cpf:
            return True
        else:
            return False