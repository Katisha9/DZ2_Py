# 3. Реализуйте алгоритм перемешивания списка. Встроенный алгоритм SHUFFLE не использовать!
# Реализовать свой метод


from random import randint as rand


def shuffle(list):
    shufLen = len(list)
    while shufLen:
        shufLen -= 1
        i = rand(0, shufLen)
        list[shufLen], list[i] = list[i], list[shufLen]
    return list


size = int(input('Введите длину списка: '))
randomList = []

for i in range(size):
    randomList.append(rand(0, 100))

print(randomList)
shuffle(randomList)
print(randomList)