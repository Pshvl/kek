f=open('24.txt').readline()
j=''  #пустая строка
for i in range(len(f)-1):   #до предпоследнего символа
    if f[i] == 'A':
        j += f[i+1]   #следующий символ в строку
print(j)
print(set(j))
print(max(set(j),key = j.count))
#сет - множество элементов(т.е удаляем повторяющиеся)
#ключ-кол во
#Параметру key присвоено значение j.count, которое определяет функцию,
# вычисляющую значение ключа для каждого элемента в наборе.
#j.count используется для подсчета вхождений каждого символа
#в исходной строке j,
#set(j): Эта часть преобразует строковую переменную j в набор.
# Набор в Python - это неупорядоченная коллекция уникальных элементов. Этот шаг гарантирует, что у нас есть набор уникальных элементов из строки.

#2. key=j.count: Аргумент key используется совместно с функцией max() для указания функции, которая вычисляет значение ключа для каждого элемента
# в наборе. В данном случае используется j.count. Это относится к методу count() strings в Python, который возвращает количество вхождений определенного элемента в строке.