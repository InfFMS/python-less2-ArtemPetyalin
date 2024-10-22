a = int(input())

if a == 1 or a == 2 or a == 12:
    print('Зима')

elif 3 <= a <= 5:
    print('Весна')

elif 6 <= a <= 8:
    print('Лето')

elif 9 <= a <= 11:
    print('Осень')

else:
    print('Неверный номер месяца')
