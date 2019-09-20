"""Lazy lemmings.

Find the farthest any single lemming needs to travel for food.

    >>> furthest(3, [0, 1, 2])
    0

    >>> furthest(3, [2])
    2

    >>> furthest(3, [0])
    2

    >>> furthest(6, [2, 4])
    2

    >>> furthest(7, [0, 6])
    3

    >>> furthest_optimized(7, [0, 6])
    3

    >>> furthest_optimized(3, [0, 1, 2])
    0

    >>> furthest_optimized(3, [2])
    2

    >>> furthest_optimized(3, [0])
    2

    >>> furthest_optimized(6, [2, 4])
    2
"""


def furthest(num_holes, cafes):
    """Find longest distance between a hole and a cafe."""

    # set a farthest counter
    farthest = 0

    # loop through lemming hole locations
    for num in range(num_holes):

        # find the shortest distance from lemming hole (num) to cafe
        smallest_distance = num_holes - 1

        for cafe in cafes:
            
            distance = abs(cafe - num)

            if distance < smallest_distance:
                smallest_distance = distance

        if smallest_distance > farthest:
            farthest = smallest_distance

    return farthest


def furthest_optimized(num_holes, cafes):
    """Find longest distance between a hole and a cafe."""

    # set a farthest counter
    farthest = 0

    if len(cafes) == num_holes:
        return farthest

    cafe_indices = set(cafes)

    # loop through lemming hole locations
    for num in range(num_holes):

        if num in cafe_indices:
            continue

        else:
            # find the shortest distance from lemming hole (num) to cafe
            smallest_distance = num_holes - 1

            for cafe in cafes:
                
                distance = abs(cafe - num)

                if distance < smallest_distance:
                    smallest_distance = distance

            if smallest_distance > farthest:
                farthest = smallest_distance

    return farthest

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED; GREAT JOB!\n")
