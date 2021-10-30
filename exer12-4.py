

filename = "words.txt"
max_word_size = 30

def get_words():
    words = []
    with open(filename) as f:
        words = f.read().splitlines()
    return words

def sort_by_length(words):
    # array of list of string
    # assume that no word is longer than 30
    out = [[] for i in range(max_word_size)]
    for word in words:
        length = len(word)
        out[length].append(word)
    return out

def gen_child_words(word):
    children = []
    for i in range(len(word)):
        children.append(word[0:i] + word[i+1:])
    return children

def exe():
    words = get_words()
    words.append("i")
    words.append("a")
    sorted = sort_by_length(words)
    # sorted is a list of list of words, where the index of the sublist
    # is the length of words it contains
    good_words = []
    for i in range(max_word_size):
        good_words.append(set())

    print("Checking word length 1... Found 2.")
    for word in sorted[1]:
        good_words[1].add(word)

    # for each word length, check if any words of that length are good words
    for word_len in range(2, max_word_size):
        print("Checking word length {}...".format(word_len), end='')
        count = 0
        # for each word of a given length, check if any of its children are good_words (of n-1)
        for word in sorted[word_len]:
            children = gen_child_words(word)
            for child in children:
                if child in good_words[word_len-1]:
                    good_words[word_len].add(word)
                    count = count + 1
                    break

        print(" Found {}.".format(count))
        if count == 0:
            break

    length_of_longest = word_len - 1
    print("Length of longest word is {} and there are {} word(s) of that length.".format(length_of_longest, len(good_words[length_of_longest])))
    print("Answer: ", good_words[length_of_longest])


exe()
