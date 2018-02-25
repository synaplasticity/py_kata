from ProductOfFibNumbers.product_fib_num import fibonacci
from ProductOfFibNumbers.product_fib_num import product_fib_num


def test_fibonacci_function_for_0():
    assert fibonacci(0) is 0


def test_fibonacci_function_for_1():
    assert fibonacci(1) is 1


def test_fibonacci_function_for_3():
    assert fibonacci(3) is 2


def test_fibonacci_function_for_11():
    assert fibonacci(11) is 89


def test_prodt_fib_num_true():
    assert product_fib_num(714) is [21, 34, True]
