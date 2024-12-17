from Pessoa import Pessoa
class Medico(Pessoa):
    def __init__(self, nome, sexo, endereco, cpf, telefone, identidade,CRM,especialidade):
        super().__init__(nome, sexo, endereco, cpf, telefone, identidade)
        self.CRM=CRM
        self.especialidade=especialidade
    
        