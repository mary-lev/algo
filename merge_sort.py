import random

def merge(numbers_first: list, numbers_second: list) -> list:
    """
    Метод двух указателей.
    :param numbers_first: отсортированный список
    :param numbers_second: отсортированный список
    :return: один список, объединяющий элементы двух данных
    """
    result = list()
    i = 0
    j = 0
    while i < len(numbers_first) and j < len(numbers_second):
        if numbers_first[i] < numbers_second[j]:
            result.append(numbers_first[i])
            i += 1
        else:
            result.append(numbers_second[j])
            j += 1
    result += numbers_first[i:] + numbers_second[j:]
    return result

def merge_sort(numbers: list) -> list:
    if len(numbers) > 1:
        return merge(
            merge_sort(numbers[:len(numbers) // 2]),
            merge_sort(numbers[len(numbers) // 2:])
            )
    else:
        return numbers

if __name__ == '__main__':
    test_list = [random.randint(0, 100) for iter in range(100)]
    print(merge_sort([4, 3, 2, 1]))
    print(merge_sort(test_list))
    print(merge_sort([1]))
