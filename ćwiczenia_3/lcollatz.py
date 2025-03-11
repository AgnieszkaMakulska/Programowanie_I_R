limit = int(1e6)

def collatz_length(k):
    c = [k]
    n = 1
    while c[-1] != 1:
        if c[-1] % 2 == 0:
            c.append(int(0.5 * c[-1]))
        elif c[-1] % 2 != 0:
            c.append(int(3 * c[-1] + 1))
        n += 1
    return n

def longest_collatz(limit):
    max_length = 0
    k_with_max_length = 0
    for k in range(1,limit):
        length = collatz_length(k)
        if length > max_length:
            max_length = length
            k_with_max_length = k
    return max_length, k_with_max_length

max_len, k_max_len = longest_collatz(limit)
print('Ciąg Collatza dla k = ', k_max_len, ' ma ', max_len, ' wyrazów przed pierwszym wyrazem o wartości 1.')