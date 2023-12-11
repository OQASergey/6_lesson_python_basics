# while - цикл с прерыванием условием
import random

rn = 7
un = random.randint(0,10)

while un != rn:
    print(f'User_Number ({un}) не равен {rn}')
    un = random.randint(0, 10)

i = 10
rn = 5

while i != rn:
    print(f'Сейчас i = {i}')
    i -= 1

# for ====== - для списков и словарей
print('======')

TRPG = [{"id":1, "title":"Apocalypse World"},
        {"id":2, "title":"Dungeon World"},
        {"id":3, "title":"Urban Shadows"},
        {"id":4, "title":"MonsterHearts"},
        {"id":5, "title":"MASKs"},
        {"id":6, "title":"Glitter Heart"},
        {"id":7, "title":"The veil"},
        {"id":8, "title":"SCUB"},
        {"id":9, "title":"Hum4n1ty Zer0"},
        {"id":10, "title":"Грань Вселенной"}]

rn = random.randint(1,10)

for games in TRPG:
    if games["id"] == rn:
        print(games['title'])

print('=====')

a = {
    "key":1,
    "title":"pbta",
    "type":"hobby",
    "style":"storygame"
}

for words in a:
    print(words) #- ключи

for key in a.keys():
    print(key)

for value in a.values():
    print(value)

print('===')

for (key, value) in a.items():
    print(key, value)

