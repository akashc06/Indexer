import os

path = "D:\\ff"
dirs = os.listdir(path)
uni_index = {}
U = {}
bi_index = {}
B = {}
tri_index = {}
T = {}
Documents = {}
count = 0

def get(dict):
    s = ""
    for i in dict:
        s = s + " " + i
    return s

for file in dirs:
    f = open(path + '\\' + file, "r")
    x = f.read()
    d = x.split()
    count = count + 1
    Documents[file] = "Doc-" + str(count)
    doc_ID = "Doc-" + str(count)
    for w in d:
        if w in uni_index:
                if doc_ID in uni_index[w]:
                    uni_index[w][doc_ID] += 1
                else:
                    uni_index[w][doc_ID] = 1
        else:
                uni_index[w] = {doc_ID: 1}
    for i, k in zip(d, d[1:]):
         m = i + " " + k
         if m in bi_index:
             if doc_ID in bi_index[m]:
                 bi_index[m][doc_ID] += 1
             else:
                 bi_index[m][doc_ID] = 1
         else:
             bi_index[m] = {doc_ID: 1}
    for i,k,j in zip(d, d[1:],d[2:]):
         m = i + " " + k + " " + j
         if m in tri_index:
             if doc_ID in tri_index[m]:
                 tri_index[m][doc_ID] += 1
             else:
                 tri_index[m][doc_ID] = 1
         else:
             tri_index[m] = {doc_ID: 1}

for i in uni_index:
     U[i] = sum(uni_index[i].values())

for i in bi_index:
     B[i] = sum(bi_index[i].values())

for i in tri_index:
     T[i] = sum(tri_index[i].values())


ft1 = open("uni-tf.txt","w+")
j = sorted(U.items(), key=lambda x: (-x[1], x[0]))
for y in j:
     ft1.write(str(y) + "\n")

ft2 = open("bi-tf.txt","w+")
j = sorted(B.items(), key=lambda x: (-x[1], x[0]))
for y in j:
     ft2.write(str(y) + "\n")

ft3 = open("tri-tf.txt","w+")
j = sorted(T.items(), key=lambda x: (-x[1], x[0]))
for y in j:
      ft3.write(str(y) + "\n")

ft1.close()
ft2.close()
ft3.close()


f1 = open("uni-df.txt", "w+")
for i in uni_index:
         d = get(uni_index[i])
         f1.write(i + " " + d + " " + str(len(uni_index[i].values())) + "\n")

f2 = open("bi-df.txt", "w+")
for i in bi_index:
        d = get(bi_index[i])
        f2.write(i + " " + d + " " + str(len(bi_index[i].values())) + "\n")

f3 = open("tri-df.txt", "w+")
for i in tri_index:
       d = get(tri_index[i])
       f3.write(i + " " + d + " " + str(len(tri_index[i].values())) + "\n")

f1.close()
f2.close()
f3.close()