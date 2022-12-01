# 2. Задайте список из n чисел последовательности (1 + 1/n)^n.
# Вывести в консоль сам список и сумму его элементов.

n = int(input('Введите число n: '))

startList = []
summElem = 0
for i in range(1, n+1):
    startList.append((1 + 1 / i) ** i)
    summElem += startList[i - 1]

print (*startList, sep=', ')
print(f'Сумма элементов списка: {summElem}')