x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if 0 < x1 < 9 and 0 < y1 < 9 and 0 < x2 < 9 and 0 < y2 < 9:

    if abs(x1 - x2) == abs(y1 - y2):
        print('да')

    else:
        print('нет')

else:
    print('ошибка')