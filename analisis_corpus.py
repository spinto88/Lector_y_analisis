from nltk.corpus import PlaintextCorpusReader as PCR
from nltk.corpus import stopwords
from nltk.corpus import swadesh
from nltk.probability import FreqDist
import os
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

corp = PCR(os.getcwd(), '.*.txt')

words = [i.lower() for i in corp.words()]

freq = FreqDist(words)

data = freq.values()

hist = plt.hist(data, range = [0, 200], bins = 200, normed = True)

hist = hist[0]

plt.clf()
plt.plot(range(200), hist, '.', markersize = 15)
plt.grid('on')
plt.yscale('log')
plt.xscale('log')
plt.xlabel('Word frecuency', size = 15)
plt.ylabel('# Words', size = 15)
plt.show()


