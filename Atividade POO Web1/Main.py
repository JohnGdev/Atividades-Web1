class Aluno:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf


class Equipe:
    def __init__(self, participantes, projeto):
        self.participantes = participantes
        self.projeto = projeto


class GerenciadorEquipes:
    def __init__(self):
        self.equipe_list = []
        
    def criarEquipe(self, participantes, projeto):
        for equipe in self.equipe_list:
            if equipe.projeto == projeto:
                for aluno in participantes:
                    if aluno in equipe.participantes:
                        print("A equipe não pode ser criada porque um ou mais alunos já estão em outra equipe com o mesmo projeto.")
                        return
                if len(set(participantes)) < len(participantes):
                    print("A equipe não pode ser criada porque há alunos duplicados.")
                    return
        nova_equipe = Equipe(participantes, projeto)
        self.equipe_list.append(nova_equipe)
        print("Equipe criada com sucesso!")


# Exemplo de uso:
gerenciador = GerenciadorEquipes()

aluno1 = Aluno("João", "123.456.789-00")
aluno2 = Aluno("Maria", "987.654.321-00")

participantes = [aluno1, aluno2]
projeto = "Sistema de Gerenciamento de Tarefas"

gerenciador.criarEquipe(participantes, projeto)  

participantes2 = [aluno1]
projeto2 = "Sistema de Gerenciamento de Tarefas"

gerenciador.criarEquipe(participantes2, projeto2)  

participantes3 = [aluno2, aluno1]
projeto3 = "Sistema de Gerenciamento de Tarefas"

gerenciador.criarEquipe(participantes3, projeto3)  