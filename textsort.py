def textsort(file):
    with open(file, 'r') as r:
        f1 = open("Sortedfile", "w+")
        for line in sorted(r):
            f1.write(line)
        f1.close()

textsort("tri-df.txt")