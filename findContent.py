class Solution:
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        
        i, j = 0, 0
        
        n = len(g)
        m = len(s)
        
        result = 0
        
        while i < n and j < m:
            if g[i] <= s[j]:
                i+=1
                j+=1
                result += 1
            
            elif g[i] > s[j]:
                j += 1
            
        return result
                

obj = Solution()

print(obj.findContentChildren([1,2,3], [1,2]))
