f=open('input.txt','r')
g=open('output.txt','w')
for line in f.readlines()[1::2]:
    g.write(line)
g.close()