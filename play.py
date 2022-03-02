import solver
import create_valid_nerdle_sentences


def play(all: list) -> None:
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
            answe = solver.score(guess, secret)
            print(f'score              -> {answe}')

        for trial in trials:
            if solver.score(guess, trial) == answe:
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

            e = solver.entropy(x,possible_secrets)  # change possible_secrets to all to calculate.
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
        #     e = solver.entropy(x, possible_secrets)
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


def main():
    print(f'{create_valid_nerdle_sentences.FILENAME=}')
    with open(create_valid_nerdle_sentences.FILENAME) as f:
        all = [line.rstrip('\n') for line in f]
    play(all)


if __name__ == "__main__":
    main()

# uncomment to write possible answers to file
# tic = time.perf_counter()
# write_file()
# toc = time.perf_counter()
# print(f'took {round(toc - tic, 3)} seconds')


# sample = ['11-1-1=9', '48-32=16', '48-36=12', '12-35=47','12345=78']
# for el in sample:
#     print(f'{el} has entropy {entropy(el, all):.2f}')
# play(all)
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


# secret = 'babb-bab'
# guess = 'bbaabbba'
# print(f'{secret}')
# print(f'{guess}')
# print(f"{solver.score(guess, secret)}")

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
