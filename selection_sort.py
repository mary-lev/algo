import random


def selection_sort(numbers):
    length = len(numbers)

    for i in range(length - 1):
        least = i
        for k in range(i + 1, length):
            if numbers[k] < numbers[least]:
                least = k

        if least != i:
            numbers[least], numbers[i] = numbers[i], numbers[least]

    return numbers


if __name__ == '__main__':
    test_list = [random.randint(0, 100) for iter in range(10)]
    print(selection_sort(test_list))
    print(selection_sort([1]))
