import Receita
import Paciente

from datetime import date

class Farmaceutico:
    def __init__(self, nome):
        self.nome = nome

    def receber_receita(self, paciente: Paciente, receita: Receita):
        self.paciente = paciente
        self.receita = paciente

    def validar_receita(self):
        validade = self.receita.validade.split("/")

        if len(validade) == 2:
            print(validade.reverse())

        ano = int(validade[0])
        mes = int(validade[1])
        dia = int(validade[2])

        validacoes = list()
        validacoes.append(self.paciente == self.receita.nome)
        validacoes.append(date(dia, mes, ano) >= date.today())
        validacoes.append(self.paciente.idade >= 18)
        return all(validacoes)

    def verificar_estoque(self):
        if not self.validar_receita():
            return False

        nome = ''
        quantidade = 0

        with open("Estoque.txt", "r") as file:
            for line in file:
                medicamento = line.split(';')
                # Verifica se
                if medicamento[1] == self.receita.medicamento:
                    nome = medicamento[1]
                    quantidade = int(medicamento[3].strip())
                    break


    def entregar_medicamento(self):
        pass

    def retirar_item_estoque(self):
        pass


