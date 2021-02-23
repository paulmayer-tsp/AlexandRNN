import os
os.chdir('Downloads')

with open('compteur.txt', encoding = 'utf-8') as f:
    tab = []
    for line in f:
      tab.append(line.split())

def takeSecond(elem):
    return int(elem[1])

tab.sort(key=takeSecond, reverse=True)

cumul = 0
for rime in tab:
  cumul += int(rime[1])
  rime.append(cumul)
for rime in tab:
  rime.append(rime[2]/157781)

with open('mots_rimes.txt', encoding = 'utf-8') as f:
    incr = 0
    mat2 = []
    for line in f:
        if incr %2 == 0:
            mat2.append(line.split())
        else:
            mat2[-1].append(line.split())
        incr +=1

new_mat = []

for rimeme in tab:
    for group in mat2:
        if group[0] == rimeme[0]:
            new_mat.append(group)
            break

for k in range(len(new_mat)):
    unique_words = []
    for j in range(len(new_mat[k][1])):
        if not(new_mat[k][1][j] in unique_words):
            unique_words.append(new_mat[k][1][j])
    new_mat[k][1] = unique_words

with open('mots_rimes_final.txt', 'a', encoding='utf-8') as f:
    for group in new_mat:
        f.write(group[0] + '\n')
        f.write(' '.join(group[1]) + '\n')
print(tab[0])
with open('pourcentages.txt', 'a', encoding='utf-8') as f:
    for rime in tab:
        f.write(rime[0]+' '+ rime[1]+' '+str(rime[2])+' '+str(rime[3]) +'\n')
