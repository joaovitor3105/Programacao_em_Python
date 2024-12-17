class Pessoa:
    def __init__(self,nome,sexo,endereco,cpf,telefone,identidade):
        self.nome=nome
        self.sexo=sexo
        self.endereco=endereco
        self.cpf=cpf
        self.telefone=telefone
        self.identidade=identidade
    def imprimirDados(self):
        print(f"Nome:{self.nome}\nSexo:{self.sexo}\nEndereço:{self.endereco}\nCpf:{self.cpf}\nTelefone:{self.telefone}\nIdentidade:{self.identidade}")
    