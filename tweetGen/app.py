from flask import Flask
from corpus_genv2 import Markov_gen
import random
app = Flask(__name__)

@app.route('/')
def hello_world():
    word_list = []
    text = open("clean_text.txt").readlines()
    for lines in text:
        word_list.append(lines.split())
    word_list = word_list[0]
    markov_model = Markov_gen(word_list)
    sentence = markov_model.random_walk(random.randint(5,10))
    return sentence

if __name__ == "__main__":
    hello_world()
