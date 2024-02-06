# from inspect import getsource

# from gameparts import Board

# game = Board()

# Функция getsource() в работе.
#print(getsource(Board)) 
#
#print(str.__doc__)
#
#print(Board.__doc__)

try:
    # Блок кода, который может вызвать исключение.
    result = 10 / 1
except ZeroDivisionError as e:
    # Обработка исключения при делении на ноль.
    print(f'Ошибка: {e}')
else:
    # Блок кода, который выполняется, если исключение не возникло.
    print('Операция выполнена успешно.')
finally:
    # Блок кода, который выполняется всегда.
    print('Программа завершила свою работу.')