s=input('Enter the string:')
d={}
sep=s.split()
for word in sep:
    if word in d:
        d[word]=d[word]+1
    else:
        d[word]=1
for i in d:
    print(i,d[i])
