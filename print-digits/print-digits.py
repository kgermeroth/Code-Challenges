"""Given int, print each digit in reverse order, starting with the ones place.

For example::

    >>> print_digits(1)
    1

    >>> print_digits(413)
    3
    1
    4

    >>> print_digits(7331)
    1
    3
    3
    7

"""


def print_digits(num):
    """Given int, print digits in reverse order, starting with the ones place."""

    num_str = str(num)

    i = -1

    while i > -1 * (len(num_str) + 1):
        print(num_str[i])
        i -= 1

    ## official solution:
    # while num:
    #     next_digit = num % 10
    #     print(next_digit)
    #     num = (num - next_digit) // 10


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. WOWZA!\n")
