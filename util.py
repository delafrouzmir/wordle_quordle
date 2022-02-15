from csv import DictReader

LETTERS_IN_WORD = 5


word_dict = origin_destination_city_tuples = list(DictReader(open('wordle_words.csv')))
word_list = [word['word'] for word in word_dict]
word_len = len(word_list)


def distinct_letters(t):
    letters = set()
    for word in t:
        for letter in word:
            letters.add(letter)
    list_of_letters = tuple()
    for i in range(LETTERS_IN_WORD):
        list_of_letters = list_of_letters + tuple(sorted([word[i] for word in t]))
    return len(letters), list_of_letters
