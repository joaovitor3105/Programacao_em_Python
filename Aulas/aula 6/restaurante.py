
#class restaurante
class Restaurante():
    def __init__(self,restaurante_nome,tipo_cozinha):
        self.restaurante_nome= restaurante_nome
        self.tipo_cozinha = tipo_cozinha 
        self.number_served = 0
    def mostrarRestaurante(self):
            print(f"Restaurante:{self.restaurante_nome},Tipó da cozinha:{self.tipo_cozinha},clientes atendidos:{self.number_served}") 

    def restauranteAberto(self):
            print('o restaurante esta aberto')

    def set_number_served(self,num):
          self.number_served=num

    def increment_number_served(self):
          
          self.number_served+=1


#class Sorveteria

class Sorveteria(Restaurante):
    def __init__(self, restaurante_nome, tipo_cozinha):
            super().__init__(restaurante_nome, tipo_cozinha)
            self.sabor = []
       
    def   increment_sabor_served(self,sabor):
          self.sabor.append(sabor)
    def mostrar_sabores(self):
          print("Tem os seguintes sabores:\n")
          for i in self.sabor:
                print(i)






#Main

# rest = Restaurante("big Alvarás","Italiano")

# print(rest.restaurante_nome)
# print(rest.tipo_cozinha)

# rest.mostrarRestaurante()
# rest.set_number_served(int(input("quantas pessoas foram servidas?\n")))
# rest.increment_number_served()  
# rest.restauranteAberto()
# rest.mostrarRestaurante()

# sorv = Sorveteria("BlueColdMix","gourmet")
# while True:
#     sabor=input("Digite os sabores disponiveis ou s para sair")
#     if sabor== "s":
#           break
#     else:
#         sorv.increment_sabor_served(sabor)

# sorv.mostrar_sabores()
# sorv.mostrarRestaurante()
