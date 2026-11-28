class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # create dictionaries for freq of each string's characters
        s_count, t_count = defaultdict(int), defaultdict(int) 

        # for each index i, add 1 to the count of char=s[i] in s_count and, char=t[i] in t_count
        for i in range(len(s)): 
            s_count[s[i]] += 1
            t_count[t[i]] += 1

        return s_count == t_count
        
        