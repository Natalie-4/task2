# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных индексах. Индексы вводятся одной строкой, через пробел.
# n = 3 [-3, -2, -1, 0, 1, 2, 3] --> 0 2 3
# -3 * -1 * 0 = 0 Вывод: 0

N = int(input('Введите значение N = '))
position_1 = int(input('Введите номер позиции элемента 1:'))
position_2 = int(input('Введите номер позиции элемента 2:'))
list = []
for i in range(2*N+1):
    if i < N:
        list.append(-N+i)
    elif i > N:
        list.append(i-N)
    else:
        list.append(0) 
print(list)
if ((position_1 or position_2) > 2*N+1) or (position_1 or position_2) <=0:
    print('как минимум одно значение позиции элемента за пределами [-N, N]')
else:
    print(f"Произведение элементов в указанных позициях = {list[position_1-1]*list[position_2-1]}" )
