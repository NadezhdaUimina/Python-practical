# 5. ** Реализовать функцию, возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх списков 
# (по одному из каждого)
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью", "когда-то", "где-то"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
# in
# 10 True
# out
# ['дом ночью мягкий', 'огонь завтра зеленый', 'лес вчера яркий', 'автомобиль сегодня веселый', 'город позавчера утопичный']
# in
# 10 False
# ['автомобиль ночью мягкий', 'огонь вчера веселый', 'автомобиль позавчера веселый', 'город вчера утопичный', 
# 'лес сегодня зеленый', 'дом вчера яркий', 'автомобиль вчера зеленый', 'огонь позавчера яркий', 'огонь где-то утопичный', 
# 'автомобиль где-то мягкий']

from random import randrange
from secrets import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью", "когда-то", "где-то"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]   

def get_jokes(num, flag):
     
    list_min = min(nouns, adverbs, adjectives)
    list_joke = []
    if flag:
        for i in range(len(list_min)):
            rang_min = randrange(len(list_min))
            list_joke.append(f"{nouns.pop(rang_min)} {adverbs.pop(rang_min)} {adjectives.pop(rang_min)}")
    else:
        for i in range(num):
            list_joke.append(f"{choice(nouns)} {choice(adverbs)} {choice(adjectives)}")
    print(list_joke)
        
    
get_jokes(10, True)
