"""
СОРТИРОВКА ВСТАВКАМИ

Как и сортировка выборкой, этот алгоритм сегментирует список на две части:
отсортированную и неотсортированную. Алгоритм перебирает второй сегмент и
вставляет текущий элемент в правильную позицию первого сегмента.

Предполагается, что первый элемент списка отсортирован.
Переходим к следующему элементу, обозначим его х. Если х больше первого,
оставляем его на своём месте.
Если он меньше, копируем его на вторую позицию,
а х устанавливаем как первый элемент.

Переходя к другим элементам несортированного сегмента, перемещаем более
крупные элементы в отсортированном сегменте вверх по списку, пока не встретим
элемент меньше x или не дойдём до конца списка.
В первом случае x помещается на правильную позицию.

ВРЕМЯ СОРТИРОВКИ: в среднем O(n²)
"""


def insertion_sort(array: list) -> list:

    for first_elem in range(len(array) - 1):
        for second_elem in range(first_elem, len(array)):
            if array[first_elem] > array[second_elem]:
                array[first_elem], array[second_elem] = array[second_elem], array[first_elem]

    return array


if __name__ == '__main__':
    assert insertion_sort([2, 1, 5, 4, 7]) == [1, 2, 4, 5, 7]
    assert insertion_sort([2, -5, -3, 3, 1, 2]) == [-5, -3, 1, 2, 2, 3]
    print('Решено!')
