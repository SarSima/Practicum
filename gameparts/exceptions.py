
class FieldIndexError(IndexError): 
    def __str__(self):
        return 'Введено значение за границами игрового поля'


class ColumnIndexErorr(IndexError): 
    def __str__(self): 
        return 'Введено значение за пределами игровых столбцов'


class ValErr(ValueError):
    def __str__(self): 
        return 'Буквы вводить нельзя. Только числа.'
   

class CellOccupiedError(Exception):

    def __str__(self):
        return 'Попытка изменить занятую ячейку'