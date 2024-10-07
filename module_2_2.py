first = int(input('Введите 3 целых числа: \n1. '))
second = int(input('2. '))
third = int(input('3. '))

if first == second and second == third:
    print(3)

elif first == second or second == third or third == first:
    print(2)

elif first != second and second != third:
    print(0)
