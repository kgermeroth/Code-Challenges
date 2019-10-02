"""How many different ways can you climb a staircase of `n` steps?

You can climb 1, 2, or 3 steps at a time.

For one step, we could do this one way: 1

    >>> steps(1)
    1

For two: 11 2

    >>> steps(2)
    2

For three: 111 12 21 3

    >>> steps(3)
    4

For four: 1111 121 211 112 22 13 31

    >>> steps(4)
    7

For five: 11111 2111 1211 1121 1112 122 121 221 113 131 311 23 32

    >>> steps(5)
    13

For six steps: 111111 21111 12111 11211 11121 11112 2211 2121 2112
    1212 1122 1221 3111 1311 1131 1113 321 312 213 231 132 123 222 33

    >>> steps(6)
    24
"""


def steps(n):
    """How many different ways can you climb a staircase of `n` steps?

    You can climb 1, 2, or 3 steps at a time.
    """

    # # we can solve this by figuring out all the non-unique step combos (ie for three steps 2,1 and 1,2 would be the same)
    # # and then go through each combo and calculate the number of combinations possible

    non_unique_step_combos = []

    for a in range(n + 1):                          # all possible values for a (1 step)
        for b in range( (n // 2) + 1):             # all possible values for b (2 steps)
            for c in range ( (n // 3) + 1):        # c is num of 3 steps, it is max possible left after a and b are assigned values

                if ((1 * a) + (2 * b) + (3 * c)) == n:    # see if combination is exactly equal to the number of steps. If it is, move on

                    non_unique_step_combos.append((a, b, c))

    # now we loop through each item in our non_unique_step_combos and calculate the number of possible combinations
    # this can be calculated by (a + b + c)! / (a! * b! * c!)

    count_of_ways_to_step = 0

    for (a, b, c) in non_unique_step_combos:

        possible_combos = 0

        abc_factorial = 1
        a_factorial = 1
        b_factorial = 1
        c_factorial = 1


        for i in range(1,(a + b + c + 1)):
            abc_factorial = abc_factorial * i

        for i in range(1,(a + 1)):
            a_factorial = a_factorial * i

        for i in range(1,(b + 1)):
            b_factorial = b_factorial * i

        for i in range(1,(c + 1)):
            c_factorial = c_factorial * i

        count_of_ways_to_step += int(abc_factorial / (a_factorial * b_factorial * c_factorial))

    return count_of_ways_to_step


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TEST PASSED! YOU'RE A STAIRMASTER!\n")
