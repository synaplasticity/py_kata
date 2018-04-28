def race(first, second, lead):
    if first <= 0 or second <= 0 or lead <= 0:
        return None

    if first >= second:
        return None
    # else:
    #     return [-1, -1, -1]

    a_pos = lead
    b_pos = 0
    i = 0
    while round(a_pos - b_pos) != 0:
        a_pos += 2
        b_pos += 2.4
        i += 1
        print('a :' + str(a_pos) + 'b :'
          + str(b_pos) +
          'time:' + str(i))
