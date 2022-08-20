# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

    def get_max_index(arr):
        maxy = -1
        max_idx = -1
        for idx, i in enumerate(arr):
            if maxy < i:
                maxy = i
                max_idx = idx
        
        return maxy, max_idx

    def solution(S, B):
        # write your code in Python 3.6
        result = []

        N = len(B)    
        available_sum = sum(B)

        for i in range(N):
            val, idx = get_max_index(B)

            res = S * val / available_sum
            res = f"{res:.2f}"
            result.append(res)

            del B[idx]

            res = float(res)
            available_sum = available_sum - val
            S = S - res
            if S <= 0:
                break

        return result

print(solution(300.01, [300, 200,100]))

