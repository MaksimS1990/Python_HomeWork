fileName = 'tel.txt'

def writeFile(fileName):                               # функция записи в файл
    with open (fileName, 'a') as data:
        data.writelines('\n' + input("Введите данные контакта: ") + '\n')
    
def readFile(fileName):                                # функция чтения из файла
    result = []                                        # создаем пустой список
    with open (fileName, 'r+') as data:
        for line in data:                              # бежим по списку списков
            result.append(line.split())                # преобразуем строку в список
        return result

def findUsers(userlist):                              # ищем по индексу (Имя -> данные контакта)
    cancel = input("Введите Ф/И/0/ номер: ")
    for user in userlist:
        if cancel in user:
            print(user)
    return userlist

# def PhoneNumberReplacement(userlist):
    # cancel = input("Введите Ф/И/0/ номер: ")
    # for user in userlist:
        # if cancel in user:
            # cancel[3] =  input("Введите новый номер телефона: ")
    # return userlist

def DeleteUsers(userlist):                            # удаляем контакт по Ф/И/О либо номеру телефона
    cancel = input("Введите данные контакта для удаления: ")
    for user in userlist:
        if cancel in user:
            userlist.remove(user)                     # remove - функция удаления списка
            print(userlist)
    return userlist

def overwritingFile(userlist):
    with open (fileName, 'w') as data:
        for user in userlist:
            data.writelines(f"\n {user}")
print(fileName)

writeFile(fileName)
print(readFile(fileName))
findUsers(readFile(fileName))
PhoneNumberReplacement(readFile(fileName))
overwritingFile(DeleteUsers(readFile(fileName)))