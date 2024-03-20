from datetime import date


def search(name, data):
    for row in data:
        if row['artist_name'] == name:
            return row['track_name']
    return ''

dn = date(2023, 5, 12)
data = []

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

name = input()
while name != '0':
    res = search(name, data)
    if res:
        print(f'У {name} найдена песня: {res}')
    else:
        print('К сожалению, ничего не удалось найти')
    name = input()
