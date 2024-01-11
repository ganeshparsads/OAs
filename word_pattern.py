class Solution:
    def wordPattern(self, s: str, t: str):
        letter_dict = {}
        visited_set = set()
        
        t = t.split(" ")
        
        n = len(s)
        
        if n != len(t):
            return False
        
        for i in range(n):
            src = s[i]
            term = t[i]
            if src not in letter_dict:
                if term in visited_set:
                    print("hiii")
                    return False
                
                letter_dict[src] = term
                visited_set.add(term)

        return True


obj = Solution()

print(obj.wordPattern("abba", "dog cat cat dog"))
