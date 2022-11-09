# length методы
list = [1, 2, 3, 4, 5]
print(len(list))

dict = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}
print(len(dict))

tup = (1, 2, 3, 4, 5)
print(len(tup))

set = {1, 2, 3, 4, 5}
length = len(set)
print(length)

#clear методы
list = [1,2,3,4,5]
element = list.clear()
print(element)

dict = {"one":1,"two":2,"three":3,"four":4,"five":5}
element = dict.clear()
print(element)

set = {1,2,3,4,5}
set.clear()
print(set)

tup = (1,2,3,4,5)
del tup

#элементті өшіру
list = [1,2,3,4,5]
print(list.remove(3))

set = {1, 2, 3, 4, 5, 6}
print(set.remove(3))

dict = {"one":1,"two":2,"three":3,"four":4,"five":5}
dict.pop("two") #немесе del методымен

#кортежде элемент өшіруге болмайды!


#Элементті қосу
list = [1,2,3,4,5]
list.append(6) #append  функциясымен

dict = {"one":1,"two":2,"three":3,"four":4,"five":5}
dict["six"] = 6 #кілт арқылы

tup = (1,2,3,4,5)
tup2 = (6,) #екінші кортеж құру арқылы

set = {1,2,3,4,5}
set.add(6)#add функциясымен

print(list)
print(dict)
print(tup + tup2)
print(set)

#index методы
print(list.index(2))
print(tup.index(2))

dict = {"one":1,"two":2,"three":3,"four":4,"five":5}
keys = list(dict.keys())
print(keys[1])
#set - те индекс методы жоқ

#count методы
print(list.count())
print(tup.count(2))
print(dict.values())    #print(dict.items())

#reverse методы
list = [1, 2, 3, 4, 5]
list2 = list.reverse()
print(list2)
list = [1,2,3,4,5]
print(list(reversed(list)))

from collections import OrderedDict
dict = {"one":1,"two":2,"three":3,"four":4,"five":5}
res = OrderedDict(reversed(list(dict.items())))
print(str(res))

def Reverse(tuples):
    new_tup = tuples[::-1]
    return new_tup
tuples = (1,2,3,4,5)
print(Reverse(tuples))


#Резюме
print("                      Резюме            ")

# info - Кортеж
info = (
    ("Наби", "Айман", "Серікқызы"),
)
for item in info:
    lastname, firstname, fname = item
    print("\nФ.И.О : " + lastname, firstname, fname)

# experience  - set
company = {"Dar IT", "One Dev"}
vacancy = {"Python разработчик", "Middle Python разработчик"}
experience = company.union(vacancy)
print("Опыт работы : " + str(experience))

# obrazovanie = dict
study = {
    'ВУЗ': 'Satbayev University',
    'Специальность ': 'Computer Science',
    'GPA': '3.3',
    'Год окончания ': '2023'
}
for x, y in study.items():
    print(x + ' : ' + y)

# skills - кортеж
skills = ('Языки программирования C++, Python', ',', 'Django', ',', 'OS Linux', 'HTML,CSS')
skills = ''.join(skills)
print("Основные навыки : " + skills)

info = []
info.append("Номер телефона : ")
info.append("Эл.почта : ")
print(info[0] + '87071376847')
print(info[1] + 'nabiaiman@gmail.com')
print("Цель : " + "Получение вакантной должности программиста-стажера")


#5. Словарь синонимов
n = int(input())
dict = {}
for i in range(n):
    f, s = map(str, input().split())
    dict[f] = s
    dict[s] = f
s = str(input())
print(dict[s])
