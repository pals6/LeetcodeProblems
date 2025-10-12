def prime_frequency_map(matrix):
    freq = {}
    for row in matrix:
        for val in row:
            if is_prime(val):              # given helper
                freq[val] = freq.get(val, 0) + 1
    return freq
