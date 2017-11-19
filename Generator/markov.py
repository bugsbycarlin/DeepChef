
import random
import re

punctuation = [".", ",", "!", "?"]

class Markov(object):

  def __init__(self, gram=1):
    self.dictionary = {}
    self.first_words = {}
    self.second_words = {}
    self.gram=gram

  def train(self, item):
    for punctuation_mark in punctuation:
      item = item.replace(punctuation_mark, " " + punctuation_mark)
    words = [word for word in re.sub("[^0-9a-zA-Z'.,!?]+", " ", item).split() if word]
    words = [word for word in words if len(word) > 0]
    words.append("STOP_WORD")
    for i, word in enumerate(words):
      if i <= len(words) - self.gram:
        ngram = " ".join(words[i:i+self.gram])
        if i == 0:
          if not ngram in self.first_words:
            self.first_words[ngram] = 1
          else:
            self.first_words[ngram] += 1
        if not ngram in self.dictionary:
          self.dictionary[ngram] = {}
        if i < len(words) - self.gram:
          next_ngram = " ".join(words[i+1:i+self.gram+1])
          if not next_ngram in self.dictionary[ngram]:
            self.dictionary[ngram][next_ngram] = 1
          else:
            self.dictionary[ngram][next_ngram] += 1

  def clean(self):
    if "" in self.dictionary:
      del self.dictionary[""]
    if " " in self.dictionary:
      del self.dictionary[" "]
    if "" in self.first_words:
      del self.first_words[""]
    if " " in self.first_words:
      del self.first_words[" "]
    new_first_words = {}
    for item in self.first_words:
      if self.first_words[item] >= 3:
        new_first_words[item] = self.first_words[item]
    self.first_words = new_first_words

  def generate(self, min_length=0, start_random=False):
    ngram_list = []
    word = weightedChoice(self.first_words)
    if start_random:
      word = random.choice(self.dictionary.keys())
    while word in self.dictionary and word.split()[-1] != "STOP_WORD":
      ngram_list.append(word)
      word = weightedChoice(self.dictionary[word])
      while len(ngram_list) < min_length and (word not in self.dictionary or word.split()[-1] == "STOP_WORD"):
        word = random.choice(self.dictionary.keys())
    if len(ngram_list) == 0:
      return ""
    if self.gram > 1:
      phrase = " ".join([ngram.split()[0] for ngram in ngram_list] + [ngram_list[-1].split()[1]])
    else:
      phrase = " ".join(ngram_list)
    for punctuation_mark in punctuation:
      phrase = phrase.replace(" " + punctuation_mark, punctuation_mark)
    return phrase
    

def weightedChoice(dictionary):
    random_value = random.uniform(0, sum(dictionary.itervalues()))
    total = 0.0
    for key, weight in dictionary.iteritems():
        total += weight
        if random_value < total: return key
    return key