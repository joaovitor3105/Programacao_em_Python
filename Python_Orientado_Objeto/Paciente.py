from Pessoa import Pessoa
class Paciente(Pessoa):
    def __init__(self, nome, sexo, endereco, cpf, telefone, identidade,medicacaocontinua):
        super().__init__(nome, sexo, endereco, cpf, telefone, identidade)
        self.medicacaocontinua=medicacaocontinua
    
    