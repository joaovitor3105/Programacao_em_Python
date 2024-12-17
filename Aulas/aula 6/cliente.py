class Cliente ():
    def __init__(self,first_name,last_name,historico=[]):
        self.first_name = first_name
        self.last_name = last_name
        self.historico = historico
    def describe_client(self):
        print(f"primeiro nome:{self.first_name},ultimo nome :{self.last_name},historico:{self.historico}")
    
    def greet_client(self):
        print(f"Saudaçoes{self.first_name} ")

    def agregar_historico(self,novo):
       
        self.historico.append(novo)

ahmed = Cliente("ahmed","Amer")
Bluecold = Cliente("joao","vitor")
Big = Cliente("Big","Alvaras")
joao = Cliente("joao","pedro")
    
ahmed.describe_client()
Bluecold.describe_client()
Big.greet_client()
Big.agregar_historico("motorista")
Big.agregar_historico("bagre")
Big.describe_client()
