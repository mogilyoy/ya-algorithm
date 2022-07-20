# Задача 1
# Найти первое вхождение положительного числа Х в последовательности чисел длиной Н, или вывести -1, если число не встречалось 


def task1(lst: list, target) -> int:
    for i, el in enumerate(lst):
        if el == target:
            return i
    return -1

# Задача 2
# Найти последнее (самое правое) вхождение числа Х в последовательность чисел длиной Н.
# Вернуть -1, если число не встречается

def task2(seq: list, target)->int:
    for i in range(len(seq)-1, -1, -1):
        if seq[i] == target:
            return i
    return -1


# Задача 3
# Найдите максимальное число в последовательности
def max_val(seq: list) -> int:
    assert len(seq)>0, 'Список пуст'
    result = seq[0]
    for i in seq:
        if i > result:
            result = i
    return result
# для строк это алгоритм плох, потому что каждый раз будет происходить копирование, хотя в питоне это происходит быстро (мы переприсваиваем ссылку на строку)
# чтобы хорошо работало для строк, можно запоминать не само значение, а индекс

def max_val_2(seq: list) -> int:
    assert len(seq)>0, 'Список пуст'
    result = seq[0]
    for i, el in enumerate(seq):
        if el > seq[result]:
            result = i
    return seq[result]

# Задача 4
# Найти максимальное и второе по величине значение в последовательности длиной Н > 1
# (как если бы мы вычеркнули ОДНО максимальное значение) - не путать 

def max_two(seq:list)->tuple:
    assert len(seq) > 1, 'Не достаточно значений в списке'
    most = seq[0] if seq[0] > seq[1] else seq[1]
    second = seq[1] if seq[0] > seq[1] else seq[0]
    for el in seq[2:]:
        if el > most:
            second = most
            most =el
        elif el > second:
            second = el
    return most, second

# print(max_two([6, 8, 6, 9, 3]))

# Задача 5
# Найти минимальное четное число в последовательности длиной Н 
# Вывести -1, если такого нет

def min_even(seq: list) -> int:
    if seq:
        res = float('inf')
        for el in seq:
            if el%2 == 0 and el<res:
                res = el
        return res if res%2 == 0 else -1 
    else:
        return ('Последовательность пуста')
# print(min_even([4, 3, 2, 5, 6, 7, 8, 5, 4, 3, 1, 0, 0]))

# Задача 6
# Двупроходный алгоритм
# Вывести все самые короткие слова через пробел

def smallest_words(words: list) -> str: 
    # можно было бы за 1 проход искать слова, накапливать их где-то и перезаписывать результат
    # но это медленно 
    minlen = 0
    for word in words:
        if len(word) < minlen:
            minlen = len(word)
    result = [] # если сразу склеивать в строку, то это будет медленно, т.к. в питоне строки - неизменяемый тип, то будт каждый раз создаваться новая строка
    for word in words:
        if len(word) == minlen:
            result.append(word)
    return ' '.join(result)    

print(smallest_words([]))    

# Задача 7
# Остров игрока представляет собой набор столбцов различной высоты, состоящих из блоков
# Над островом прошел дождь и зполнил все углубления, а вся оставшаяся вода стекла в море
# По ландшафту острова определите, сколько блоков воды осталось после дождя  

      #   
 #~~~~###~~~#~~~#
 #~~##########~~#
##################
# примерно так

def isleflood(h):
    maxpos = 0
    for i, el in enumerate(h):
        if el > maxpos:
            maxpos = i
    ans = 0
    curm = 0
    for i in range(maxpos):
        if h[i] > curm:
            curm = h[i]
        ans += curm - h[i]
    curm = 0 
    for i in range(len(h)-1, maxpos, -1):
        if h[i] > curm:
            curm = h[i]
        ans += curm - h[i]
    return ans

# Задача 8
# Дана строка АААВВВВВВСССССXYZAA
# Нужно написать функцию RLE, которая выдаст строку вида: А3В6С5ХYZA2
# И в случае не валидной строки (не из A-Z), выдаст ошибку
# моя:
def RLE(string):
    lenght = len(string)
    result = [] 
    counter = 0
    for i in range(lenght-1):
        assert ord(string[i]) >= 65 and ord(string[i]) <= 90, f'[{string[i]}]: Недопустимый символ'
        counter += 1
        if string[i] != string [i+1]:
            result.append(f'{string[i]}{counter}' if counter > 1 else f'{string[i]}')
            counter = 0
    assert ord(string[i+1]) >= 65 and ord(string[i+1]) <= 90, f'[{string[i+1]}]: Недопустимый символ'
    result.append(f'{string[i+1]}{counter+1}' if counter > 1 else f'{string[i+1]}')
    return ''.join(result)
    
# с разбора:
def rle(s):
    def pack(s, cnt):
            if cnt>1:
                return s + str(cnt)
            return s
    lastsym = s[0]
    lastpos = 0
    ans = []
    for i in range(len(s)):
        if s[i] != lastsym:
            ans.append(pack(lastsym, i - lastpos))
            lastpos = i
            lastsym = s[i]
    ans.append(pack(s[lastpos], len(s) - lastpos))
    return ''.join(ans)

# a1 = """
# def RLE(string):
#     lenght = len(string)
#     result = [] 
#     counter = 0
#     for i in range(lenght-1):
#         counter += 1
#         if string[i] != string [i+1]:
#             result.append(f'{string[i]}{counter}' if counter > 1 else f'{string[i]}')
#             counter = 0
#     result.append(f'{string[i]}{counter}' if counter > 1 else f'{string[i]}')
# RLE('GGGGGGGGHHHHHHHHHHDDDDDDDDDUUUUUUUUUURRRRRRIIIEIOOOOWO')

# """
# a2 = """
# def rle(s):
#     def pack(s, cnt):
#         if cnt>1:
#             return s + str(cnt)
#         return s
#     lastsym = s[0]
#     lastpos = 0
#     ans = []
#     for i in range(len(s)):
#         if s[i] != lastsym:
#             ans.append(pack(lastsym, i - lastpos))
#             lastpos = i
#             lastsym = s[i]
#     ans.append(pack(s[lastpos], len(s) - lastpos))
# rle('GGGGGGGGHHHHHHHHHHDDDDDDDDDUUUUUUUUUURRRRRRIIIEIOOOOWO')
# """
# import cProfile
# from timeit import timeit
# import dis
# cProfile.run("rle('')")
# print(timeit(a2, number=100000))
# print('*'*100)
# cProfile.run("RLE('')")
# print(timeit(a1, number=100000))

print(rle('GGGGGGGGHHHHHHHHHHDDDDXYZDDDDDUUUUUUUUUURRRRRRIIIEIOOOOWO'))
print(RLE('GGGGGGGGHHHHHHHHHHDDDDXYZDDDDDUUUUUUUUURRRRRRIIIEIOOOOWO'))

# Вывод: функция преподователя немного быстрее, т.к. оператор += отнимает больше времени, чем =. 




        
 