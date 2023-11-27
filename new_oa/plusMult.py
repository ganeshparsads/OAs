
def check_overflow(num):
    if(abs(num) > (2 ** 31 - 1)):
        return True
    return False


def plusMult(A):
    Reven = 1
    Rodd = 1

    eve_mul = True
    odd_mul = True

    for i in range(len(A)):
        if i % 2 == 0:
            if eve_mul:
                if check_overflow(Reven * A[i]):
                    Reven = Reven % 10**9

                Reven = (Reven * A[i])
                eve_mul = False
            else:
                eve_mul = True
                Reven = Reven + A[i]
        else:
            if odd_mul:
                if check_overflow(Rodd * A[i]):
                    Rodd = Rodd % 10**9
                Rodd = (Rodd * A[i]) % 2
                odd_mul = False
            else:
                odd_mul = True
                Rodd = (Rodd + A[i])


    Reven = Reven % 2

    Rodd = Rodd % 2

    if Reven > Rodd:
        return "EVEN"
    elif Rodd > Reven:
        return "ODD"
    else:
        return "NEUTRAL"
