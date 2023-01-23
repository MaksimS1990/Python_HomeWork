def read_data_from_file(name):
    result = []
    with open(name, 'r', encoding='utf8') as datafile:
        for line in datafile:
            result.append(line.strip('\n').split(','))
        return result

def save_data_to_file(name, data_list):
    with open(name, 'a', encoding='utf8') as datafile:
        datafile.write(data_list +'\n')


def print_bus():
    return read_data_from_file('bus.txt')

def add_bus():
    save_data_to_file('bus.txt', input("Введите параметры автобуса: "))
    
def print_driver():
    return read_data_from_file('driver.txt')

def add_driver():
    save_data_to_file('driver.txt', input("Введите водителя: "))

def print_route():
    return read_data_from_file('route.txt')

def add_route():
    save_data_to_file('route.txt', input("Введите маршрут: "))

def DeleteInfo(name):                                                     # удаляем контакт по Ф/И/О либо номеру телефона
    with open(name, 'r') as data:
        line = data.readlines()
    cancel = int(input("Введите порядковый номер для удаления: "))
    del line[cancel - 1]
    with open (name, 'w') as data:
        for i in line:
            data.write(i)


