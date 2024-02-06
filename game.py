from gameparts import Board
# from gameparts import parts
# from gameparts import FieldIndexError
from gameparts.exceptions import FieldIndexError, ColumnIndexErorr


# Вот новая функция.
# def main():
#    game = Board()
#    game.display()
#    # Тут пользователь вводит координаты ячейки.
#    row = int(input('Введите номер строки: '))
#    column = int(input('Введите номер столбца: '))
#    # В метод make_move передаются те координаты, которые ввёл пользователь.
#    game.make_move(row, column, 'X')
#    print('Ход сделан!')
#    game.display()

def main():
    game = Board()
    game.display()
    # Пользователь вводит номер строки.
    row = int(input('Введите номер строки: '))
    # Если введённое значение меньше нуля или больше или равно
    # field_size (это значение равно трём, оно хранится в модуле
    # parts.py)...
    if row < 0 or row >= game.field_size:
        # ...выбросить исключение FieldIndexError.
        raise FieldIndexError
    column = int(input('Введите номер столбца: '))
    if column <0 or column >= game.field_size: 
        raise ColumnIndexErorr
    game.make_move(row, column, 'X')
    print('Ход сделан!')
    game.display()


# А вот вызов этой функции.
if __name__ == '__main__':
    main()
