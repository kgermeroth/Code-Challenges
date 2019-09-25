"""Given two strings, are they, at most, one edit away?

    >>> one_away("make", "make")
    True

    >>> one_away("make", "fake")
    True

    >>> one_away("task", "take")
    False

    >>> one_away("ask" ,"asks")
    True

    >>> one_away("asks", "ask")
    True

    >>> one_away("act", "tact")
    True

    >>> one_away("fat", "fact")
    True

    >>> one_away("yes", "no")
    False

"""


def one_away(w1, w2):
    """Given two strings, are they, at most, one edit away?"""

    len1 = len(w1)
    len2 = len(w2)

    length_diff = abs(len1 - len2)

    # see which word is shorter or longer
    if len1 > len2:
        longer, shorter = w1, w2
    else:
        longer, shorter = w2, w1

    # now see if there is only one change needed
    if length_diff > 1:         # if the difference in length is two or more, one edit will not be sufficient
        return False

    elif length_diff == 1:      # if the difference in length is one, see if all but the first or all but the last letter of the longer word matches the shorter word
        if longer[:-1] == shorter or longer[1:] == shorter:
            return True

        else:                   # But what if you are inserting a letter in the middle? 

            for i in range(1,len(shorter)):    # only need to look at inserting, since adding at beginning or end is covered
                if shorter[:i] == longer[:i] and shorter[i:] == longer[(i + 1) : ]:      # see if the letters in longer before and after where letter would be inserted into shorter word match
                    return True

            return False

    else:                       # if the words are the same length see if there is more than one difference by creating a mine field
        mine = [0] * len1
        
        i = 0

        while i < len1:
            if w1[i] != w2[i]:
                mine[i] = 1
            i += 1

        return sum(mine) < 2



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED; NICE JOB! ***\n")
