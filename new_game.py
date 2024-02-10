from gameparts import Board
from gameparts.exceptions import FieldIndexError, ColumnIndexErorr, CellOccupiedError, ValErr


def save_result(file_str): 
    with open('results.txt', 'a',encoding='utf-8') as f:
            f.write(file_str + '\n')
            #file_result = open('results.txt', 'a',encoding='utf-8')
            #file_result.close()



def main():
    game = Board()
    current_player = 'X'
    running = True
    game.display()

    while running:
        # Запускается бесконечный цикл.
        while True:
            print(f'Ход делают {current_player}')
            # В этом блоке содержатся операции, которые могут вызвать исключение.
            try:
                # Пользователь вводит значение номера строки.
                row = int(input('Введите номер строки: '))
                # Если введённое число меньше 0 или больше
                # или равно game.field_size...
                if row < 0 or row >= game.field_size:
                    # ...выбрасывается собственное исключение FieldIndexError.
                    raise FieldIndexError
                column = int(input('Введите номер столбца: '))
                # Если введённое число меньше 0 или больше
                # или равно game.field_size...
                if column < 0 or column >= game.field_size:
                    # ...выбрасывается собственное исключение FieldIndexError.
                    raise FieldIndexError
            # Если возникает исключение FieldIndexError...
                if game.board[row][column] != ' ':
                    raise CellOccupiedError
                
            except FieldIndexError:
                # ...выводятся сообщения...
                print(
                    'Значение должно быть неотрицательным и меньше '
                    f'{game.field_size}.'
                )
                print('Пожалуйста, введите значения для строки и столбца заново.')
                # ...и цикл начинает свою работу сначала,
                # предоставляя пользователю ещё одну попытку ввести данные.
                continue

            except ColumnIndexErorr:
                print(
                    'Значение должно быть неотрицательным и меньше '
                    f'{game.field_size}.'
                )
                print('Пожалуйста, введите значения для строки и столбца заново.')
            except ValueError:
                print('Буквы вводить нельзя. Только числа.')
                print('Пожалуйста, введите значения для строки и столбца заново.')   
            # except ValErr:
            #     print('Буквы вводить нельзя. Только числа.')
            #     print('Пожалуйста, введите значения для строки и столбца заново.')
            except Exception as exc: 
                print(f'Возникла ошибка: {exc}')
                
            # Если в блоке try исключения не возникло...
            else:
                # ...значит, введённые значения прошли все проверки
                # и могут быть использованы в дальнейшем.
                # Цикл прерывается.
                break                   
        game.make_move(row, column, current_player)
        print('Ход сделан!')
        game.display()

        if game.check_win(current_player):
            str_to_file = f'Победили {current_player}!'
            save_result(str_to_file)
            print(f'Победили {current_player}!')
            running = False
        elif game.is_board_full():
            str_to_file = 'Ничья!'
            save_result(str_to_file)
            print(str_to_file)
            running = False

        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == '__main__':
    main()




