count = 0
for i in range(145852, 616943):
    int_list = [x for x in map(int, str(i))]
    if len(set(int_list)) > 5 \
            or int_list[0] > int_list[1] \
            or int_list[1] > int_list[2] \
            or int_list[2] > int_list[3] \
            or int_list[3] > int_list[4] \
            or int_list[4] > int_list[5]:
        continue
    elif len(set(int_list)) < 5:
        int_counter = {}
        for integer in int_list:
            c = int_counter.setdefault(integer, 0) + 1
            int_counter[integer] = c
        if 2 in int_counter.values():
            count += 1
    else:
        count += 1
print(count)
