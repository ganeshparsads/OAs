class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels_map = {}
        for i in range(1, 27):
            vowels_map[chr(96+i)] = i

        hash_table, prefix = {}, 0
        hash_table[0] = [-1]
        for i, c in enumerate(s):
            prefix ^= (1 << vowels_map[c])
            if prefix not in hash_table:
                hash_table[prefix] = []
            if len(hash_table[prefix]) <= 1:
                hash_table[prefix].append(i)
            else:
                hash_table[prefix][-1] = i
        print(hash_table)

        result = 0
        for i in range(1<<5):
            if i in hash_table and i^0 in hash_table:
                result = max(result, hash_table[i][-1]-hash_table[i^0][0])
        return result

obj = Solution()
print(obj.findTheLongestSubstring("bdaaadadb"))
print(obj.findTheLongestSubstring("abacb"))
print(obj.findTheLongestSubstring("zthtzh"))
