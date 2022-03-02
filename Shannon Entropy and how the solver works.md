# Shannon Entropy

If you know what it is, skip this section.

If not here's a simple introduction.
## Guess the celbrity with yes/no questions
Image we're playing a game where you have to figure out which celebrity I've chosen from a shared list 
of say 800 celebrities. You can ask only yes/no questions.

Here are 3 first questions that we can consider.
1. Is the person Tina Turner
2. Is the person an actor/actress
3. Is the person female

Considering these three, we intuitively know that question 1 is not a smart 1st question and 
most people might ask question 2 or 3.

Question 1: Gives us great information if the answer is yes, but if the answer is no, the number of
possible people it can be is now 799. With high probability (p = 799/800 = 99.88%) we will get almost no 
information
Question 2: Assume there are 200 actors. If the answer is yes, we've reduced the possible people to 200 
and if wrong, 600. So we get good information when the answer is yes (25%) and not so good if the answer is 
no (75%). The question is ok, but not great.
Question 3: Assume females make up about 50% of the 800. Whether the answer is yes or no - we've reduced the possible secret
to 400. We don't really care which the answer is - either gives us a lot of information.

How can we quantitatively measure the information gleaned?

The measure needs to consider both the probability of yes and no answer AND how each answer has reduced the 
number of possible answers i.e. the information gleaned from that answer.

The information is given by 
```
I = -1 * log of the ratio of people left.
```
The log can be to any base, but it's customary to use base 2 following Shannon's original paper on entropy.

Q1 answer 'yes'
```
I(yes) = -1 * log (1/800) = 9.65
```
We haven't interpreted what the information score means yet. It means that the number of possibilities
has been reduced by 1 over 2^9.65 ( = 1/800 as expected!). So we can use the Information measure in this way.
It will become clearer with more examples.

That's a very high information score, but it nust be balanced with the fact that the probability of 'yes'
is tiny. How about the more likely answer 'no'.
Q1 answer 'no'
```
I(yes) = -1 * log (799/800) = .002
```
We therefor get 9.65 bits of information 1/800th = .0013% of the time and only .002 bits 99.88% of the time
So what is the expected information value when balanced with the probability of getting each answer?
```
Expected Value of Information = p(yes) * I(yes) + p(no) * I(no) 
                              = 0.13% * 9.65 + 99.88% * 0.002
                              = 0.014
```
to be continued...












