def multiple_push_back(a: list, n, m):

    l = [m] * n
    a.extend(l)
    return a


def k_stat():
    str_input = input()
    list_input = [int(i) for i in str_input.split()]
    len_a = list_input[0]
    m = list_input[1]
    k = list_input[2]

    str_input = input()
    list_input = [int(i) for i in str_input.split()]
    a = list_input[0:len_a]

    for i in range(m):
        str_input = input()
        list_input = [int(i) for i in str_input.split()]
        a = multiple_push_back(a, list_input[0], list_input[1])

    a.sort()

    return a[k - 1]


print(k_stat())