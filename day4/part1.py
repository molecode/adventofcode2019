start = 145852
end = 616942

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
    count += 1
print(count)
