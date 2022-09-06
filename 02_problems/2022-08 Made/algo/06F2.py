def delivery():
    # TEST 1
    n = 4
    m = 4
    T = 3
    dict_data = {1:1, 2:1, 3:1, 4:1}

    list_input = [int(i) for i in input().split()]
    n = list_input[0] # суммарное число заказов
    m = list_input[1] # ограничение на число заказов за один вызов курьера
    T = list_input[2] # ограничение на время отправки

    dict_data = {}

    for i in range(n):
        ti = int(input().split()[0])
        if ti in dict_data:
            dict_data[ti] += 1
        else:
            dict_data[ti] = 1


    sum_oip = [] # sum orders in period
    sum_oip.append(0)

    t0 = list(sorted(dict_data.keys()))[0]
    items = sorted(dict_data.items())
    sum_d = 0
    
    i = 0
    while(i < len(items)):
        ti, ni = items[i]
        if ti <= t0 + T:
            sum_oip[-1] += ni
            i += 1
        else:
            t0 = ti
            tip = items[i-1][0]
            d = 0
            if ti <= tip + T:
                if sum_oip[-1] // m > 0:
                    d = sum_oip[-1] % m
                    sum_oip[-1] -= d
                t0 = tip
            sum_oip.append(0)
            sum_oip[-1] += d + ni
            i += 1

    sum_d = 0 # sum of deliveries
    for i in sum_oip:
        if i % m == 0:
            sum_d += i // m
        else:
            sum_d += (i // m) + 1

    return sum_d

print(delivery())