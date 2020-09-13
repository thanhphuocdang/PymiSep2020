def fibonacci(number):
    if number == 0:
        return [0]
    fibonacci_array = [0]
    for element in range(1, number + 1):
        if element == 1 or element == 2:
            fibonacci_array.append(1)
        else:
            value = fibonacci_array[element - 1] + fibonacci_array[element - 2]
            fibonacci_array.append(value)
    return fibonacci_array


if __name__ == '__main__':
    n = int(input())
    print(fibonacci(n))

    print(list(map(lambda x: x ** 3, fibonacci(n))))
