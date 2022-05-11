import random


class bcolors:
    """
    Colors for terminal text
    """
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def coinflip(n: int) -> str:
    """
    Generator for flipit

    Args:
        n: number of coin flips

    Yields:
        heads or tails
    """
    for _ in range(n):
        yield "heads" if random.randint(1, 2) == 1 else "tails"


def flipit(n: int = 10) -> list:
    """
    Generates result of n coin flips

    Args:
        n: Best of n

    Returns:
        Result of coin flips
    """
    result = []

    for flip in coinflip(n):
        result.append(flip)

    return result


def flips_info(flips: list, print_info: bool = False):
    """
    Generates flipped coins statistics

    Args:
        flips: list of coin flips
        print_info: Prints statistics in console. Defaults to False.

    Returns:
        heads, tails, probability of heads, probabilitiy of tails, majority
    """
    heads = flips.count('heads')
    tails = flips.count('tails')

    pheads = 100 * (flips.count('heads')/len(flips)) // 0.01 / 100
    ptails = 100 * (flips.count('tails')/len(flips)) // 0.01 / 100

    majority = max(set(flips), key=flips.count)

    if print_info:
        print('\n' * 10)
        print(bcolors.OKBLUE + "HEADS: " + bcolors.ENDC, heads)
        print(bcolors.OKBLUE + "TAILS: " + bcolors.ENDC, tails)
        print()
        print(bcolors.OKCYAN + "p(HEADS): " +
              bcolors.ENDC, f"{pheads:0.3f}", '%', sep='')
        print(bcolors.OKCYAN + "p(TAILS): " +
              bcolors.ENDC, f"{ptails:0.3f}", '%', sep='')
        print()

        print(bcolors.OKGREEN + "MAJORITY:", bcolors.FAIL + bcolors.BOLD + bcolors.UNDERLINE +
              majority + bcolors.ENDC)
        print()

    return (heads, tails, pheads, ptails, majority)


if __name__ == "__main__":
    flips = flipit()
    flips_info(flips, True)
