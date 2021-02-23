import os
os.chdir('Downloads/PFE/corpus')
corpus = ['test.txt', 'train.txt', 'valid.txt']
valid, train, test = [], [], []
for text in corpus :
    with open(text, encoding = 'utf-8') as f:
        mylist = f.read().splitlines()

    incr = 0
    while (incr < len(mylist)):
        for _ in range(6):
            if incr >= len(mylist) -1 : break
            i = 0
            while (mylist[incr-1][-1] != '.') | (i<4) | (i % 2 == 1):
                train.append(mylist[incr])
                i+=1
                incr +=1
                if incr >= len(mylist) -1 : break
        if incr < len(mylist) - 1:
            i = 0
            while (mylist[incr-1][-1] != '.') | (i<4) | (i % 2 == 1):
                test.append(mylist[incr])
                i+=1
                incr +=1
                if incr >= len(mylist) -1 : break
            i = 0
            while (mylist[incr-1][-1] != '.') | (i<4) | (i % 2 == 1):
                valid.append(mylist[incr])
                i+=1
                incr +=1
                if incr >= len(mylist) -1 : break
        else : incr += 5

with open('../corpus_new/valid.txt', 'w', encoding = 'utf-8') as f:
    for str in valid:
        f.write(str+'\n')
with open('../corpus_new/test.txt', 'w', encoding = 'utf-8') as f:
    for str in test:
        f.write(str+'\n')
with open('../corpus_new/train.txt', 'w', encoding = 'utf-8') as f:
    for str in train:
        f.write(str+'\n')