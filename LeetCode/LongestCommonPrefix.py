class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ""
        min_len = float("inf")
        for str in strs:
            if len(str) < min_len:
                min_len = len(str)
        for i in range (min_len):
            start_symbol = strs[0][i]
            #print(start_symbol)
            if all(s[i] == start_symbol for s in strs):
                prefix += start_symbol
            else:
                break
        #print(prefix)
        return prefix
#print(Solution().longestCommonPrefix(["flower","flow","flight"]))