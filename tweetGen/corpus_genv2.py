import random
from random import choice

class Markov_gen(dict):
    def __init__(self,word_list=None):
        super(Markov_gen,self).__init__()
        self.words = word_list
        if word_list is not None:
            word_list_length = len(word_list)-2
            for index in range(0, word_list_length):
                tuple_pair= (word_list[index],word_list[index+1])
                next_word = word_list[index+2]
                self._gen_model(tuple_pair,next_word)

    def _gen_model(self,word_tupl,next_word):
        if word_tupl in self:

            if next_word in self[word_tupl]:
                self[word_tupl][next_word] += 1
            else:
                self[word_tupl][next_word] = 1
        else:
            self[word_tupl] = {next_word:1}

    def frequency(self,histogram):
        accumulator = 0
        total_tokens = len(histogram)
        random_integer = random.randint(1,total_tokens)

        for key,value in histogram.items():
            accumulator += value
            if accumulator >= random_integer:
                 return key

    def random_walk(self, length):
        sentence = []
        markov = Markov_gen(self.words)

        if len(markov) == 0:
            print("Error Found: Empty histogram")

        weighted_word = choice(list(markov.keys()))

        while len(sentence) != length:
            sentence .append(weighted_word[1])
            weighted_word = (weighted_word[1], self.frequency(markov[weighted_word]))

        return " ".join(sentence) + "."