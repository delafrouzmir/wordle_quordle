import operator

from util import word_list, LETTERS_IN_WORD, distinct_letters

green_letter_frequency = {}

for word in word_list:
    for i in range(len(word)):
        letter = word[i]
        if letter not in green_letter_frequency:
            green_letter_frequency[letter] = [0 for _ in range(LETTERS_IN_WORD)]
        green_letter_frequency[letter][i] += 1


average_green_score = {}
for word in word_list:
    score = 0
    for i in range(len(word)):
        letter = word[i]
        letter_s_green_guesses = green_letter_frequency[letter][i]
        score += letter_s_green_guesses
    distinct_lets, _ = distinct_letters([word])
    average_green_score[word] = (score / LETTERS_IN_WORD) * distinct_lets

best_green_score = sorted(average_green_score.items(), key=operator.itemgetter(1), reverse=True)
