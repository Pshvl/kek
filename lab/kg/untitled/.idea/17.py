#ФАЙЛ В ТОЙ ЖЕ ДИРЕКТОРИИ ЧТО И ПРОГРАММА
#-10000 10000
#пары хотя бы одно число делится на 3
#макс из сумм элементов этих пар
count = 0
maxx = -20001
f = open('17.txt')
l = [int(i) for i in f]  #считываем инты из файла в список
for i in range(len(l) - 1): #до предпоследнего элемента
    if (l[i] % 3 == 0) or (l[i + 1] % 3 == 0): #первый или второй элемент пары делится
        count += 1 #увеличиваем счетчик
        maxx = max(maxx, l[i]+ l[i + 1]) #выбираем максимум между старым макс и новой суммой
print(count, maxx) #выводим колво пар и максимум
