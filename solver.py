# support module for solving nerdle
import collections
import math


def score(guess: str, secret: str) -> str:
    """
    returns the score comparing guess with secret where
    green = 2 when correct character appears in correct place
    orange = 1 where character is correct but in wrong place
    and grey = 0 where character does not appear (or appear again) in secret

    score('abcb','bbcc') will return '0221'
    score will be calculated in a list, and converted to a string and returned
    """
    score = ['0'] * len(guess)
    matched_in_secret = [False] * len(guess)  # keep track of what's matched already to stop double counting
    for g_ind, g in enumerate(guess):
        for s_ind, s in enumerate(secret):
            if g == s:
                if not matched_in_secret[s_ind]:
                    score[g_ind] = '2' if g_ind == s_ind else '1'
                    matched_in_secret[s_ind] = True
                    break
    return ''.join(score)  # .join([ 'a', 'b', 'c']) creates the string 'abc'


def entropy(guess: str, possiblilities: list) -> float:
    """for a given guess and a list of possibilities, calculate the entropy of that guess"""
    l = []
    for poss in possiblilities:
        l.append(score(guess, poss))
    # for i in range(len(l)):
    #     print(l[i], possiblilities[i])
    # using the collections module create a counter dict (sore: count)
    # since I want only to calculate entropy for guess vs possibilities
    # see https://stackoverflow.com/questions/2161752/how-to-count-the-frequency-of-the-elements-in-an-unordered-list
    # for a great primer on collections.Counter()
    counter = collections.Counter(l)
    entropy = 0
    denom = len(l)
    for val in counter.values():
        p = val / denom
        x = -1 * p * math.log2(p)
        entropy += x
    if guess == '48-32=16':
        print(f'counter is {counter}')
        print(f'counter keys{counter.keys()}')
        print(f'counter.values is {counter.values()}')
        print(f'entropy is {entropy}')
    return entropy
