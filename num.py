"""
Представление числа в видде степени по выбраному основынию
"""
Chr = {'0': chr(8304), '1': chr(185), '2': chr(178), '3': chr(179), '4': chr(8308),
       '5': chr(8309), '6': chr(8310), '7': chr(8311), '8': chr(8312), '9': chr(8313), '-': chr(8315)}


def number_to_digit_rev(num, base):
    pow = 0

    if num > 0:

        if num > 1:

            num = int(num)
            while num > 1:
                num /= 10
                pow += 1

        while num < 1:
            num *= 10
            pow -= 1

    elif num < 0:

        if num < -1:

            num = int(num)
            while num < -1:
                num /= 10
                pow += 1

        while num > -1:
            num *= 10
            pow -= 1

        base = -base

        if pow % 2 == 0:
            print('negative number', base, 'via even pow', pow)
            return 0

    else:
        print('Put your finger im  my', chr(9794) + 'ss')
        return 0

    pow = list(str(pow))

    for i in range(len(pow)):
        pow[i] = Chr.get(pow[i])

    print('~', base, ''.join(pow))


print('Input MIGHTY BIG FAT HUGE LARGE number or his expression: num;base')

print('Example: (10**20/6+100/0.000057)*-23.535;44\n')
number_to_digit_rev((10 ** 20 / 6 + 100 / 0.000057) * -23.535, 44)
print('\n22**33;0.6\n')
number_to_digit_rev(22 ** 33, 0.6)

while True:
    Num, base = list(input().split(';'))
    Num = eval(Num)
    base = float(base)
    number_to_digit_rev(Num, base)
