import csv
import operator

from util import word_list, distinct_letters, LETTERS_IN_WORD
from green_guess import average_green_score, green_letter_frequency

# yellow_and_green_scores = {key: average_yellow_score[key]+average_green_score[key] for key in average_yellow_score}

yellow_and_green_scores = {}
overall_score = {}

for word in word_list:
    score = 0
    for i in range(len(word)):
        letter = word[i]
        letter_s_green_guesses = green_letter_frequency[letter][i]
        letter_s_yellow_guesses = sum([green_letter_frequency[letter][j] for j in range(len(word)) if j != i])
        score += (letter_s_green_guesses + 0.25 * letter_s_yellow_guesses)
    distinct_lets, _ = distinct_letters([word])
    yellow_and_green_scores[word] = score
    overall_score[word] = (score / LETTERS_IN_WORD) * distinct_lets

best_overall_score = sorted(overall_score.items(), key=operator.itemgetter(1), reverse=True)

# first_choice_file = open("res/wordle_pool_one_choice.csv", "w")
# writer = csv.writer(first_choice_file)
# writer.writerow(['word', 'score'])
#
# for i in range(50):
#     writer.writerow([best_overall_score[i][0], best_overall_score[i][1]])
#
# first_choice_file.close()
