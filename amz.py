import heap

def topKFrequent()
        freq = {}
        for i in nums:
            if i not in freq:
                freq[i] = 0
            freq[i] += 1
        
        minHeap = []
        
        for key, value in freq.items():
            if len(minHeap) < k:
                heapq.heappush(minHeap, (value, key))
            else:
                if minHeap[0][0] < value:
                    heapq.heappop(minHeap)
                    heapq.heappush(minHeap, (value, key))
        
        result  = []
        for each in minHeap:
            result.append(each[1])
        
        return result


for i in range()