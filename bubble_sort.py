def bubble(numbers):
    """
    Реализация алгоритма сортировки пузырьком.
    """
    length = len(numbers)
    for x in range(length - 1):
        check = False
        for y in range(length - 1 - x):
            if numbers[y] > numbers[y + 1]:
                check = True
                numbers[y], numbers[y + 1] = numbers[y + 1], numbers[y]
        if not check:
            break
    return numbers


if __name__ == '__main__':
    print(bubble([1, 4, 7, 2, 10, 15, 20, 3, 45]))
    print(bubble([1, 0]))
    print(bubble([0]))
    print(bubble([-23, 0, 6, -4, 34]) == sorted([-23, 0, 6, -4, 34]))
    print(bubble([0, 5, 2, 3, 2]) == sorted([0, 5, 2, 3, 2]))