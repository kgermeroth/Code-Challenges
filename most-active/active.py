"""Find window of time when most authors were active.

For example::

    >>> data = [
    ...    ('Alice', 1901, 1950),
    ...    ('Bob',   1920, 1960),
    ...    ('Carol', 1908, 1945),
    ...    ('Dave',  1951, 1960),
    ... ]

    >>> most_active(data)
    (1920, 1945)

(Alice, Bob, and Carol were all active then).

If there's more than one period, find the earliest::

    >>> data = [
    ...    ('Alice', 1901, 1950),
    ...    ('Bob',   1920, 1960),
    ...    ('Carol', 1908, 1945),
    ...    ('Dave',  1951, 1960),
    ...    ('Eve',   1955, 1985),
    ... ]

    >>> most_active(data)
    (1920, 1945)

(Alice, Bob, Carol were active 1920-1945. Bob, Dave, and Eve were active 1951-1960.
Since there's a tie, the first was returned)
"""


def most_active(bio_data):
    """Find window of time when most authors were active."""

    active_auth_by_year = {}    

    # makes a dictionary with a count of how many authors are active for each year
    for author in bio_data:
        for year in range(author[1], author[2] + 1):
            authors_active = active_auth_by_year.get(year, 0)
            active_auth_by_year[year] = authors_active + 1

    # gives the biggest number of active authors
    max_active = max(active_auth_by_year.values())
    
    # get a list of all years that have the max authors present
    years_at_max = []

    for year_count in active_auth_by_year.items():
        if year_count[1] == max_active:
            years_at_max.append(year_count[0])

    # sort the list to ensure years are in order
    years_at_max.sort()

    # get the first year
    start_year = years_at_max[0]

    # get the last year in range (look for the first year when the next year is not sequential

    # first go through each item and see if the next item is only one year different
    # if it's NOT, that's because it's the start of a new range. So take the current year
    # and that's the end year. Return tuple
    try:
        for i, year in enumerate(years_at_max):
            if years_at_max[i + 1] - year != 1:
                return((start_year, year))
                
    # if there is only one range present, you will get an out of range index error if you 
    # reach the end and it's still the same range. If that happens, just take the last 
    # value and make that the year
    except:
        return((start_year, years_at_max[-1]))





if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YAY!\n")