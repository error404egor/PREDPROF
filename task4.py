from datetime import date


RUSSIAN_LETTERS = 'йцукенгшщзхъёэждлорпавыфячсмитьбю'

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

russian_artists = set()

foreign_artists = set()
 
for row in data:
    if any([(letter in RUSSIAN_LETTERS) for letter in row['artist_name']]):
        russian_artists.add(row['artist_name'])
    else:
        foreign_artists.add(row['artist_name'])

russian_artists = list(russian_artists)

foreign_artists = list(foreign_artists)

print(f'Количество российских исполнителей: {len(russian_artists)} ')
print(f'Количество иностранных исполнителей: {len(foreign_artists)} ')

with open('russian_artists.txt', 'w') as f:
    f.write('\n'.join(russian_artists))

with open('foreign_artists.txt', 'w') as f:
    f.write('\n'.join(foreign_artists))



