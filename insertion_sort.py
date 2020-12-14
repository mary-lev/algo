import random


def insertion_sort(numbers):
    """
    Сортировка вставками (Insertion sort)
    Худшее время: O(n ** 2)
    Лучшее время: O(n), 0 обменов
    Среднее время: O(n ** 2)
    Затраты памяти: O(n), O(1) вспомогательный.
    :param numbers: список сравнимых элементов.
    :return: отсортированный список элементов.
    """
    for insert_index, insert_value in enumerate(numbers[1:]):
        temp_index = insert_index
        while insert_index >= 0 and insert_value < numbers[insert_index]:
            numbers[insert_index + 1] = numbers[insert_index]
            insert_index -= 1
        if insert_index != temp_index:
            numbers[insert_index + 1] = insert_value
    return numbers


if __name__ == '__main__':
    test_list = [random.randint(0, 100) for iter in range(10)]
    print(insertion_sort(test_list))
    print(insertion_sort([1]))