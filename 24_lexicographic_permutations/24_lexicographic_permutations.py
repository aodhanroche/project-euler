from itertools import islice, permutations


def lexicographically_permutate(range_limit, target):
    digit_permutations = permutations(range(range_limit))
    digits = next(islice(digit_permutations, target - 1, target))
    answer = sum([digit * 10 ** (range_limit - 1 - i) for i, digit in enumerate(digits)])
    return answer

print(lexicographically_permutate(10, 1000000))
