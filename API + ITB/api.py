import requests
import json
import collections

client_id = 'ce22dcdbd89f82a6ab0d'
client_secret = '486e0eed14ca47eded8846285567ec58'

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбираем ответ сервера
j = json.loads(r.text)

# достаем токен
token = j["token"]

# str_od_id_art = "4d8b92b34eb68a1b2c0003f4 537def3c139b21353f0006a6 4e2ed576477cc70001006f99"

str_od_id_art = "4f958feaaa701d0001000e3e \
4d8b92a44eb68a1b2c000328 \
4e96f70a6e481d0001002c73 \
5324d4657622dd48700001e3 \
4f86f41a24907b0001000d46 \
506b33134466170002000254 \
519258cc9e628509c40000d7 \
511294005c85615a61000082 \
53393f7a275b2458b10004a9 \
506255b93111cc0002000986 \
4f552b2e3b55524170000002 \
53d8b30672616913c7e40200 \
529c4b09139b21cdd4000250 \
554a78d87261692b00710400 \
5074b71827ef8d00020002bd"
lst = list(str_od_id_art.split(" "))

# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token" : token}

dct = {}

for id_artist in lst:
    r = requests.get(f"https://api.artsy.net/api/artists/{id_artist}", headers=headers)
    # r.encoding = 'utf-8'
    j = json.loads(r.text)
    name_artist = j['name']
    birthday = j['birthday']
    dct[name_artist] = birthday

tuple_artist = sorted(dct.items(), key=lambda x: (x[1], x[0]))
for artist in tuple_artist:
    full_name_art = artist[0].split(' ')
    # print(full_name_art)
    name = full_name_art.pop(0)
    surname = full_name_art[::-1]
    # print(*surname)
    print(*surname, name)

print('--------------2nd try-------------')


client_id = 'db311cfe37ec4bc74a61'
client_secret = 'ba1d22427d386b0b79ce4403c063b2ec'

r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })
j = json.loads(r.text)
token = j["token"]

artists = []

with open('dataset_24476_4.txt') as file:
    for artist_id in file:
        artist_id = artist_id.strip()
        url = 'https://api.artsy.net/api/artists/{}'.format(artist_id)
        params = {'xapp_token': token}
        resp = requests.get(url, params=params).text
        data = json.loads(resp)
        artists.append({'name': data['sortable_name'], 'birthday': data['birthday']})

for artist in sorted(artists, key=lambda x: (x['birthday'], x['name'])):
    print(artist['name'])


