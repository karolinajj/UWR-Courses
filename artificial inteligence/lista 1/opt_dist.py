def count_prefix(bits, n):
    prefix = [0] * n
    ones = 0

    if bits[0] == 1:
        prefix[0] = 1
        ones += 1

    for i in range(1, n):
        if bits[i] == 1:
            prefix[i] = prefix[i - 1] + 1
            ones += 1
        else:
            prefix[i] = prefix[i - 1]

    return prefix, ones

def count_ones_in_window(d, prefix, n):
    if d == 0:
        max_count = 0
    else:
        max_count = prefix[d - 1]

        for i in range(d, n):
            max_count = max(max_count, prefix[i] - prefix[i - d])
    
    return max_count

def opt_dist(bits, d):
    n = len(bits)
    prefix, ones = count_prefix(bits, n)
    max_count = count_ones_in_window(d, prefix, n)
    result = (d - max_count) + (ones - max_count)
    return result

# bits = [0, 0, 1, 0, 0, 0, 1, 0, 0, 0]
# d = 5
# print(opt_dist(bits, d))
