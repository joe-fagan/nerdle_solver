import collections
import math
import re
import time
from functools import lru_cache
import random

FILENAME = "C:/Users/Joe_F/Downloads/all_valid_nerdle_sentences.txt"
pattern1 = re.compile("\d+[*+\-/]\d+")  # must have digits, operator, digits
# pat1 = re.compile(".*[*+\-/]{2}")   # must not have 2 adjacent operators
# pat2 = re.compile(".*[*+\-/]0")     # must not have operator followed by zero
# pat3 = re.compile(".*[*+\-/]$")     # must not end with an operator
# for performance reasons, pat2 - pat4 are combined with pipe symbol
pattern_combined = re.compile("(.*[*+\-/]{2})|(.*[*+\-/]0)|(.*[*+\-/]$)")

def validate(lhs):
    # if '+' not in lhs and '-' not in lhs and '/' not in lhs and '*' not in lhs or '**' in lhs:
    #     # print(f'{sent} has no operator or has **')
    #     return False
    if not bool(pattern1.match(lhs)):  # check for required "digits operator digits" pattern
        # print(f'failed at 1: {lhs} must contain digit, single operator, digit ')
        return False
    elif bool(pattern_combined.match(lhs)):
        return False
    else:
        # try:
        #     rhs = eval(lhs)
        # except:
        #     print(f'{lhs} failed eval()')
        #     return False
        rhs = eval(lhs)
        if rhs < 0 or rhs != int(rhs):
            return False
        rhs = int(rhs)
        if len(f'{lhs}={str(rhs)}') == 8:
            # print(len(f'{str(lhs)}={str(rhs)}'))
            # print(f'{sent}={res} ')
            return True
    # print('failed at 3')
    return False



def find_all_valid_sentences():
    dig_operators = '0123456789+-*/'
    dig_no_zero = '123456789'
    dig_with_zero = '0123456789'
    valid_sentences = []
    for first in dig_no_zero:
        for second in dig_operators:
            for third in dig_operators:
                for fourth in dig_operators:
                    lhs4 = first + second + third + fourth
                    if validate(lhs4):
                        valid_sentences.append(f'{lhs4}={int(eval(lhs4))}')
                    for fifth in dig_operators:
                        lhs5 = lhs4 + fifth
                        if validate(lhs5):
                            valid_sentences.append(f'{lhs5}={int(eval(lhs5))}')
                        for sixth in dig_with_zero:
                            lhs6 = lhs5 + sixth
                            if validate(lhs6):
                                valid_sentences.append(f'{lhs6}={int(eval(lhs6))}')
    return valid_sentences





def write_file():
    valid_sentences = find_all_valid_sentences()

    with open(FILENAME, "w") as f:
        for sentence in valid_sentences:
            f.write(sentence + "\n")

    print(f'writing {len(valid_sentences)} to {FILENAME}')


def score(guess, secret):
    sco = ['0'] * len(guess)
    matched_in_secret = [False] * len(guess)  # keep track of what's matched already to stop double counting
    for g_ind, g in enumerate(guess):
        for s_ind, s in enumerate(secret):
            if g == s:
                if not matched_in_secret[s_ind]:
                    sco[g_ind] = '2' if g_ind == s_ind else '1'
                    matched_in_secret[s_ind] = True
                    break
    score=''
    return score.join(sco)


def entropy(guess, possiblilities):
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


