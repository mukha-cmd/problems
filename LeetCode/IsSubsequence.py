class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s is None:
            return True
        pointer = 0
        for c in t:
            if s[pointer] == c and pointer < len(s):
                pointer += 1
            if pointer == len(s):
                return True
        return False
string1 = 'b'
string2 = 'abcd'
print(Solution().isSubsequence(string1, string2))
