def fibonacci(number):
    if number == 0 or number == 1:
        return number*number
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)


def product_fib_num(product):
    """
    Returns a list of the two consecutive fibonacci numbers
    that give the provided product and a boolean indcating if
    those two consecutive numbers where found.
    """

    for n in range(1, product):
        f1 = fibonacci(n)
        f2 = fibonacci(n + 1)

        if f1 * f2 == product or f1 * f2 > product:
            break

    return [f1, f2, f1 * f2 == product]
    # return list[0]
