"""Given an NxM matrix, if a cell is zero, set entire row and column to zeroes.

A matrix without zeroes doesn't change:

    >>> zero_matrix([[1, 2 ,3], [4, 5, 6], [7, 8, 9]])
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

But if there's a zero, zero both that row and column:

    >>> zero_matrix([[1, 0, 3], [4, 5, 6], [7, 8, 9]])
    [[0, 0, 0], [4, 0, 6], [7, 0, 9]]

Make sure it works with non-square matrices:

    >>> zero_matrix([[1, 0, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    [[0, 0, 0, 0], [5, 0, 7, 8], [9, 0, 11, 12]]
"""


def zero_matrix(matrix):
    """Given an NxM matrix, for cells=0, set their row and column to zeroes."""

    row_to_zero = None
    col_to_zero = None 

    for i, lst in enumerate(matrix):
        for j, num in enumerate(lst):
            if num == 0:
                row_to_zero = i
                col_to_zero = j

    # update proper values to zero
    if row_to_zero is not None:
        # update row to zero
        for i in range(len(matrix[row_to_zero])):
            matrix[row_to_zero][i] = 0

        # update columns
        for i in range(len(matrix)):
            matrix[i][col_to_zero] = 0

    return matrix


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** TESTS PASSED! YOU'RE DOING GREAT!\n")
