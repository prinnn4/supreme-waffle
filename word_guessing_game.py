# Word Guessing Game Program by Daniel Lee
# Import modules for later use in program
import random

# Randomly choose word from wordbank
def randomanimal():
    # the potential bug i noticed was taht the randomanimal function doesn't handle newline characters that are present in each line of the wordbank file.
    with open('wordbank.txt','r') as file:
        words = file.readlines()
        return random.choice(words).strip()
    # get rid of white space from the chosen word

# Test random word
print(randomanimal())

# why did you print randomanimal? 

# try adding a function that provides a notice of how many words/terms are left in order for them to get the hint at a certain time before running out of tries.
# Give player hint when requested
