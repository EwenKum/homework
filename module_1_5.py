immutable_var = ([1, 2, 6], True, 'String', 58, 75.7) #1
print(immutable_var)

mutable_list = [1, 2, 6, True, 'String', 58, 75.7]
mutable_list.extend([False, 'Boba'])
mutable_list [-1] = 48
print(mutable_list)

immutable_var [1] = False                             #2 Кортеж обычно используют для хранения информации и защиты от случайного изменения данных. Он неизменяемый и по размеру меньше других типов данных
print(immutable_var)

