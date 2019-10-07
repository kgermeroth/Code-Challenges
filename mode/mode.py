"""Find the most frequent num(s) in nums.

Return the set of nums that are the mode::

    >>> mode([1]) == {1}
    True

    >>> mode([1, 2, 2, 2]) == {2}
    True

If there is a tie, return all::

    >>> mode([1, 1, 2, 2]) == {1, 2}
    True
"""


def mode(nums):
    """Find the most frequent num(s) in nums."""

    mode = set()
    mode_times = 0
    num_count = {}

    for i in nums:
        num_count[i] = num_count.get(i, 0) + 1
        if num_count[i] > mode_times:
            mode_times = num_count[i]

    for num, count in num_count.items():
        if count == mode_times:
            mode.add(num)

    return mode

# could optimize a little bit - instead of checking and updating mode_times each time, take max of num_count.values()


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. HOORAY!\n")
