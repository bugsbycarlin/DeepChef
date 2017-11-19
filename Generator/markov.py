
import random
import re

class Markov(object):

  def __init__(self, gram=1):
    self.dictionary = {}
    self.first_words = {}
    self.second_words = {}
    self.gram=gram

  def train(self, item):
    if self.gram == 1:
      self.train_1(item)
    else:
      self.train_n(item)

  def train_1(self, item):
    words = [re.sub('[^0-9a-zA-Z]+', ' ', word).strip() for word in item.split()]

    for i, word in enumerate(words):
      if not word in self.dictionary:
        self.dictionary[word] = {}
      if i == 0:
        if not word in self.first_words:
          self.first_words[word] = 1
        else:
          self.first_words[word] += 1
      if i == 1:
        if not word in self.second_words:
          self.second_words[word] = 1
      next_word = "STOP_WORD"
      if i < len(words) - 1:
        next_word = words[i + 1]
      if not next_word in self.dictionary[word]:
        self.dictionary[word][next_word] = 1
      else:
        self.dictionary[word][next_word] += 1

  def train_n(self, item):
    words = [re.sub('[^0-9a-zA-Z]+', ' ', word).strip() for word in item.split()]
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
    new_first_words = {}
    for item in self.first_words:
      if self.first_words[item] >= 3:
        new_first_words[item] = self.first_words[item]
    self.first_words = new_first_words

  def generate(self, min_length=0, use_start=False, cap_space=False):
    if self.gram == 1:
      return self.generate_1(min_length, use_start, cap_space)
    else:
      return self.generate_n(min_length, use_start, cap_space)

  def generate_1(self, min_length=0, use_start=False, cap_space=False):
    phrase = []
    word = random.choice(self.dictionary.keys())
    if use_start:
      word = weightedChoice(self.first_words)
    while word in self.dictionary and word != "STOP_WORD":
      phrase.append(word)
      word = weightedChoice(self.dictionary[word])
      if len(phrase) < min_length and (word not in self.dictionary or word == "STOP_WORD"):
        word = random.choice(self.dictionary.keys())
      if cap_space and word and word[0].isupper():
        phrase[-1] += "."
    return " ".join(phrase)

  def generate_n(self, min_length=0, use_start=False, cap_space=False):
    ngram_list = []
    word = random.choice(self.dictionary.keys())
    if use_start:
      word = weightedChoice(self.first_words)

    while word in self.dictionary and word.split()[-1] != "STOP_WORD":
      ngram_list.append(word)
      word = weightedChoice(self.dictionary[word])
      if len(ngram_list) < min_length and (word not in self.dictionary or word.split()[-1] == "STOP_WORD"):
        word = random.choice(self.dictionary.keys())
      if cap_space and word and work[0].isupper():
        ngram_list[-1] += "."
    phrase = [ngram.split()[0] for ngram in ngram_list] + [ngram_list[-1].split()[1]]
    return " ".join(phrase) 

def weightedChoice(dictionary):
    random_value = random.uniform(0, sum(dictionary.itervalues()))
    total = 0.0
    for key, weight in dictionary.iteritems():
        total += weight
        if random_value < total: return key
    return key