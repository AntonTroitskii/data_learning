def func1(l: list):

    maxa = max(l)
    res = {}
    if maxa % 2 == 0:
        d = maxa // 2
        for i in l:
            res[int(abs(d-i))] = i
    else:
        d = maxa // 2 + 1
        for i in l:
            res[int(abs(d-i))] = i

    return sorted(res.items())[0][1]    

def comb():
    str_input = input()
    list_input = [int(i) for i in str_input.split()]
    m = list_input[0]

    str_input = input()
    a = [int(i) for i in str_input.split()]
    a.sort()
    maxa = a[-1]

    return maxa, func1(a)

        
a, b = comb()

print(a, b)