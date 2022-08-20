intervals = (
    ('w', 604800),  # 60 * 60 * 24 * 7
    ('d', 86400),    # 60 * 60 * 24
    ('h', 3600),    # 60 * 60
    ('m', 60),
    ('s', 1),
)

def display_time(seconds):
    result = []
    time_frame = []

    for name, count in intervals:
        value = seconds // count
        if value:
            seconds -= value * count
            if value == 1:
                name = name.rstrip('s')
            # result.append(value)
            time_frame.append(name)
            result.append(value)

    # # return ''.join(result)
    # print(result)
    # print(time_frame)

    res_len = len(result)

    if res_len > 2:
        for i in range(res_len - 1, 1, -1):
            if result[i]:
                result[i-1] += 1

    final_string = []
    for idx, i in enumerate(result[:2]):
        final_string.append('{}{}'.format(result[idx], time_frame[idx]))

    return ''.join(final_string)

print(display_time(100))
print(display_time(7263))
print(display_time(777263))
print(display_time(5))
