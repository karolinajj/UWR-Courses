# Idea:
# We slide a window of length n over the array
# For each window position, we count the number of '1's inside it (using prefix[])
# We track the maximum count found in any of these windows.
# bits to switch = (n − (max_count in the window range)) + (number of ’1’s outside this range)

def count_prefix(bits,n):
    prefix = [0] * n
    ones = 0

    if bits[0] == '1':
        prefix[0] = 1
        ones += 1

    for i in range(1, n):
        if bits[i] == '1':
            prefix[i] = prefix[i - 1] + 1
            ones += 1
        else:
            prefix[i] = prefix[i - 1]

    return prefix, ones

def count_ones_in_window(d,prefix,n):
    if d == 0:
        max_count = 0
    else:
        max_count = prefix[d - 1]

        for i in range(d, n):
            max_count = max(max_count, prefix[i] - prefix[i - d])
    
    return max_count

def opt_dist(bits, d):
    n = len(bits)
    prefix, ones = count_prefix(bits,n)
    max_count = count_ones_in_window(d,prefix,n)
    result = (d - max_count) + (ones - max_count)
    return result

# bits = "0010001000"
# d = 5
# print(opt_dist(bits, d))

results = open('zad4_output.txt', 'w', encoding='utf-8')

with open('zad4_input.txt', 'rb') as lines:
    for line in lines:
        line = line.decode('utf-8').strip()
        if line:
            bits, d = line.split(' ')
            d = int(d)
            result = opt_dist(bits, d)
            results.write(str(result) + '\n')
            # results.write('\n')

lines.close()
results.close()