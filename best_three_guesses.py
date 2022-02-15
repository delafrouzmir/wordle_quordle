import csv
import operator
from copy import deepcopy
from best_two_guesses import two_words_and_scores
from util import word_len, word_list, distinct_letters, LETTERS_IN_WORD
from yellow_and_green_guess import yellow_and_green_scores


class ThreeWordGuessInfo:
    def __init__(self, words, first_word_score, second_word_score, third_word_score, score, distinct_let_num):
        self.words = words
        self.first_word_score = first_word_score
        self.second_word_score = second_word_score
        self.third_word_score = third_word_score
        self.score = score
        self.distinct_let_num = distinct_let_num

    def to_dict(self):
        return deepcopy(self.__dict__)


three_words_and_scores = []
distinct_letters_set = set()

top_two_words_and_scores = two_words_and_scores[:5000]

for i in range(len(top_two_words_and_scores)):
    for j in range(word_len):
        if word_list[j] not in top_two_words_and_scores[i].words:
            key = [*top_two_words_and_scores[i].words, word_list[j]]
            distinct_let_num, distinct_lets = distinct_letters(key)
            if distinct_lets not in distinct_letters_set:
                distinct_letters_set.add(distinct_lets)
                score = (top_two_words_and_scores[i].first_word_score + top_two_words_and_scores[i].second_word_score +
                         yellow_and_green_scores[word_list[j]]) / (3 * LETTERS_IN_WORD) * distinct_let_num
                three_words_and_scores.append(
                    ThreeWordGuessInfo(words=key,
                                       first_word_score=top_two_words_and_scores[i].first_word_score,
                                       second_word_score=top_two_words_and_scores[i].second_word_score,
                                       third_word_score=yellow_and_green_scores[word_list[j]],
                                       score=score,
                                       distinct_let_num=distinct_let_num))

three_words_and_scores = sorted(three_words_and_scores, key=operator.attrgetter('score'), reverse=True)

# first_choice_file = open("res/wordle_pool_three_choices.csv", "w")
# writer = csv.writer(first_choice_file)
# writer.writerow(['word1', 'word2', 'word3', 'first_word_score', 'second_word_score', 'first_word_score', 'score'])
#
# for i in range(50):
#     writer.writerow([*three_words_and_scores[i].words,
#                      three_words_and_scores[i].first_word_score,
#                      three_words_and_scores[i].second_word_score,
#                      three_words_and_scores[i].third_word_score,
#                      three_words_and_scores[i].score])
#
# first_choice_file.close()
