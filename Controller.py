# модуль отвечает за считывание чисел с консоли и выбор вычислительных операций
import data_provided as dp
import model_operation as model
import logger as log

def click_button():
    value = int(input('Введите: \n1 - для операций с комплексными числами, \n2 - для операций с рациональными числами\n: '))
    if value == 1:
        value_a = dp.input_comlex()
        value_b = dp.input_comlex()
    if value == 2:
        value_a = dp.input_data()
        value_b = dp.input_data()

    value_model = input('Введите значение операции: +, -, * или /: ')
    if value_model == '/':
        result = model.div(value_a, value_b)
        dp.view_data(result)
    if value_model == '+':
        result = model.sum(value_a, value_b)
        dp.view_data(result)
    if value_model == '*':
        result = model.mult(value_a, value_b)
        dp.view_data(result)
    if value_model == '-':
        result = model.sub(value_a, value_b)
        dp.view_data(result)

    log.nums_logger(value_a, value_b, value_model, result)

def restart():
    val = int(input('\n Что делаем дальше? \n 1. Новое вычисление \n 2. Закрываем калькулятор \n:'))

    if val == 1:
        click_button();
    if val == 2:
        print('Благодарим за использование нашего приложения');
