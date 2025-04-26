from restaurante import Restaurante 

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



sorv = Sorveteria("BlueColdMix","gourmet")
sorv.mostrarRestaurante()

while True:
    sabor=input("Digite os sabores disponiveis ou s para sair:\n")
    if sabor== "s":
          break
    else:
        sorv.increment_sabor_served(sabor)

sorv.mostrar_sabores()
