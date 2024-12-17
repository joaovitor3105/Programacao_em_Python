from Paciente import Paciente
from Medico import Medico
from Consulta import Consulta
from Consultorio import (
    adicionarMedico,
    procurarPacientes,
    cadastrarConsulta,
    procurarConsultas,
    cancelarConsulta,
    imprimirConsultasPaciente,
    imprimirTodasConsultas,
    cadastrarPacientes,
    imprimirPacientes,
    removerPaciente
)

pacientes = []
consultas = []

while True:
        print("\n---- MENU ----")
        print("1. Cadastrar Paciente")
        print("2. Cadastrar Médico")
        print("3. Cadastrar Consulta")
        print("4. Cancelar Consulta")
        print("5. Imprimir Consultas de um Paciente")
        print("6. Imprimir Todas as Consultas")
        print("7. Imprimir Lista de Pacientes")
        print("8. Remover Paciente")
        print("0. Sair")
        
        opcao = input("\nEscolha uma opção: ")
        
        match opcao:
            case "1":
                cadastrarPacientes()
            case "2":
                adicionarMedico()
            case "3":
                cadastrarConsulta()
            case "4":
                cancelarConsulta()
            case "5":
                imprimirConsultasPaciente()
            case "6":
                imprimirTodasConsultas()
            case "7":
                imprimirPacientes()
            case "8":
                removerPaciente()
            case "0":
                print("\nSaindo do programa...")
                break
            case _:
                print("\nOpção inválida. Tente novamente.")


