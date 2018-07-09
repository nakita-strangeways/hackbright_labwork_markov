from sys import argv

argv[3] = int(argv[3])

print(argv)
"""Generate Markov text from text files."""

import random
#import choice


def open_and_read_file(file_path1,file_path2):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    f1 = open(file_path1,"r")
    file_contents = f1.read()
    f1.close()

    f2 = open(file_path2,"r")
    file_contents += f2.read()
    f2.close()


    return file_contents

def make_chains(text_string,n_gram):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}
    words = text_string.split()

#    for item in ls:
    for i in range(len(words) - n_gram):

        gram = words[i:i+n_gram]

        gram_t = tuple(gram)
        chains[gram_t] = chains.get(gram_t,[]) + [words[i+n_gram]]
        #print(bigram,words[i+2])

        # for i in chains.items():
        #     print (i)
    return chains

# print(make_chains(open_and_read_file("green-eggs.txt")))

def make_text(chains, n_gram):
    """Return text from chains."""

    words = []
    char_length = 0

    random_key = random.choice(list(chains.keys()))
    words.extend(random_key)

    # random_value = random.choice(chains[random_key])

    # words.append(random_value)
    n = 241

    for word in words:

        char_length += len(word) +1


    while char_length < n:

        new_gram = tuple(words[n_gram *-1:])

        if new_gram not in chains.keys():
            break

        else:
            next_word = random.choice(chains[new_gram])
            words.append(next_word)
            char_length += len(next_word) +1
            #n -= 1

    words[0] = words[0][0].upper() + words[0][1:]
    words_str = " ".join(words)
    punct_list = [".","!","?"]
    for i in range( (len(words_str) -1), 0, -1):
        if words_str[i] in punct_list:
            break

        else:
            words_str = words_str[:-1]

    return words_str

# print(make_text(make_chains(open_and_read_file("green-eggs.txt"))))

#input_path = "green-eggs.txt"
#input_path = "gettysburg.txt"
input_path1 = argv[1]
input_path2 = argv[2]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path1,input_path2)

# Get a Markov chain
chains = make_chains(input_text,argv[3])

# Produce random text
random_text = make_text(chains, argv[3])

#random_text = make_text(chains)

log_file = open("markov_tweets.txt", "a")
#log_file_contents = log_file.read() + "\n" + random_text
random_text = "\n" + random_text
log_file.write(random_text)
log_file.close()
print(random_text)
