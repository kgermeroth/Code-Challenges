"""Is the word an anagram of a palindrome?

A palindrome is a word that reads the same forward and backwards
(eg, "racecar", "tacocat"). An anagram is a rescrambling of a word
(eg for "racecar", you could rescramble this as "arceace").

Determine if the given word is a re-scrambling of a palindrome.
The word will only contain lowercase letters, a-z.

Examples::

    >>> is_anagram_of_palindrome("a")
    True

    >>> is_anagram_of_palindrome("ab")
    False

    >>> is_anagram_of_palindrome("aab")
    True

    >>> is_anagram_of_palindrome("arceace")
    True

    >>> is_anagram_of_palindrome("arceaceb")
    False

"""


def is_anagram_of_palindrome(word):
    """Is the word an anagram of a palindrome?"""

    # if the word is an anagram of a palindrome, a maximum of one letter would appear once, all others would appear twice

    letter_count = {}
    odd_count = 0

    for letter in word:
    	letter_count[letter] = letter_count.get(letter, 0) + 1

    	# check to see if there is an odd count of letters, if there is, increment the count, if not, decrement the count
    	if letter_count[letter] % 2 != 0:
    		odd_count += 1
    	else:
    		odd_count -= 1

    if odd_count > 1:
    	return False

    return True

if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TEST PASSED. AWESOMESAUCE!\n")
