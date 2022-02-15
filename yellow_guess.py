import operator

from util import word_list, LETTERS_IN_WORD, distinct_letters

letter_frequency = {}

for word in word_list:
    for letter in word:
        if letter not in letter_frequency:
            letter_frequency[letter] = 0
        letter_frequency[letter] += 1

average_yellow_score = {}
for word in word_list:
    score = sum([letter_frequency[letter] for letter in word])
    distinct_lets, _ = distinct_letters([word])
    average_yellow_score[word] = (score / LETTERS_IN_WORD) * distinct_lets

best_yellow_score = sorted(average_yellow_score.items(), key=operator.itemgetter(1), reverse=True)
