from itertools import islice, permutations
import math


def lexicographically_permutate(tuple_of_digits: tuple, target: int) -> str:
    """Targeted Permutation of list of numbers

        Args:
            tuple_of_digits: tuple of numbers provided by the user to be permuted
            target: a number which indicates which permutation is of interest

        Returns:
            The targeted permutation
            Ex:
            lexicographically_permutate((1, 2, 3), 1)
            -> 123

        Raises:
            Error: if the target falls out of the range of possible permutations
    """
    possible_permutations = math.factorial(len(tuple_of_digits))

    if target <= possible_permutations:
        digit_permutations = permutations(tuple_of_digits)
        digits = next(
            islice(
                digit_permutations, target - 1, target
            )
        )
        targeted_permutation = ''.join(map(str, digits))
        return targeted_permutation

    else:
        return f"There are not {target} permutations of the numbers"


print(lexicographically_permutate((0, 1, 2, 3, 4, 5, 6, 7, 8, 9), 1000000))
