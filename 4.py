# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

n = int(input('Введите чилсло: '))

spis = [i for i in range(-n, n+1)]
print(spis)


with open('file.txt') as file:
    for i in file:
        print(f'{i} индекс = {spis[int(i.rstrip())]}')