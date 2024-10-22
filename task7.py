N = int(input())

def easy_numbers(b):
    easy_nums = []

    for i in range(2, b + 1):
        num = i
        diver = 2
        counter = 0

        while num != 1:

            if num % diver == 0:
                counter += 1
                num = num // diver
                diver = 2

            else:
                diver += 1

        if counter == 1:
            easy_nums.append(i)

    return easy_nums

print(easy_numbers(N))





