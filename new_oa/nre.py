def find_least_smallest_left_elements(rawData):
    nearest_smallest_left_indices = [-1] * len(rawData)
    stack = []

    for i in range(len(rawData)):
        while stack and rawData[i] <= rawData[stack[-1]]:
            stack.pop()
        
        if stack:
            nearest_smallest_left_indices[i] = stack[-1]
        
        stack.append(i)

    return nearest_smallest_left_indices


def find_least_smallest_right_elements(rawData):
    least_smallest_right_elements = [-1] * len(rawData)
    stack = []

    for i in range(len(rawData)):
        while stack and rawData[i] < stack[-1]:
            stack.pop()

        if not stack or rawData[i] > stack[-1]:
            least_smallest_right_elements[i] = stack[-1] if stack else -1

        stack.append(rawData[i])

    return least_smallest_right_elements

# rawData = [3, 1, 4, 5, 2, 6]

def func(rawData, localArea):

    sre = find_least_smallest_right_elements(rawData)

    sle = find_least_smallest_left_elements(rawData)

    result = []

    for i in range(len(rawData)):
        if abs(i-sre[i]) < localArea and (sle[i] == 0 or abs(i-sle[i]) < localArea):
            result.append(i)

    return result
