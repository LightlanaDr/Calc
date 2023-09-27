#Данный модуль отвечает за обработку поступающих чисел. В зависимости от типа (рациональные или комплексные)
#данные записываются в типы данных float и complex соответственно.
def input_data():
    number = float(input('Введите рациональное число: '))
    return number

def input_comlex():
    number = complex(input('Введите комлексное число (пример: "5+6j"): '))
    return number

def view_data(number):
    print(f'Результат: {number}')

