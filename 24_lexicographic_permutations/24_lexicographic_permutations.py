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


# # create a list of digits that be combined to give the answer in an integer form
#     list_of_digits = [
#          create a list of the digits of the target permutation
#          multiply each digit by ten to the power of however far they are from the last digit,
#          so they can be added together
#          ex: if the permutation was 123 the list would be [100, 20, 3]
#         digit * 10 ** (range_limit - 1 - i) for i, digit in enumerate(digits)
#     ]
