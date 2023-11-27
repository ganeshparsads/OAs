import pdb

def ngr(arr):

    result = []
    stack = []

    for i in arr[::-1]:
        print(i)

        while stack and i > stack[-1]:
            stack.pop()

        if not stack:
            result.append(-1)
        else:
            result.append(stack[-1])

        stack.append(i)

    return result[::-1]

def ngl(arr):

    result = []
    stack = []

    for i in arr:

        while stack and i > stack[-1]:
            stack.pop()

        if not stack:
            result.append(-1)
        else:
            result.append(stack[-1])

        stack.append(i)

    return result

def nsr(arr):
    result = []
    stack = []

    for i in arr[:]:

        while stack and i < stack[-1]:
            stack.pop()

        if not stack:
            result.append(-1)
        else:
            result.append(stack[-1])

        stack.append(i)

    return result

def nsl(arr):

    result = []
    stack = []

    for i in arr:

        while stack and i > stack[-1]:
            stack.pop()

        if not stack:
            result.append(-1)
        else:
            result.append(stack[-1])

        stack.append(i)

    return result

ip = [1, 3, 2, 4]

print(ngl(ip))
