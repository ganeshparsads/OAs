import heapq
from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        heap = []
        
        letter_dict = dict(Counter(s))
        
        for key, value in letter_dict.items():
            heapq.heappush(heap, (-value, key))
        

        result = ""
        
        while heap:
            (value, key) = heapq.heappop(heap)
            result += key * -value
        
        return result

obj = Solution()

print(obj.frequencySort('aabbbb'))
