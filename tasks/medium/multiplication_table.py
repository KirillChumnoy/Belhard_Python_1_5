"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Реализовать таблицу умножения от 0 до 10 включительно.
Функция принимает значение n, нужно вернуть список значений [n, n*2, n*4 ..]

нужно будет применить функцию range
"""


def multiplication_table(n: int) -> list:
    # TODO тут написать код
    list_value = []
    for i in range(11):
        list_value.append(n * i)
    result = list_value
    return result


if __name__ == '__main__':
    assert multiplication_table(5) == [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
    print('Решено!')
