# 1 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример: 0,56 -> 11
real_number = input("Введите число, узнаем сумму его цифр ")

def CalculateNumbers (real_number):
    summa = 0
    list = []
    i = 0
    for char in real_number:
        if char == "." or char == "," or char == "-":
            char = 0
        list.append(int(char))
        summa = summa + list[i]
        i += 1
    return summa

print("\nСумма всех цифр введённого числа: [", CalculateNumbers(real_number), "]")