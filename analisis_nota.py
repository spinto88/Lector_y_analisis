from nltk.corpus import PlaintextCorpusReader as PCR
from nltk.corpus import stopwords
from nltk.corpus import swadesh
from nltk.probability import FreqDist
from nltk.text import Text
import os

corp = PCR(os.getcwd(), '.*.txt')

nota0_words = corp.words(fileids = 'Nota27.txt')

#texto = Text(nota0_words)


def propernouns(list_words):
    pn = []
    first = list_words[0]
    if first.lower() not in stopwords.words('spanish') and first not in swadesh.words('es'):
        pn.append(list_words[0])

    for i in range(1, len(list_words)):
        if list_words[i][0].isupper() == True and len(list_words[i]) > 2:
           pn.append(list_words[i])

    return pn

print propernouns(nota0_words)


words = [i.lower() for i in nota0_words]

words_new = []

for i in words:
    if i in stopwords.words('spanish') or i in swadesh.words('es') or len(i) < 3:
        pass
    else:
        words_new.append(i)
       
freq = FreqDist(words_new)

for i in freq.keys():
    print i, freq[i]

