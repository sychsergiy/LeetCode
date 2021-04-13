"""
https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/589/week-2-march-8th-march-14th/3665/
"""


class Slice:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def len(self):
        return self.end - self.start

    def apply(self, string):
        return string[self.start:self.end]

    def apply_inverse(self, string):
        return string[:self.start] + string[self.end:]

    def is_nearest_neighbours_palindromic(self, string):
        if string[self.start - 1] == string[self.end]:
            return True
        return False

    def increment_right(self):
        self.end += 1

    def increment(self):
        self.end += 1
        self.start -= 1

    @classmethod
    def null(cls):
        return cls(0, 0)

    def is_null(self):
        return self.start == 0 and self.end == 0

    def __gt__(self, other):
        return self.len() > other.len()

    def __lt__(self, other):
        return self.len() < other.len()

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end


class Solution(object):
    def __init__(self):
        self.the_longest_slices = [Slice.null()]

    def removePalindromeSub(self, s):
        """
        :type s
        :rtype: int
        """
        # start from the middle

        # check the nearest  neighbours until palindrome

        # when not palindrome stop

        # save result(the longest palindrome subseq at the moment)

        # start the check starting from each neighbour

        # if the slice between current middle item and left or right edge is less  than longest subseq len/2
        #   there is not sense to check futher

        # remove the longest subseq

        # recursive call for the smallr string
        return self.remove_the_longest_palindrome(s)

    def find_the_longest_palindromes(self, string):
        if self.the_longest_slices[0].len() > len(string):
            return

        middle_element_index = len(string) // 2

        if len(string) % 2 == 0:
            # aabb
            middle_slice = Slice(middle_element_index, middle_element_index)
        else:
            middle_slice = Slice(middle_element_index, middle_element_index + 1)

        while middle_slice.start > 0 and middle_slice.end < len(string):
            if middle_slice.is_nearest_neighbours_palindromic(string):
                middle_slice.increment()
            else:
                break

        if middle_slice > self.the_longest_slices[0]:
            self.the_longest_slices = [middle_slice]
        elif middle_slice.len() == self.the_longest_slices[0].len():
            self.the_longest_slices.append(middle_slice)

        self.find_the_longest_palindromes(string[1:])
        self.find_the_longest_palindromes(string[:len(string) - 1])

    def remove_the_longest_palindrome(self, string):
        if len(string) == 1:
            return 1
        if len(string) == 0:
            return 0

        self.the_longest_slices = [Slice.null()]
        self.find_the_longest_palindromes(string)

        if len(self.the_longest_slices) == 1:
            string = self.the_longest_slices[0].apply_inverse(string)
            return 1 + self.remove_the_longest_palindrome(string)
        else:
            k = [self.remove_the_longest_palindrome(i.apply_inverse(string)) for i in self.the_longest_slices]
            return 1 + min(k)
            # return self.the_longest_slices.apply_inverse(string)


import unittest


class PalindromeTestCase(unittest.TestCase):
    def test_big_number(self):
        self.assertEqual(Solution().removePalindromeSub("ab" * 10 ** 2), 2)

    def test_edge_cases(self):
        self.assertEqual(Solution().removePalindromeSub("a"), 1)
        self.assertEqual(Solution().removePalindromeSub(""), 0)

    def test_one_step_case(self):
        self.assertEqual(Solution().removePalindromeSub("ababa"), 1)
        self.assertEqual(Solution().removePalindromeSub("aabaa"), 1)

    def test_ok(self):
        self.assertEqual(Solution().removePalindromeSub("baabb"), 2)
        self.assertEqual(Solution().removePalindromeSub("aab"), 2)

        self.assertEqual(Solution().removePalindromeSub("abb"), 2)
        self.assertEqual(Solution().removePalindromeSub("bb"), 1)
        self.assertEqual(Solution().removePalindromeSub("ababb"), 2)

    def test_error(self):
        self.assertEqual(Solution().removePalindromeSub("abbaaaab"), 2)
