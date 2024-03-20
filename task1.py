from datetime import date

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



for row in data:
    if row['streams'] == 0:
        td = dn - row['date']
        row['streams'] = round(abs(td.days) / 
                          (len(row['artist_name']) + len(row['track_name'])) * 10000)



with open('songs_new.csv', 'w') as f:
    s = ';'.join(headers) + '\n'
    
    for row in data:
        row = [row[key] for key in headers]
        row[0] = str(row[0])
        row[3] = '.'.join(str(row[3]).split('-')[::-1])
        s += ';'.join(row) + '\n'
    
    f.write(s)