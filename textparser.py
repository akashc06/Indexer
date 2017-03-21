from string import maketrans
import os
import re
import string

path = 'E:\New folder'
dirs = os.listdir(path)
rem = "!\"#$%&\'()*+,./:;<=>?@[\]^_`{|}~"
repl = "                               "
transtab = maketrans(rem, repl)
allowed = string.letters + string.digits + "!#$%&'()*+,-/:;<=>?@[\]^_`{|}~"
acceptable_characters = string.letters + string.digits + "."

def num_there(s):
    return any(i.isdigit() for i in s)

for file in dirs:
    main_list = []
    f = open(path + '\\' + file, "r")
    m = f.read()
    x = re.compile('<.*?>')
    txt = re.sub(x, '', m)
    p = txt.lower()
    d = p.split()
    for each in d:
        if not num_there(each):
            s = each.translate(transtab)
        else:
            s = each
        main_list.append(s)
    f1 = open(filter(lambda c: c in acceptable_characters, file), "w+")
    f1.write(" ".join(main_list))
    f1.close()