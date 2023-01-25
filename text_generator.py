# This is my text_generator project

from nltk.probability import FreqDist
from nltk.tokenize import WhitespaceTokenizer

# All tokens
user_file = input()
f = open(user_file, 'r', encoding='utf8')
my_file = f.read()
my_tokenizer = WhitespaceTokenizer()
token_split = my_tokenizer.tokenize(my_file)
f.close()

counter = 0
for tokens in token_split:
    counter += 1
print('Corpus statistics')
print('All tokens : ', counter)

# Unique tokens
print('Unique token : ', len(set(token_split)))

# Print index
while True:
    user_input = input()
    if user_input == "exit":
        break
    try:
        integer = int(user_input)
        print(token_split[integer])
    except ValueError:
        print("Type Error. Please input an integer.")
    except IndexError:
        print("Index Error. Please input an integer that is in the range of the corpus.")
