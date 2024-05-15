# Word Guessing Game Program by Daniel Lee
# Import modules for later use in program
import random

# Randomly choose word from wordbank
def randomanimal():
    # the potential bug i noticed was taht the randomanimal function doesn't handle newline characters that are present in each line of the wordbank file.
    with open('wordbank.txt','r') as file:
        words = file.readlines()
        return random.choice(words)

# Test random word
print(randomanimal())

# why did you print randomanimal? 


# Give player hint when requested
