# 4. * Функция принимает в качестве аргументов строки в формате «Имя Фамилия», возвращает словарь, 
# ключи — первые буквы фамилий, значения — словари, реализованные по схеме предыдущего задания.
# in
# "Иван Сергеев", "Инна Серова", "Петр Алексеев",
# "Илья Иванов", "Анна Савельева", "Юнона Ветрякова",
# "Борис Аркадьев", "Антон Серов", "Павел Анисимов"
# out
# {'С': {'А': ['Анна Савельева', 'Антон Серов'], 'И': ['Иван Сергеев', 'Инна Серова']}, 
# 'А': {'Б': ['Борис Аркадьев'], 'П': ['Павел Анисимов', 'Петр Алексеев']}, 'И': {'И': ['Илья Иванов']},
#  'В': {'Ю': ['Юнона Ветрякова']}}

def dictionary(*list):
    result = {}

    for surname in list:
        key_1 = surname.split()[1][0]
        if not key_1 in result: 
            result[key_1] = []
            
        result[key_1].append(surname)
        
        
        
    #     for key_1, name in result:
    #         key_2 = name.split()[0]
    #         if not key_2 in result:
    #             result[key_2] = []
    #         result[key_2].append(name)
        
    # return result

print(dictionary("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева", "Юнона Ветрякова",
    "Борис Аркадьев", "Антон Серов", "Павел Анисимов"))


# def thesaurus_adv(*args):
#     s_n_sort = {}
#     for s_n in args:
#         s_n_sort.setdefault(s_n.split()[1][0], {}).setdefault(s_n.split()[0][0], []).append(s_n)
#     return s_n_sort


# print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев",
#                     "Илья Иванов", "Анна Савельева", "Юнона Ветрякова",
#                     "Борис Аркадьев", "Антон Серов", "Павел Анисимов"))

# dict.setdefault(key[, default])