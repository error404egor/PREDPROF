from datetime import date



def search(name: str, data: list) -> str:
    '''функция поиска песни артиста. 
    Если найдена песня артиста, то возвращает название найденной песни
    Если нет, то возвращает пустую строку'''
    for row in data:
        if row['artist_name'] == name:
            return row['track_name']
    return ''


# объявление списка, в котором будем хранить данные
data = []

# Считываем данные из файла в список. Получаем список словарей data
# [{streams: int, artist_name: str, track_name: str, date: date}, ...]
with open('songs.csv') as f:
    headers = f.readline().strip().split(";")
    headers[0] = 'streams'
    for line in f.readlines():
        if line == '\n' or line == '':
            break
        lst = line.strip().split(';')
        lst[0] = int(lst[0])
        lst[3] = date(*list(map(int, lst[3].split('.')))[::-1])
        d = {headers[i]: lst[i] for i in range(len(headers))}
        data.append(d)

# считываем имя интересующего артиста
name = input()
# пока не считали 0
while name != '0':
    # применяем ф-цию поиска
    res = search(name, data)
    # выводим результат
    if res:
        print(f'У {name} найдена песня: {res}')
    else:
        print('К сожалению, ничего не удалось найти')
    # вводим новое имя
    name = input()
