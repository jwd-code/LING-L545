import nltk
nltk.download('punkt')
from nltk import sent_tokenize
import sys

line = sys.stdin.readline()

while line != '':
    token_list = sent_tokenize(line)
    for sent in token_list:
        sys.stdout.write(sent + '\n')
    line = sys.stdin.readline()
    