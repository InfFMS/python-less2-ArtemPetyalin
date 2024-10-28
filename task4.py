N = int(input())
pow_2 = '2'

for i in range(2, N + 1):
    pow_2 = pow_2 + ' ' + str(2 ** i)

print(pow_2)