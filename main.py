import os
import time


patients = []
doctors = []
appointments = []


def createUser(name, age, gender, tel, address):
    newUser = {
        "name": name,
        "age": age,
        "gender": gender,
        "tel": tel,
        "address": address,
        "createdAt": time.time(),
        "updatedAt": time.time(),
    }
    return newUser


def askForInfo(type):
    name = input("Informe o nome do " + type + ": ")
    age = int(input("Informe a idade do " + type + ": "))
    gender = input("Informe o gênero do " + type + ": ")
    tel = input("Informe o número de telefone do " + type + ": ")
    address = input("Informe o endereço do " + type + ": ")
    newEntity = createUser(name, age, gender, tel, address)
    return newEntity


def RemoveAppointment():
    if len(appointments) == 0:
        print("Nenhuma consulta cadastrada.")
        return

    print("Consultas cadastradas:")
    for i, appointment in enumerate(appointments):
        print(
            f"{i + 1}. Paciente: {appointment['patientName']}, Médico: {appointment['doctorName']}, Data: {appointment['date']}"
        )

    index = int(input("Informe o número da consulta que deseja excluir: ")) - 1

    if 0 <= index < len(appointments):
        removed_appointment = appointments.pop(index)
        print(
            f"Consulta do paciente {removed_appointment['patientName']} com o médico {removed_appointment['doctorName']} removida com sucesso."
        )

    else:
        print("Número inválido. Nenhuma consulta foi removida.")
    return

def RemovePatients():
    if len(patients) == 0:
        print("Nenhum usuário cadastrado.")
        return

    print("Usuários cadastrados:")
    for i, patient in enumerate(patients):
        print(
            f"{i + 1}. Nome: {patient['name']}, Idade: {patient['age']}, Gênero: {patient['gender']}"
        )

    index = int(input("Informe o número do usuário que deseja excluir: ")) - 1

    if 0 <= index < len(patients):
        removed_patients = patients.pop(index)
        print(f"Removido o usuário: {removed_patients['name']}.")
    else:
        print("Número inválido. Nenhum usuário foi removido.")
    return


def RemoveDoctor():
    if len(doctors) == 0:
        print("Nenhum médico cadastrado.")
        return

    print("Médicos cadastrados:")
    for i, doctor in enumerate(doctors):
        print(
            f"{i + 1}. Nome: {doctor['name']}, Idade: {doctor['age']}, Gênero: {doctor['gender']}"
        )
    index = int(input("Informe o número do medico que deseja excluir: ")) - 1

    if 0 <= index < len(doctors):
        removed_doctor = doctors.pop(index)
        print(f"Removido o médico {removed_doctor['name']}.")

    else:
        print("Número inválido. Nenhum médico foi removido.")
    return


def appointmentsActionsMenu():
    op = 0
    while op != 5:
        print(
            "\n\n====== SISTEMA HOSPITALAR - IFRS ======\n"
            "====== MENU DE CONSULTAS ======\n\n"
            "- 1 Cadastrar nova consulta\n"
            "- 2 Listar Consultas\n"
            "- 3 Atualizar Consultas\n"
            "- 4 Excluir Consulta\n"
            "- 5 Retornar ao menu principal\n"
            ""
        )
        op = int(input("Selecione uma opção: "))

        if op == 1:
            # TODO
            print("")
        elif op == 2:
            # TODO
            print("")
        elif op == 3:
            # TODO
            print("")
        elif op == 4:
            print("Acessando exclusão de consulta...")
            RemoveAppointment()
        elif op == 5:
            return


def doctorActionsMenu():
    op = ""

    while op != 5:
        print(
            "\n\n====== SISTEMA HOSPITALAR - IFRS ======\n"
            "====== MENU DE MÉDICOS ======\n\n"
            "- 1 Cadastrar novo médico\n"
            "- 2 Listar médicos\n"
            "- 3 Atualizar médico\n"
            "- 4 Excluir médico\n"
            "- 5 Retornar ao menu principal\n"
            ""
        )
        op = int(input("Selecione uma opção: "))

        if op == 1:
            newDoctor = askForInfo("médico")
            doctors.append(newDoctor)
        elif op == 2:
            # TODO
            print("")
        elif op == 3:
            # TODO
            print("")
        elif op == 4:
            print("Acessando o menu de exclusão de médicos")
            RemoveDoctor()
        elif op == 5:
            return


def pacientActionsMenu():
    op = ""

    while op != 5:
        print(
            "\n\n====== SISTEMA HOSPITALAR - IFRS ======\n"
            "====== MENU DE PACIENTES ======\n\n"
            "- 1 Cadastrar novo paciente\n"
            "- 2 Listar pacientes\n"
            "- 3 Atualizar paciente\n"
            "- 4 Excluir paciente\n"
            "- 5 Retornar ao menu principal\n"
            ""
        )
        op = int(input("Selecione uma opção: "))

        if op == 1:
            newPatient = askForInfo("paciente")
            patients.append(newPatient)
        elif op == 2:
            # TODO
            print("")
        elif op == 3:
            # TODO
            print("")
        elif op == 4:
            # TODO
            RemovePatients()
            print("")
        elif op == 5:
            return


def mainMenu():
    op = ""

    while op != 4:
        os.system("cls" if os.name == "nt" else "clear")
        print(
            "\n\n====== SISTEMA HOSPITALAR - IFRS ======\n"
            "====== MENU PRINCIPAL ======\n\n"
            "- 1 Ações para pacientes\n"
            "- 2 Ações para médicos\n"
            "- 3 Ações para consulta\n"
            "- 4 Sair\n"
            ""
        )
        op = int(input("Selecione uma opção: "))

        if op == 1:
            pacientActionsMenu()
        elif op == 2:
            doctorActionsMenu()
        elif op == 3:
            appointmentsActionsMenu()
        elif op == 4:
            print("Saindo...")


mainMenu()
 