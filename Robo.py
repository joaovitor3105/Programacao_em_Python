mapa = [['R','#','-','-','-'],
        ['-','#','-','#','-'],
        ['-','-','-','#','!']]
i =0
j =0
# "#"=bloqueado,"-" = livre,"!" = final,"R" = Robo,"*" Caminho percorrido
       
while True:
        
     
        if (i+1 < len(mapa) and mapa[i+1][j]=="-"):
            mapa[i][j]="*"
            i=i+1
            mapa[i][j]="R"
        
        elif (i-1>=0 and mapa[i-1][j]=="-"):
            mapa[i][j]="*"
            i=i-1
            mapa[i][j]="R"          
            
        elif (j+1 < len(mapa[0]) and mapa[i][j+1]=="-"):
            mapa[i][j]="*"
            j=j+1
            mapa[i][j]="R"
           
        
        elif (j-1>=0 and mapa[i][j-1]=="-"):
            mapa[i][j]="*"
            j=j-1
            mapa[i][j]="R"
           
        else:
            if((i+1 < len(mapa) and mapa[i+1][j]=="!") or (i-1>=0 and mapa[i-1][j]=="!")or (j+1 < len(mapa[0]) and mapa[i][j+1]=="!") or (j-1>=0 and mapa[i][j-1]=="!")):
                mapa[i][j]="*"        
                for linha in mapa:
                    print(" ".join(linha))
                print()
                print("O robo encontrou a saida!")
                break
                
            else:
                print("Caminho nao encontrado")
                break
        for linha in mapa:
            print(" ".join(linha))
        print()