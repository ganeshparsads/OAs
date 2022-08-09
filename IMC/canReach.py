from math import sqrt, floor, ceil

def canReach(c, x1, y1, x2, y2):
    if helper(c, x1, y1, x2, y2):
        return "Yes"

    return "No"

def helper(c, x1, y1, x2, y2):
    start = sqrt(x1 + y1)
    end = sqrt(x2 + y2)

    if (floor(start) == ceil(start)) or (floor(end) == ceil(end)) or x1 > x2 or y1 > y2:
        return False

    if (x1 == x2 and y1 == y2) or (x1+c == x2 and y1+c == y2):
        return True

    return helper(c, x1+c, y1+c, x2, y2) or helper(c, x1+y1, y1, x2, y2) or helper(c, x1, x1+y1, x2, y2)


def canReach1(c, x1, y1, x2, y2):
    stack = []

    stack.append((x1, y1))

    end = sqrt(x2+y2)

    if floor(end) == ceil(end):
        return "No"

    while(stack):
        p1, q1 = stack.pop()

        start = sqrt(p1+q1)

        if (floor(start) == ceil(start)) or p1 > x2 or q1 > y2:
            continue

        if (p1 == x2 and q1 == y2) or (p1+c == x2 and q1+c == y2):
            return "Yes"

        if p1 + c < x2 and q1+c < y2:
            stack.append((p1+c, q1+c))

        if p1 + q1 < x2:
            stack.append((p1+q1, q1))
        if p1 + q1 < y2:
            stack.append((p1, p1+q1))

    return "No"

print(canReach1(1, 1, 4, 7, 6))
print(canReach1(1, 4, 3, 6, 4))
