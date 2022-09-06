def delivery():
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
    for ti, ni in sorted(dict_data.items()):
        if ti <= t0 + T:
            sum_oip[-1] += ni
        else:
            t0 = ti
            sum_oip.append(0)
            sum_oip[-1] += ni

    sum_d = 0 # sum of deliveries
    for i in sum_oip:
        if i % m == 0:
            sum_d += i // m
        else:
            sum_d += (i // m) + 1
            
    return sum_d

print(delivery())