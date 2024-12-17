import random

def jogodaforca():

    palavras = ["python", "programacao", "desafio", "jogo","linguagem","desenvolvedor","faculdade","aula","java","computador","engenharia","professor","mouse","carro" ]
    while True:
        #escolhendo a palavra
        palavra_secreta = random.choice(palavras)
        chutes = []
        dic_palavra={}
        print("vamos comecar o jogo da forca:")
        print ("_ " * len(palavra_secreta))
        #declarando o dicionario
        dic_palavra = {letra: False for letra in palavra_secreta}
            
        print
        tentativas=5
        while (tentativas > 0): 
            
            #input
            letra=input("digite uma letra:").lower()
            if letra in chutes:
                print("Você já tentou essa letra.")
                continue
            
            if letra in dic_palavra :
                dic_palavra[letra] = True
                print("Voce acertou!")
                
            else:
                tentativas-=1
                print(f"Voce errou total de tentativas restantes:{tentativas}")
            
            chutes.append(letra)
            #printando o jogo
            progresso = ""
            
            for caracter in palavra_secreta: 
                if dic_palavra[caracter]:
                    progresso += caracter + " "
                else:
                    progresso += "_ "
                    
            print (progresso)        
            #chutes        
            print(f"letra enviadas:{chutes}")

            if all(dic_palavra.values()):
                print ("\nParabéns, você ganhou!")
                break
            
        if tentativas == 0 :
             print(f"\nVocê perdeu! A palavra era: {palavra_secreta}")
        jogar_novamente=input("deseja jogar novamente? sim ou nao")
        if jogar_novamente != "sim":
            print ("Obrigado por jogar!")
            break
                
jogodaforca()      
            
             
                   
            
    
    
    





