from itertools import islice, permutations
import math


def lexicographically_permutate(tuple_of_digits, target) -> str:

    # calculate the total number of permutations that are possible
    possible_permutations = math.factorial(len(tuple_of_digits))

    # if the target is less than the total permutations:
    if target <= possible_permutations:

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

        # return the permutation of interest
        return ans

    # if there are fewer permutations than the target:
    else:

        # return an error message
        return f"There are not {target} permutations of the numbers"


print(lexicographically_permutate((0, 1, 2, 3, 4, 5, 6, 7, 8, 9), 1000000))
