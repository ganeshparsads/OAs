# a = [3, 1, 5]
a = [4, 17, 17, 9, 9, 18, 9, 5]
b = [15, 9, 16, 2, 4, 7, 5, 7, 8]
# b = [5, 6, 7]
d = 0

a = sorted(a)

min_a = min(a)
max_a = max(a)

print(min_a)
print(max_a)

min_b = ""
max_b = ""

for i in b:
    if i == 5:
        import pdb
        pdb.set_trace()
    if not min_b and abs(min_a - i) > d:
        min_b = abs(min_a - i)
    elif min_b and abs(min_a - i) > d:

        print(i, abs(min_a - i))
        min_b = min(abs(min_a - i), min_b)

    if not max_b and abs(max_a - i) > d:
        max_b = abs(min_a - i)
    else:
        max_b = max(abs(min_a - i), max_b)

print "here", (min_b, max_b)

cnt = 0

# import pdb
# pdb.set_trace()

for i in a:
    if min_b - abs(min_a - i) <= d:
        break
    cnt += 1

print(cnt)

# for i in a:
#   if abs(min_b - i) <= d:

