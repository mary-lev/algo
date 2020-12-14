import random

def qsort(numbers):
    """
    Реализация быстрой сортировки (она же сортировка Хоара).
    Худшее время: О(n ** 2)
    Лушчее время: O(n log n)
    Среднее время: O(n log n)
    Затраты памяти: O(log n)
    :param numbers: список сравнимых элементов
    :return: отсортированный по возрастанию список элементов
    """
    if len(numbers) < 2:
        return numbers
    point = numbers.pop()
    greater = list()
    lesser = list()
    for number in numbers:
        (greater if number > point else lesser).append(number)
    return qsort(lesser) + [point] + qsort(greater)


if __name__ == '__main__':
    test_list = [random.randint(0, 100) for iter in range(10)]
    print(qsort(test_list))
    print(qsort([1]))
