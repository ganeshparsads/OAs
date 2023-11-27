def check(new, old):
    i, j = 0, 0
    while i < len(new) and j < len(old):
        if ord(new[i]) + 1 == 123:
            new_ele = 97
        else:
            new_ele = ord(new[i]) + 1
        if ord(old[j]) == ord(new[i]) or ord(old[j]) == new_ele:
            i += 1
            j += 1
        else:
            i += 1
    return j == len(old)

# newPassword = ["baacbab", "accdb", "baacba"]
# oldPassowrd = ["abdbc", "ach", "abb"]

# newPassword = ["bzz"]
# oldPassowrd = ["az"]

# newPassword = ["aaccbbee", "aab"]
# oldPassowrd = ["bdbf", "aee"]

newPassword = ["aaaa", "bzz"]
oldPassowrd = ["bcd", "az"]

result = []

for i in range(len(oldPassowrd)):
    result.append(check(newPassword[i], oldPassowrd[i]))

print(result)
