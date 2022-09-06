def add_elem(data:dict, elem):
    if elem in data:
        data[elem] += 1
    else:
      data[elem] = 1

def push_bask(data:dict, n, m):
    if m in data:
        data[m] += n
    else:
      data[m] = n

def k_stat2():
    str_input = input()
    list_input = [int(i) for i in str_input.split()]
    
    len_a = list_input[0]
    m = list_input[1]
    k = list_input[2]

    str_input = input()
    list_input = [int(i) for i in str_input.split()]
    dict_data = {}
    for i in list_input:
        add_elem(dict_data, i)

    for i in range(m):
        str_input = input()
        list_input = [int(i) for i in str_input.split()]
        push_bask(dict_data, list_input[0], list_input[1])

    sum = 0
    for i, j in sorted(dict_data.items()):
        sum += j
        if sum >= k:
            return i

print(k_stat2())