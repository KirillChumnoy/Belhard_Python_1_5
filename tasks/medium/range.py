"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Написать функцию list_compose, которая принимает два списка (INDEX_LIST, VALUE_LIST).
Составить новый список: берем индекс из списка индексов, и вставляем значение по этому
индексу из другого списка. Если значения нет, что вставить None

ПРИМЕРЫ
--------------------------------------------------------------------------------
list_compose(INDEX_LIST, VALUE_LIST) -> ['b', 'f', None, None, 'c', 'd', None, 'e']
"""
INDEX_LIST = [1, -1, 6, -12, 2, 3, 9, 4]
VALUE_LIST = ['a', 'b', 'c', 'd', 'e', 'f']


def list_compose(indexes: list, values: list) -> list:
    result_list = []
    for index in INDEX_LIST:
        if index in range(len(VALUE_LIST)):
            result_list.append(VALUE_LIST[index])
        elif index in range(-len(VALUE_LIST), 0):
            result_list.append(VALUE_LIST[index])
        else:
            result_list.append(None)

    return result_list


if __name__ == '__main__':
    assert list_compose(INDEX_LIST, VALUE_LIST) == ['b', 'f', None, None, 'c', 'd',
                                                    None, 'e']
    print('Решено!')
