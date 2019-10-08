"""Given list (haystack), return index (0-based) of needle in the list.

    Return None if needle is not in haystack.

    Do this with recursion. You MAY NOT USE A `for` OR `while` LOOP.

For example:

    >>> recursive_index(5, [1, 3, 5, 2, 4])
    2

    >>> recursive_index("hey", ["hey", "there", "you"])
    0

    >>> recursive_index("you", ["hey", "there", "you"])
    2

    >>> recursive_index("zork", ["foo", "bar", "baz"]) is None
    True

"""


def recursive_index(needle, haystack, i = 0):
    """Given list (haystack), return index (0-based) of needle in the list.

    Return None if needle is not in haystack.

    Do this with recursion. You MAY NOT USE A `for` OR `while` LOOP.
    """
    if not haystack:
        return

    if haystack[0] == needle:
        return i
    else:
        i += 1        
        return recursive_index(needle, haystack[1:], i)

    # Official solution:
    # def _recursive_index(needle, haystack, start_at):

    #     # Check if not found (we've gone too far)
    #     if start_at == len(haystack):
    #         return None

    #     # Have we found it?
    #     if haystack[start_at] == needle:
    #         return start_at

    #     return _recursive_index(needle, haystack, start_at + 1)

    # return _recursive_index(needle, haystack, 0)

    # my solution is a little dangerous - what if a third argument is supplied when calling the function?

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. GO GO GO!\n")
