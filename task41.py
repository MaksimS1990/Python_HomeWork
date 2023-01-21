import os
os.system('cls')

def cls():
    os.system('cls')
cls()    

MainFile = 'tel.txt'

# def ConvertToString(listUser):
#     stringUser = ''
#     for i in range(0, len(listUser)-1):
#         stringUser = stringUser + listUser[i] + ', '
#     stringUser = stringUser + listUser[-1]
#     return stringUser

# def ConvertToList(stringUser):
#     stringUser = stringUser.replace('\n','')
#     return list(stringUser.split(', '))

def writeFile(file_name):
    with open (file_name, 'a') as data:
        data.writelines(input("Введите данные нового контакта: ") + '\n')

def readFile(file_name):                                          # функция чтения из файла 
    with open (file_name, 'r') as data: 
        line = data.readlines()

    for i in line:
            i = line.index(i)
            print(f'{i+1}. {line[i].strip()}')


def findUsers(file_name):
    with open (file_name, 'r') as data:                           # ищем по индексу (Имя -> данные контакта)
        cancel = input("Введите Ф/И/0/ или номер искомого контакта: ")
        for user in data:
                if cancel in user:
                    print(user)
        
    
def DeleteUsers(file_name):                                       # удаляем контакт по Ф/И/О либо номеру телефона
    with open(file_name, 'r') as data:
        line = data.readlines()
        
     
    cancel = int(input("Введите порядковый номер контакта для удаления: "))
    del line[cancel - 1]
    
    with open (file_name, 'w') as data:
        for i in line:
            data.write(i)

def writingNewNumber(file_name):
    with open (file_name, 'r') as data: 
        line = data.readlines()
    cancel = int(input("Введите порядковый номер абонента для изменения номера телефона: "))
    result = line[cancel - 1].split()
    new_data = input("Введите новое значение: ")
    result[3] = new_data
    line[cancel - 1] = ' '.join(result) + '\n'
    with open (file_name, 'w', encoding = 'utf-8') as data:
        for i in line:
            data.write(i)

# def fileOverwritting(Kraken):
#      with open (MainFile, 'w') as data:
#         data.writelines(Kraken)
#         Kraken = MainFile
#         return MainFile
# print(MainFile)
    
# writeFile(MainFile)
# readFile(MainFile)
# findUsers(MainFile)
# DeleteUsers(MainFile)
# readFile(MainFile)
# writingNewNumber(MainFile)
# MainMenu()
# PhoneBookMenu()
# fileOverwritting(readFile())
cls()
def MainMenu():

    print("   Телефонный справочник   \n"
      "       Главное меню        \n"
     "1 - Показать все записи\n"
     "2 - Найти запись по ФИО или номеру телефона\n"
     "3 - Добавить новый контакт\n"
     "4 - Удалить контакт\n"
     "5 - Изменить данные контакта\n"
     "0 - Выход")

    UserChoise = int(input("Выберите номер команды, которую хотите выполнить: "))

    while True:

        if UserChoise == 1:
            print()
            readFile(MainFile),print()
            MainMenu()
            break

        if UserChoise == 2:
            print()
            findUsers(MainFile), print()
            MainMenu()
            break

        if UserChoise == 3:
            print()
            writeFile(MainFile), print()
            MainMenu()
            break

        if UserChoise == 4:
            print()
            DeleteUsers(MainFile), print()
            MainMenu()
            break

        if UserChoise == 5:
            print()
            writingNewNumber(MainFile), print()
            print()
            MainMenu()
            break

        if UserChoise == 0:
            print()
            MainMenu(), print()
            print()
            break

        else:
            print()
            MainMenu(), print()
            print()
            break

MainMenu()