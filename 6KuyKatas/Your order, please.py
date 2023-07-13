import re


def order(sentence):
  return ' '.join(sorted(sentence.split(), key=lambda w:sorted(w)))
