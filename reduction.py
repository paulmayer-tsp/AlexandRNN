import os
os.chdir('Downloads/PFE')
with open('new_categories.txt', encoding='utf-8') as f:
  mylist = []
  for line in f:
    mylist.append(line.split())
for i in range(len(mylist)-1, -1, -1):
  isNotinCat = True
  for word in mylist[i]:
    if isNotinCat:
      for j in range(i):
        if isNotinCat:
          if word in mylist[j]:
            mylist[j] = mylist[j] + [word for word in mylist[i]]
            mylist.pop(i)
            isNotinCat = False

with open('final_categories.txt', 'a', encoding='utf-8') as f:
    for line in mylist:
        f.write(' '.join(line) + '\n')