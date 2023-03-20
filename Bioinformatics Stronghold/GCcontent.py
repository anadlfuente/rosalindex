fast= open('fasta.txt','r')
d={}
content={}
for line in fast:
    line=line.strip()
    if '>' in line:
        id=str(line[10:14])
    else:
        try:
            d[id]=d[id]+line
        except:
            d[id]=line
for id in d:
    seq=list(d[id])
    num=0;gc=0
    for i in seq:
        num=num+1
        if i in ['G','C']:
            gc=gc+1
    content[id]=(gc/num)*100
max=0
rosalind=0
for id in content:
    if content[id] > max:
        max=content[id]
        rosalind=id.strip()
print('Rosalind_',rosalind,'\n',max,sep='')
