MainFile = 'tel.txt'

def ConvertToString(listUser):
    stringUser = ''
    for i in range(0, len(listUser)-1):
        stringUser = stringUser + listUser[i] + ', '
    stringUser = stringUser + listUser[-1]
    return stringUser

def ConvertToList(stringUser):
    stringUser = stringUser.replace('\n','')
    return list(stringUser.split(', '))

def writeFile():
    with open (MainFile, 'a') as data:
        data.writelines(input("Введите данные нового контакта: ") + '\n')

def readFile():                                          # функция чтения из файла 
    result = []                                                  # создаем пустой список 
    with open (MainFile, 'r+') as data: 
        for line in data:                                        # бежим по списку списков 
            result.append(ConvertToList(line))                   # преобразуем строку в список
        return result

def findUsers(result):                                           # ищем по индексу (Имя -> данные контакта)
    cancel = input("Введите Ф/И/0/ или номер искомого контакта: ")
    for user in result:
            if cancel in user:
                print(user)
    return user
    
def DeleteUsers(fileName):                                       # удаляем контакт по Ф/И/О либо номеру телефона
    cancel = int(input("Введите номер контакта для удаления: "))
    fileName.pop(cancel-1)                                       # remove - функция удаления списка
    print(fileName)
    return fileName

def writingNewNumber(result):
    cancel = input("Введите Ф/И/0/ или номер искомого контакта для смены номера: ")
    for user in result:
            if cancel in user:
                user[3] = (input("Введите новый номер: "))
                print(user)
                print(result)
    return result

def fileOverwritting(Kraken):
     with open (MainFile, 'w') as data:
        data.writelines(Kraken + '\n')

# writeFile(fileName)
# print(readFile(fileName))
# print(findUsers(readFile(fileName)))
# DeleteUsers(readFile(fileName))
writingNewNumber(readFile())
fileOverwritting(readFile())