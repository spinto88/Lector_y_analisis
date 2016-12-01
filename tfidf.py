#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score as silh
from sklearn.decomposition import PCA

import matplotlib.pyplot as plt
import codecs

count_vect = CountVectorizer()
tfidf_transformer = TfidfTransformer()

texts = []

for i in range(10):
    try:
        fp = codecs.open('Nota' + str(i) + '.txt', 'r', 'utf8')
        texts.append(fp.read())
        fp.close()
    except:
        pass

texts = [text.lower() for text in texts]

X_counts = count_vect.fit_transform(texts)
X_tfidf = tfidf_transformer.fit_transform(X_counts)

krange = range(2, len(texts))
silh_list = []

for k in krange:
    km = KMeans(n_clusters = k)
    labels = km.fit_predict(X_tfidf)
    silh_list.append(silh(X_tfidf, labels))

plt.plot(krange, silh_list, '.-', markersize = 20)
plt.grid('on')
plt.show()
