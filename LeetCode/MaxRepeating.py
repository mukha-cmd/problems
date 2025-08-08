class Solution(object):
    def maxRepeating(self, sequence, word):
        """
        :type sequence: str
        :type word: str
        :rtype: int
        """
        if word is None:
            return True
        pointer = 0
        for c in sequence:
            if word[pointer] == c and pointer < len(word):
                pointer += 1
            if pointer == len(word):
                return True
        return False
print(Solution().maxRepeating("abcdefg", "abc"))
print(Solution().maxRepeating("abdefg", "abc"))
print(Solution().maxRepeating("ababc", "ac"))
