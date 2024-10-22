a1 = float(input())
b1 = float(input())
a2 = float(input())
b2 = float(input())

if b1 > a1 and b2 > a2:

    if b1 < a2 or b2 < a1:
        print('нет пересечений')

    elif b1 == a2:
        print('точка ' + str(a2))

    elif b2 == a1:
        print('точка ' + str(a1))

    # [a1; b1] правее [a2; b2]
    elif a2 < b1 < b2 and a1 < a2:
        print('[' + str(a2) + '; ' + str(b1) + ']')

    #[a2; b2] правее [a1; b1]
    elif a1 < b2 < b1 and a2 < a1:
        print('[' + str(a1) + '; ' + str(b2) + ']')

    # [a1; b1] внутри [a2; b2]
    elif a2 < a1 and b1 < b2:
        print('[' + str(a1) + '; ' + str(b1) + ']')

    # [a2; b2] внутри [a1; b1]
    elif a1 < a2 and b2 < b1:
        print('[' + str(a2) + '; ' + str(b2) + ']')

else:
    print('error')
