# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.
# Пример: Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44} Сумма 9.06

n = int(input('Введите длину списка n = '))
a = 1
list = []
sum = 0
for i in range(1, n+1):
    a = round(((1 + 1/i)**i), 3)
    list.append(a)
    sum = sum + list[i-1]
print(list)
print(sum)