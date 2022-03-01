import re
import time

FILENAME = "C:/Users/Joe_F/Downloads/all_valid_nerdle_sentences.txt"

"""
This module will write all valid nerdle sentences to a file named FILENAME
This takes <20 seconds on a Windows 10 laptop with Intel Core i7

A valid "sentence" is "lhs=rhs" of length 8 that is true and obeys all the other nerdle rules
all lhs are created iteratively
all rhs are crated using the python built-in eval() function, so rhs=eval(lhs)
"""


def find_all_valid_sentences() -> list:
    """
    Creates all possible strings of length 4, 5 and 6 that will be on lhs of equation
    Of those 3,829,880 possible strings all but 17,723 are rejected by validate() function

    :return: list of valid sentences
    """
    validate_count = 0
    dig_operators = '0123456789+-*/'
    dig_no_zero = '123456789'
    dig_with_zero = '0123456789'
    valid_sentences = []
    # tried a recursive fn to do this, but it was way too slow versus iteration and more difficult to read
    for first in dig_no_zero:
        for second in dig_operators:
            for third in dig_operators:
                for fourth in dig_operators:
                    lhs4 = first + second + third + fourth
                    validate_count += 1
                    if validate(lhs4):
                        valid_sentences.append(f'{lhs4}={int(eval(lhs4))}')
                    for fifth in dig_operators:
                        lhs5 = lhs4 + fifth
                        validate_count += 1
                        if validate(lhs5):
                            valid_sentences.append(f'{lhs5}={int(eval(lhs5))}')
                        for sixth in dig_with_zero:
                            lhs6 = lhs5 + sixth
                            validate_count += 1
                            if validate(lhs6):
                                valid_sentences.append(f'{lhs6}={int(eval(lhs6))}')
    print(f'tried to validate {validate_count} strings - most failed!!')
    return valid_sentences


"""
Here are the patterns that the regular expression re module will use in validate()
pattern1 = re.compile("\d+[*+\-/]\d+")  # must have digits, operator, digits
pat1 = re.compile(".*[*+\-/]{2}")   # must not have 2 adjacent operators
pat2 = re.compile(".*[*+\-/]0")     # must not have operator followed by zero
pat3 = re.compile(".*[*+\-/]$")     # must not end with an operator
for performance reasons, pat1 - pat3 are combined with pipe symbol into pattern_combined
"""
pattern1 = re.compile("\d+[*+\-/]\d+")  # must have digits, operator, digits
pattern_combined = re.compile("(.*[*+\-/]{2})|(.*[*+\-/]0)|(.*[*+\-/]$)")  # must not have these patterns


def validate(lhs: str) -> bool:
    """
    Takes a proposed lhs of a nerdle sentence.
    Checks that it is a valid nerdle lhs and that it passes eval()
    eval() creates the rhs
    if eval() produces an integer result (or a float with decimal part = 0)
    and the total length of lhs plus the equals sign plus the rhs equals 8
    then the lhs is good and the function returns True, otherwise False
    :return:
    :param lhs: a string to be validated as a potential lhs of a nerdle sentence
    :return: True if lhs evals to a non-neg integer and length of "lhs=rhs" = 8
    otherwise False
    """
    if not bool(pattern1.match(lhs)):  # check for required "digits operator digits" pattern
        return False
    elif bool(pattern_combined.match(lhs)):  # check the other crazy pattern to reject badly formed lhs
        return False
    else:
        """
        Did use try as follows - but since all strings that make it this far can make it through eval() without error, removed
        the try for performance reasons
            try:
                rhs = eval(lhs)
            except:
                print(f'{lhs} failed eval()')
                return False
        """
        rhs = eval(lhs)
        if rhs < 0 or rhs != int(rhs):
            return False
        rhs = int(rhs)
        if len(f'{lhs}={str(rhs)}') == 8:
            return True
    return False


def write_file(valid_sentences: list) -> int:
    with open(FILENAME, "w") as f:
        for sentence in valid_sentences:
            f.write(sentence + "\n")
    return len(valid_sentences)


def main():
    print(f'Creating all 17,723 valid nerdle sentences and writing to {FILENAME} Should take <20 seconds')
    tic = time.perf_counter()
    valid_sentences = find_all_valid_sentences()
    number_of_sentences = write_file(valid_sentences)
    toc = time.perf_counter()
    print(f'Wrote {number_of_sentences} in {round(toc - tic, 3)} seconds to {FILENAME}')


if __name__ == "__main__":
    main()
