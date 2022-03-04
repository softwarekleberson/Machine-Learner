# -*- coding: utf-8 -*-
"""Treino_Aula1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1y-rlkpLNDMV1ikFTjMrTRVLiKILgfe2D
"""

#features (1 sim, 0 não)

#pelo longo ?
#perna longa ?
#faz auau ?

porco1 = [0, 1, 0]
porco2 = [0, 1, 1]
porco3 = [1, 1, 0]

cachorro1 = [0, 1, 1]
cachorro2 = [1, 0, 1]
cachorro3 = [1, 1, 1]

# 1 => porco, 0 => cachorro

treino_x = [porco1, porco2, porco3, cachorro1, cachorro2, cachorro3]
treino_y = [1, 1, 1, 0, 0, 0]

from sklearn.svm import LinearSVC

model = LinearSVC()
model.fit(treino_x, treino_y)

animal_misterioso = [1, 1, 1]
model.predict([animal_misterioso])

misterio1 = [1, 1, 1]
misterio2 = [1, 1, 0]
misterio3 = [0, 1, 1]

teste_x = [misterio1, misterio2, misterio3]
teste_y = [0, 1, 1]

previsoes = model.predict(teste_x)

corretos = (previsoes == teste_y).sum()
total = len(teste_x)
taxa_Acerto = corretos / total

from sklearn.metrics import accuracy_score

taxa_Acerto = accuracy_score(teste_y, previsoes)
print(f'Taxa de acerto {taxa_Acerto * 100}')