def play():
    """
    Plays the game
    FYI first guess has max entropy guess is 48-32=16 with entropy 9.77

    :return:
    """
    # secret = random.choice(all)
    # print(f'random secret is ->{secret}')
    # secret = '3*42=126'
    secret = '6-8+10=8'
    guess = "48-32=16"
    # guess = '3+4*6=27'
    game_on = True
    # Start with trials being all possible answers

    trials = all[:]

    while (game_on):
        possible_secrets = []
        print(f'try                -> {guess}')
        print(f'press y to accept or enter your own guess')
        x = input('                   -> ')
        if x != 'y':
            guess = x
            print(f'guess is           -> {guess}')

        answe = input(f'enter score (or y) -> ')
        if answe == 'q':
            game_on = False
            continue
        if answe == 'y':
            answe = score(guess, secret)
            print(f'score              -> {answe}')

        for trial in trials:
            if score(guess, trial) == answe:
                possible_secrets.append(trial)

        if len(possible_secrets) == 1:
            print(f'Secret found       -> {possible_secrets[0]}')
            game_on = False
            continue



        for element in possible_secrets:
            print(f'possible secret     -> {element}')
        print(f'There are {len(possible_secrets)} possible secrets')

        # replace trials with possible_secrets
        trials = possible_secrets[:]
        # pick the first one
        # print(f'about to call entropy on {guess} on {len(possible_secrets)} possibilites ')
        # guess = all[0]
        ent = []
        maxent = 0
        max_guess = ''
        deltat = 0
        for x in all:
            deltat += 1
            if deltat % 100 == 0:
                print('.', end='')
                if deltat % 8000 == 0:
                    print('+')

            e = entropy(x, all) # change possible_secrets to all to calculate 1st guess max entropy.
            ent.append(e)
            if e > maxent:
                maxent = e
                max_guess = x
        print('')
        # I now have a max entropy guess
        # but if one of the possible_secrets has the same max entropy, choose that as next guess

        # ent_p = []
        # maxent_p = 0
        # max_guess_p = ''
        # for x in possible_secrets:
        #     e = entropy(x, possible_secrets)
        #     ent_p.append(e)
        #     if e > maxent_p:
        #         maxent_p = e
        #         max_guess_p = x
        # # compare maxent with maxent_p
        #
        # if maxent_p == maxent:
        #     print(f'found a guess of maximum entropy in possible secrets')
        #     guess = max_guess_p
        # else:
        #     guess = max_guess
        guess = max_guess

        print(f'max entropy guess is {max_guess} with entropy {round(maxent, 2)}')
        # call

        #
        # for x in ent:
        #     print(round(x,2))


# uncomment to write possible answers to file
# tic = time.perf_counter()
# write_file()
# toc = time.perf_counter()
# print(f'took {round(toc - tic, 3)} seconds')


with open(FILENAME) as f:
    all = [line.rstrip('\n') for line in f]

# sample = ['11-1-1=9', '48-32=16', '48-36=12', '12-35=47','12345=78']
# for el in sample:
#     print(f'{el} has entropy {entropy(el, all):.2f}')
play()
# secret = 'babb-bab'
# guess  = 'bbaabbba'
# tic = time.perf_counter()
# for _ in range(1100_000):
#     score(guess, secret)
# toc = time.perf_counter()
# print(f'score too took {round(toc - tic, 3)} seconds')
# tic = time.perf_counter()
# for _ in range(1100_000):
#     score_old1(guess, secret)
# toc = time.perf_counter()
# print(f'score too took {round(toc - tic, 3)} seconds')



secret = 'babb-bab'
guess  = 'bbaabbba'
print(f'{secret}')
print(f'{ guess}')
print(f"{score(guess, secret)}")

# import time
# import sys
#
# toolbar_width = 40
#
# # setup toolbar
# sys.stdout.write("[%s]" % (" " * toolbar_width))
# sys.stdout.flush()
# sys.stdout.write("\b" * (toolbar_width+1))  # return to start of line, after '['
#
# for i in range(toolbar_width):
#     time.sleep(0.1) # do real work here
#     # update the bar
#     sys.stdout.write("-")
#     sys.stdout.flush()
#
# sys.stdout.write("]\n")  # this ends the progress bar


# guess ='10-8+6=8'
# print(score(guess, secret))

# print(f'number of possible secrets = {len(all)}')
# guess = '12+35=47'
# answe = '20000100'
#
# # jack = score(guess,'9/3*4=12')
# # print(f'score guess,12+80=97 {jack}')
# guess1 = '11-8+3=6'
# answe1 = '21111021'
#
#
# for trial in all:
#     if score(guess, trial) == answe:
#         possible_secrets.append(trial)
#
#
# #
# for trial in possible_secrets:
#     if score(guess1, trial) == answe1:
#         print(trial)
#
#
# # print(validate('9/3*4'))
