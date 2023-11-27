import sys

class Solution(object):
    def optimal_utilization(self, a, b, target):
        temp_value = -sys.maxsize - 1
        a_value_list = sorted(a, key=lambda x: x[1])
        b_value_list = sorted(b, key=lambda x: x[1])
        left = 0
        right = len(b_value_list) - 1
        res = []

        while left < len(a_value_list) and right >= 0:
            sum_value = a_value_list[left][1] + b_value_list[right][1]

            if sum_value > target:
                right -= 1
            else:
                if temp_value <= sum_value:
                    if temp_value < sum_value:
                        res = []
                        temp_value = sum_value
                    
                    res.append([a_value_list[left][0], b_value_list[right][0]])
                    count = right

                    while count > 0 and b_value_list[count][1] == b_value_list[count - 1][1]:
                        res.append([a_value_list[left][0], b_value_list[count - 1][0]])
                        count -= 1

                left += 1

        return res

def main():
    a = [[2, 12], [3, 8], [1, 11]]
    b = [[1, 12], [2, 14], [3, 15]]
    target = 14
    solution = Solution()
    res = solution.optimal_utilization(a, b, target)
    print(res)

if __name__ == "__main__": 
    main()
