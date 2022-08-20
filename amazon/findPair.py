a = 'abcd'
b = 'xbddea'

def matches(astr, bstr):
    total = 0
    i = 0
    while i<len(astr) and i<len(bstr):
        if astr[i] == bstr[i]:
            total += 1
        i += 1

    print(total)
    return total


matches(a, b)