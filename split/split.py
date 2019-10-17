"""Split a string by splitter and return list of splits.

This should work like the built-in Python .split() method [*].
YOU MAY NOT USE the .split() method in your solution!
YOU MAY NOT USE regular expressions in your solution!

For example:

    >>> split("i love balloonicorn", " ")
    ['i', 'love', 'balloonicorn']

    >>> split("that is which is that which is that", " that ")
    ['that is which is', 'which is that']

    >>> split("that is which is that which is that", "that")
    ['', ' is which is ', ' which is ', '']

    >>> split("hello world", "nope")
    ['hello world']

* Note: the actual Python split method has special behavior
  when it is not passed anything for the splitter -- you do
  not need to implement that.

"""


def split(astring, splitter):
    """Split a string by splitter and return list of splits."""

    list_of_splits = []

    # index through string and keep track of the index
    i = 0

    while i <= len(astring):
        # look for the index of the splitter starting at our current index
        next_splitter = astring.find(splitter, i)

        # if the splitter is not found, then add the string from i through the end to the list
        if next_splitter == -1:
            list_of_splits.append(astring[i:])
            
            break

        # if it is found, add the string sliced from i : next_splitter and then advance i to be the end of the 
        else:
            list_of_splits.append(astring[i:next_splitter])
            i = next_splitter + len(splitter)

    return list_of_splits


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. FINE SPLITTING!\n")
