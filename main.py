from pymongo import MongoClient
import os
import time

client = MongoClient("mongodb+srv://mongo:hP64nnoip1KRx7Wv@cluster0.zjkjvh2.mongodb.net/?appName=cluster0")
db = client["hospital_ifrs"]

users_col = db["users"]
patients_col = db["patients"]
doctors_col = db["doctors"]
appointments_col = db["appointments"]

def createUser(name, age, gender, tel, address):
    return {
        "name": name,
        "age": age,
        "gender": gender,
        "tel": tel,
        "address": address,
        "createdAt": time.time(),
        "updatedAt": time.time()
    }


def createAppointment(patientName, doctorName, date):
    return {
        "patientName": patientName,
        "doctorName": doctorName,
        "date": date,
        "createdAt": time.time(),
        "updatedAt": time.time()
    }


def listPatients():
    print("\nPacientes cadastrados:")
    for i, p in enumerate(patients_col.find(), start=1):
        print(f"{i}. Nome: {p['name']} | Idade: {p['age']} | Gênero: {p['gender']}")


def listDoctors():
    print("\nMédicos cadastrados:")
    for i, d in enumerate(doctors_col.find(), start=1):
        print(f"{i}. Nome: {d['name']} | Idade: {d['age']} | Gênero: {d['gender']}")


def listAppointments():
    print("\nConsultas cadastradas:")
    for i, a in enumerate(appointments_col.find(), start=1):
        print(f"{i}. Paciente: {a['patientName']} | Médico: {a['doctorName']} | Data: {a['date']}")


def askForInfo(tipo):
    os.system("cls" if os.name == "nt" else "clear")

    name = input(f"Informe o nome do {tipo}: ")
    age = int(input(f"Informe a idade do {tipo}: "))
    gender = input(f"Informe o gênero do {tipo}: ")
    tel = input(f"Informe o telefone do {tipo}: ")
    address = input(f"Informe o endereço do {tipo}: ")

    return createUser(name, age, gender, tel, address)


def askForAppointmentInfo():
    print('hello')
    os.system("cls" if os.name == "nt" else "clear")

    if patients_col.count_documents({}) == 0:
        print("Nenhum paciente cadastrado.")
        input("ENTER para voltar")
        return None

    if doctors_col.count_documents({}) == 0:
        print("Nenhum médico cadastrado.")
        input("ENTER para voltar")
        return None

    listPatients()
    patientName = input("\nDigite o nome do paciente: ")

    if not patients_col.find_one({"name": patientName}):
        print("Paciente não encontrado.")
        input("ENTER para voltar")
        return None

    listDoctors()
    doctorName = input("\nDigite o nome do médico: ")

    if not doctors_col.find_one({"name": doctorName}):
        print("Médico não encontrado.")
        input("ENTER para voltar")
        return None

    date = input("\nDigite a data da consulta (dd/mm/yyyy): ")

    return createAppointment(patientName, doctorName, date)


def RemovePatients():
    listPatients()
    name = input("\nDigite o nome do paciente para remover: ")
    patients_col.delete_one({"name": name})
    users_col.delete_one({"name": name})
    input("Paciente removido. ENTER para continuar")


def RemoveDoctor():
    listDoctors()
    name = input("\nDigite o nome do médico para remover: ")
    doctors_col.delete_one({"name": name})
    users_col.delete_one({"name": name})
    input("Médico removido. ENTER para continuar")


def RemoveAppointment():
    listAppointments()
    date = input("\nDigite a data da consulta para remover: ")
    appointments_col.delete_one({"date": date})
    input("Consulta removida. ENTER para continuar")

def updateUser(collection, userType):
    if collection.count_documents({}) == 0:
        print(f"Nenhum {userType} cadastrado.")
        input("ENTER para voltar")
        return

    os.system("cls" if os.name == "nt" else "clear")
    print(f"Lista de {userType}s:\n")

    users = list(collection.find())
    for i, u in enumerate(users, start=1):
        print(f"{i}. Nome: {u['name']} | Idade: {u['age']} | Gênero: {u['gender']}")

    index = int(input(f"\nDigite o número do {userType} para atualizar: ")) - 1

    if index < 0 or index >= len(users):
        print("Opção inválida.")
        input("ENTER para voltar")
        return

    user = users[index]

    print("\nDeixe em branco para manter o valor atual.\n")

    name = input(f"Nome ({user['name']}): ")
    age = input(f"Idade ({user['age']}): ")
    gender = input(f"Gênero ({user['gender']}): ")
    tel = input(f"Telefone ({user['tel']}): ")
    address = input(f"Endereço ({user['address']}): ")

    update_data = {}

    if name:
        update_data["name"] = name
    if age:
        update_data["age"] = int(age)
    if gender:
        update_data["gender"] = gender
    if tel:
        update_data["tel"] = tel
    if address:
        update_data["address"] = address

    if update_data:
        update_data["updatedAt"] = time.time()
        collection.update_one(
            {"_id": user["_id"]},
            {"$set": update_data}
        )

        users_col.update_one(
            {"_id": user["_id"]},
            {"$set": update_data}
        )

        print(f"\n{userType.capitalize()} atualizado com sucesso!")

    input("ENTER para voltar")

def pacientActionsMenu():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("""
====== MENU DE PACIENTES ======

1 - Cadastrar paciente
2 - Listar pacientes
3 - Atualizar paciente
4 - Excluir paciente
5 - Voltar
""")
        op = int(input("Selecione uma opção: "))

        if op == 1:
            p = askForInfo("paciente")
            patients_col.insert_one(p)
            users_col.insert_one(p)
        elif op == 2:
            listPatients()
            input("ENTER para voltar")
        elif op == 3:
            updateUser(patients_col, "paciente")
        elif op == 4:
            RemovePatients()
        elif op == 5:
            return


def doctorActionsMenu():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("""
====== MENU DE MÉDICOS ======

1 - Cadastrar médico
2 - Listar médicos
3 - Atualizar médico
4 - Excluir médico
5 - Voltar
""")
        op = int(input("Selecione uma opção: "))

        if op == 1:
            d = askForInfo("médico")
            doctors_col.insert_one(d)
            users_col.insert_one(d)
        elif op == 2:
            listDoctors()
            input("ENTER para voltar")
        elif op == 3:
            updateUser(doctors_col, "médico")
        elif op == 4:
            RemoveDoctor()
        elif op == 5:
            return


def appointmentsActionsMenu():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("""
====== MENU DE CONSULTAS ======

1 - Cadastrar consulta
2 - Listar consultas
3 - Excluir consulta
4 - Voltar
""")
        op = int(input("Selecione uma opção: "))

        if op == 1:
            a = askForAppointmentInfo()
            if a:
                appointments_col.insert_one(a)
        elif op == 2:
            listAppointments()
            input("ENTER para voltar")
        elif op == 3:
            RemoveAppointment()
        elif op == 4:
            return


def mainMenu():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("""
====== SISTEMA HOSPITALAR - IFRS ======

1 - Ações para pacientes
2 - Ações para médicos
3 - Ações para consultas
4 - Sair
""")
        op = int(input("Selecione uma opção: "))

        if op == 1:
            pacientActionsMenu()
        elif op == 2:
            doctorActionsMenu()
        elif op == 3:
            appointmentsActionsMenu()
        elif op == 4:
            print("Saindo...")
            break


mainMenu()