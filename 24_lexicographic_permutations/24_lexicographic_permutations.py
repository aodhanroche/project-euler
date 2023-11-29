from itertools import islice, permutations


def lexicographically_permutate(tuple_of_digits, target):
    # set a variable for the itertools permutation of the tuple
    digit_permutations = permutations(tuple_of_digits)

    # slice the digit_permutation obj to the permutation of the tuple you are targeting
    digits = next(
        islice(
            digit_permutations, target - 1, target
        )
    )

    # join the tuple digits into a str
    ans = ''.join(map(str, digits))

    return ans


print(lexicographically_permutate((0, 1, 2, 3, 4, 5, 6, 7, 8, 9), 1000000))


