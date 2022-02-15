import csv
import operator
from copy import deepcopy

from util import word_len, word_list, distinct_letters, LETTERS_IN_WORD
from yellow_and_green_guess import yellow_and_green_scores

class TwoWordGuessInfo:
    def __init__(self, words, first_word_score, second_word_score, score, distinct_let_num):
        self.words = words
        self.first_word_score = first_word_score
        self.second_word_score = second_word_score
        self.score = score
        self.distinct_let_num = distinct_let_num

    def to_dict(self):
        return deepcopy(self.__dict__)

two_words_and_scores = []
distinct_letters_set = set()

for i in range(0, word_len - 1):
    for j in range(i + 1, word_len):
        key = (word_list[i], word_list[j])
        distinct_let_num, distinct_lets = distinct_letters([word_list[i], word_list[j]])
        if distinct_lets not in distinct_letters_set:
            distinct_letters_set.add(distinct_lets)
            score = (yellow_and_green_scores[word_list[i]] + yellow_and_green_scores[word_list[j]]) \
                    / (2 * LETTERS_IN_WORD) * distinct_let_num
            two_words_and_scores.append(
                TwoWordGuessInfo(words=[word_list[i], word_list[j]],
                                 first_word_score=yellow_and_green_scores[word_list[i]],
                                 second_word_score=yellow_and_green_scores[word_list[j]],
                                 score=score,
                                 distinct_let_num=distinct_let_num))

two_words_and_scores = sorted(two_words_and_scores, key=operator.attrgetter('score'), reverse=True)

# first_choice_file = open("res/wordle_pool_two_choices.csv", "w")
# writer = csv.writer(first_choice_file)
# writer.writerow(['word1', 'word2', 'first_word_score', 'second_word_score', 'score'])
#
# for i in range(50):
#     writer.writerow([*two_words_and_scores[i].words,
#                      two_words_and_scores[i].first_word_score,
#                      two_words_and_scores[i].second_word_score,
#                      two_words_and_scores[i].score])
#
# first_choice_file.close()
