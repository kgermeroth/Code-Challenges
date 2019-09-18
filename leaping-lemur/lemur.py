"""Leaping lemur.

Calculate the fewest number of jumps the lemur needs to
jump to the last tree. The lemur can jump 1 or 2 branches.
It cannot use deadly branch (1 in the list).

    >>> lemur([0])
    0

    >>> lemur([0, 0])
    1

    >>> lemur([0, 0, 0])
    1

    >>> lemur([0, 1, 0])
    1

    >>> lemur([0, 0, 1, 0])
    2

    >>> lemur([0, 0, 0, 0, 1, 0, 0, 1, 0])
    5
"""


def  lemur(branches):
    """Return number of jumps needed."""

    assert branches[0] == 0, "First branch must be alive"
    assert branches[-1] == 0, "Last branch must be alive"

    current_branch = 0
    num_of_jumps = 0

    dead_branches = set()

    # pull indices of dead branches and put in set
    for i, branch in enumerate(branches):
        if branch == 1:
            dead_branches.add(i)

    # keep trying to jump unless the current branch is the last branch
    while current_branch != len(branches) - 1:

        # as long as we're not less than two branches from the end try to jump two branches
        if current_branch != len(branches) - 2:

            # check to see if the new branch is a dead branch
            if (current_branch + 2) in dead_branches:

                # if it is, only jump one branch
                current_branch += 1
                num_of_jumps += 1

            # if it's not dead, jump two!
            else:
                current_branch += 2
                num_of_jumps += 1

        # if we are less than two branches from the end we can only jump one branch
        else:
            current_branch += 1
            num_of_jumps += 1

    return num_of_jumps




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. NICE JUMPING!\n")