import os
import string
import random
import operator
os.chdir('Downloads/PFE/corpus')
tot_cat = []
corpus = ['test.txt', 'train.txt','valid.txt']
for text in corpus :
    with open(text, encoding = 'utf-8') as f:
        lines = f.read().splitlines()
    incr = 0
    rimes = []
    while incr < len(lines):
        if (len(lines[incr]) > 5) & (len(lines[incr +1]) > 5):
            s1, s2 = lines[incr], lines[incr + 1]
            while(s1[-1] in ['"', '.', ',', ';', ':', '?', '!', ' ', ')', '»', '-', '\xa0']):
                s1 = s1[:-1]
            while(s2[-1] in ['"', '.', ',', ';', ':', '?', '!', ' ', ')', '»', '-', '\xa0']):
                s2 = s2[:-1]
            s1, s2 = s1.split(), s2.split()
            rimes.append([s1[-1], s2[-1], str(incr)])
            rimes.append([s2[-1], s1[-1], str(incr)])
        incr += 2


    '''categories = []
    for rime in rimes:
        if len(categories) == 0:
            categories.append(rime)
        else :
            isInCateg = False
            for categorie in categories :
                if (rime[0] in categorie) | (rime[1] in categorie):
                    isInCateg = True
                    if not(rime in categorie):
                        categorie.append(rime[0])
                    if not(rime[1] in categorie):
                        categorie.append(rime[1])
                    break
            if not(isInCateg):
                categories.append(rime)'''
    tot_cat += rimes


os.chdir('../')
os.chdir('../')
with open('ClustersMotsRimesCorneilleRacine2021.txt') as f:
  mat = []
  for line in f:
    mat.append(line.split())
maxlen = 0
for line in mat:
    if len(line) > maxlen:
        maxlen = len(line)
mat = mat[1:]

rimeme = mat[0][-1]

i = 0
mat2 = []
while i < len(mat) - 1:
    group = []
    while (mat[i][-1] == rimeme):
        group.append(mat[i][0])
        i +=1
        if i == len(mat) : break
    mat2.append([group,rimeme])
    if i < len(mat):
        rimeme = mat[i][-1]

for k in range(len(mat2)-1,-1,-1):
    rimeme = mat2[k][-1]
    for j in range(k):
        if mat2[j][-1] == rimeme:
            mat2[j][0] += mat2[k][0]
            mat2.pop(k)
            break


'''for k in range(len(tot_cat)-1, -1, -1):
    isInGroup = False
    for word in tot_cat[k]:
        for group in mat2:
            if word in group[0]:
                isInGroup = True
                group[0] += tot_cat[k]
                break
        if isInGroup : break
    if isInGroup : tot_cat.pop(k)

for k in range(len(mat2)):
    unique_words = []
    for j in range(len(mat2[k][0])):
        if not(mat2[k][0][j] in unique_words):
            unique_words.append(mat2[k][0][j])
    mat2[k][0] = unique_words'''

d = {}
for group in mat2:
    d[group[-1]] = 0

for k in range(len(tot_cat)-1, -1, -1):
    isInGroup = False
    for group in mat2:
        if tot_cat[k][0] in group[0]:
            d[group[-1]] += 1
            isInGroup = True
            break
    if isInGroup : tot_cat.pop(k)

change = True
while change:
    change = False
    for j in range(len(tot_cat)-1, -1, -1):
        for k in range(len(mat2)):
            if tot_cat[j][1] in mat2[k][0]:
                change = True
                mat2[k][0].append(tot_cat[j][0])
                d[mat2[k][-1]] +=1
                tot_cat.pop(j)
                break

d = dict(sorted(d.items(), key=operator.itemgetter(1),reverse=True))
cumul = 0
cumul_l = []
new_mat = []

for k, v in d.items():
    cumul += v
    cumul_l.append([cumul])
    for group in mat2:
        if group[-1] == k:
            new_mat.append(group)
            break
tot = cumul_l[-1][0]

for cum in cumul_l:
    cum.append(cum[0]/tot)

for k in range(len(new_mat)):
    unique_words = []
    for j in range(len(new_mat[k][0])):
        if not(new_mat[k][0][j] in unique_words):
            unique_words.append(new_mat[k][0][j])
    new_mat[k][0] = unique_words

with open('residual_categories.txt', 'w', encoding='utf-8') as f:
    for line in tot_cat:
        f.write(' '.join(line) + '\n')
'''with open('paires_rimes.txt', 'a', encoding='utf-8') as f:
    for line in paires_rimes:
        f.write(line + '\n')'''
with open('mots_rimes.txt', 'w', encoding='utf-8') as f:
    for group in new_mat[:150]:
        f.write(group[1] + '\n')
        f.write(' '.join(group[0]) + '\n')
with open('compteur.txt', 'w', encoding='utf-8') as f:
    incr = 0
    for key, value in d.items():
        f.write(key+' '+str(value)+ ' '+str(cumul_l[incr][0])+' '+str(cumul_l[incr][1]) +'\n')
        incr +=1
