# Nerdle Solver
### A solver for Nerdle using Shannon Entropy

Nerdle is Wordle for numeric equations like '12+35=47'

To find out more see https://faqs.nerdlegame.com/

#### How to create all valid sentences
The file **create_valid_nerdle_sentences.py** creates all 17,723 valid sentences and writes them 
to a file according to the global variable FILENAME, specified at the top of the file.
Edit the variable FILENAME to change the name and path of the file.

### Nerdle Solver introduction
The file *play.py* will solve the nerdle i.e. find the *secret*, in the fewest possible attempts 
(almost always 3 attempts, never more than 4). This module reads the file FILENAME created above. 

If you happen to know the secret you can enter it when asked. This will mean the program can calculate the
score for you (ie the Greens, Yellows and Greys) to save you having to calculate this, or enter it from elsewhere.

At each stage the solver will suggest a next guess. You can either accept the guess or choose your own. When
only one possible secret remains or when the score is all greens (2's) the program ends.

#### How to use the solver.

You can use the solver to either 
- play the game and try to solve the secret yourself 
- have the solver find the secret for you

The initial guess is hardcoded into the program (currently 48-32=16) because finding the maximum entropy 
first guess takes about 20 minutes and always produces the same result. There may be others of similar entropy
but this guess is a maximum, and is in fact the 7200'th entry in FILENAME. All guesses before this have 
lower entropy. 

Scoring the guess is entered with 
- Green as 2 - meaning the character is correct and in the correct position 
- Yellow as 1 - meaning the character is correct but in the wrong position
- Grey as 0 - the character is incorrect

A score will like '02210101' 

When the initial guess is scored (either automatically if secret is known or manually entered if not), 
that score is used to calculate all possible secrets that would produce that score. 
Depending on the secret, the possible secrets after the max entropy guess above will reduce the number of possible
secrets to 140. All possible secrets are shown and the next guess is suggested. You can either accept this guess 
or enter your own guess.

Here's an example running on today's nerdle (2nd March 2022)
```
try                -> 48-32=16
press y to accept or enter your own guess
                   -> y
enter score (or y) -> 10112201
Secret found       -> 6*6-2=34
```
<img src="https://github.com/joe-fagan/nerdle_solver/blob/main/nerdle_2-March-2022.PNG" alt="drawing" width="200"/>



#### How does the solver work




