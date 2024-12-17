from Paciente import Paciente
from Medico import Medico
from Consulta import Consulta
medicos = []
pacientes = []
consultas = []

def adicionarMedico():
    nome = input("Insira o nome do Medico: ")
    Sexo = input("Insira o sexo do Medico: ")
    endereco = input("Insira o endereco do Medico: ")
    cpf = input("Insira o cpf do Medico: ")
    telefone = int(input("Insira o telefone do Medico: "))
    identidade = int(input("Insira a identidade do Medico: "))
    Crm = int(input("Insira o crm do Medico: "))
    especialidade = input("Insira a especialidade do Medico: ")
    m = Medico(nome, Sexo, endereco, cpf, telefone, identidade, Crm, especialidade)
    medicos.append(m)

def procurarPacientes(novonome):
    for paciente in pacientes:
        if paciente.nome == novonome:
            return paciente
    else:
        print("Não encontrado")
        return None

def cadastrarConsulta():
    if not pacientes:
        print("Não existem pacientes cadastrados")
        return

    for paciente in pacientes:
        print(paciente.nome)

    novonome = input("Qual paciente vai fazer a consulta? ")
    p = procurarPacientes(novonome)

    if p is not None:
        relato = input("Digite o relato do paciente: ")
        medicamentos = input("Digite os medicamentos: ")
        consulta = Consulta(p, relato, medicamentos)
        consultas.append(consulta)
    else:
        print("Não existe pacientes cadastrados")

def procurarConsultas(novonome):
    for i in consultas:
        if i.p.nome == novonome:
            return i
    else:
        print("Não encontrado")
        return None

def cancelarConsulta():
    if not consultas:
        print("Não existe consultas")
    else:
        for i in consultas:
            print("\n")
            i.p.imprimirDados()
            print("Relato: " + i.relato)
            print("Medicamentos: " + i.medicamentos)
        novonome = input("Qual nome do paciente da consulta: ")
        consulta = procurarConsultas(novonome)
        if consulta is not None:
            for i in consultas:
                if i == consulta:
                    consultas.remove(i)
                    print("Consulta cancelada com sucesso")
                    return

def imprimirConsultasPaciente():
    print("Digite o nome do Paciente para achar a consulta:")
    print("Pacientes:")
    for i in pacientes:
        print(i.nome)
    novonome = input("Nome do Paciente: ")
    i = procurarConsultas(novonome)
    if i is not None:
        i.p.imprimirDados()
        print("Relato: " + i.relato)
        print("Medicamentos: " + i.medicamentos)

def imprimirTodasConsultas():
    print("Todas as consultas:")
    for i in consultas:
        print("\n")
        i.imprimirDados()
        print("Relato: " + i.relato)
        print("Medicamentos: " + i.medicamentos)

def cadastrarPacientes():
    nome = input("Insira o nome do Paciente: ")
    Sexo = input("Insira o sexo do Paciente: ")
    endereco = input("Insira o endereco do Paciente: ")
    cpf = input("Insira o cpf do Paciente: ")
    telefone = int(input("Insira o telefone do Paciente: "))
    identidade = int(input("Insira a identidade do Paciente: "))
    medicacaocontinua = input("Insira a medicacao do paciente: ")
    pacientes.append(Paciente(nome, Sexo, endereco, cpf, telefone, identidade, medicacaocontinua))

def imprimirPacientes():
    for paciente in pacientes:
        print("\n")
        paciente.imprimirDados()
        print("Medicação: " + paciente.medicacaocontinua)

def removerPaciente():
    if not pacientes:
        print("Nenhum paciente cadastrado")
        return
    for paciente in pacientes:
        print(paciente.nome)
    novonome = input("Qual paciente deseja remover: ")
    for paciente in pacientes:
        if paciente.nome == novonome:
            pacientes.remove(paciente)
            print("Paciente removido com sucesso")
            return

    print("Paciente não encontrado.")
