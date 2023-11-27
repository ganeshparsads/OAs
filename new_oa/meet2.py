import heapq

def minMeetingRooms(intervals):
        size = len(intervals)
        if size<=1: return size
        heap = []
        for interval in sorted(intervals):
            if heap and interval[0]>heap[0]:
                heapq.heappushpop(heap,interval[1])
            else:
                heapq.heappush(heap,interval[1])
        return len(heap)


print(minMeetingRooms([[1, 7],[8, 9],[3, 6], [9,14],[6,7]]))

print(minMeetingRooms([[2, 5],[1, 3],[5, 8], [5, 6],[8,12]]))
