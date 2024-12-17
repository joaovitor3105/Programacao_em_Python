from Paciente import Paciente
from Medico import Medico
from Consulta import Consulta
medicos = []
pacientes = []
consultas = []
def adicionarMedico():
    nome = input("\nInsira o nome do Medico:")
    Sexo = input("\nInsira o sexo do Medico:")
    endereco = input("\nInsira o endereco do Medico:")
    cpf = input("\nInsira o cpf do Medico:")
    telefone = int(input("\nInsira o telefone do Medico:"))
    identidade= int(input("\nInsira a identidade do Medico:"))
    Crm = int(input("\nInsira o crm do Medico:"))
    especialidade = input("\nInsira a especialidade do Medico:")
    m = Medico(nome,Sexo,endereco,cpf,telefone,identidade,Crm,especialidade)
    medicos.append(m)
    
def procurarPacientes(novonome):
    for paciente in pacientes :
       if paciente.nome == novonome:
           return paciente
    else :
        print("Não encontrado")
        return None
    
def cadastrarConsulta():
    if not pacientes:
        print("\nNão existem pacientes cadastrados")
        return
    
    for paciente in pacientes:
        print(paciente.nome)
    
    novonome = input("\nQual paciente vai fazer a consulta?")
    p = procurarPacientes(novonome)
    
    if p is not None:    
        relato = input("\nDigite o relato do paciente:")
        medicamentos = input("\nDigite os medicamentos:")
        consulta = Consulta(p, relato, medicamentos)
        consultas.append(consulta)
    else :
        print("\nNão existe pacientes cadastrados")
 
def procurarConsultas(novonome):
    for i in consultas :
       if i.p.nome == novonome:
           return i
    else :
        print("\nNão encontrado")
        return None
           
def cancelarConsulta():
    if (consultas == []):
        print("\nNão existe consultas")
    else :
        
        for i in consultas:
            print("\n\n")
            i.imprimirDados()
            print("\n"+i.relato)
            print("\n"+i.medicamentos)
        novonome=input("\nQual nome do paciente da consulta")
        consulta=procurarConsultas(novonome)
        if consulta!= None:
            for i in consultas :
                if i == consulta:
                    consultas.remove(i)
        
def imprimirConsultasPaciente():
    print("\ndigite o nome do Paciente par achar a consulta: \n Pacientes:")  
    for i in pacientes:
        print('\n')
        print(i.nome)    
    novonome=input()
    i=procurarConsultas(novonome)
    if i != None:
        i.imprimirDados()
        print("\n"+i.relato)
        print("\n"+i.medicamentos)

def imprimirTodasConsultas():
    print("\nTodas as consultas:")
    for i in consultas:
            print("\n\n")
            i.imprimirDados()
            print("\n"+i.relato)
            print("\n"+i.medicamentos)
            
def cadastrarPacientes():
    nome = input("\nInsira o nome do Paciente:")
    Sexo = input("\nInsira o sexo do Paciente:")
    endereco = input("\nInsira o endereco do Paciente:")
    cpf = input("\nInsira o cpf do Paciente:")
    telefone = int(input("\nInsira o telefone do Paciente:"))
    identidade= int(input("\nInsira a identidade do Paciente:"))
    medicacaocontinua=input("\nInsira a medicacao do paciente:")
    pacientes.append(Paciente(nome,Sexo,endereco,cpf,telefone,identidade,medicacaocontinua))
    
def imprimirPacientes():
    for paciente in pacientes:
            print("\n")
            paciente.imprimirDados()
            print("\nMedicação:")
            print(paciente.medicacaocontinua)
       
def removerPaciente():
    if not pacientes:
        print("\nNenhum paciente cadastrado")
        return
    for paciente in pacientes:
        print(paciente.nome)
    novonome = input("\nQual paciente deseja remover: ")
    for paciente in pacientes:
        if paciente.nome == novonome:
            pacientes.remove(paciente)
            return
    
    print("\nPaciente não encontrado.")
    
        
         
            
        
            
    

    
    

















    

