s=input('Enter the oligo sequence:')
dic= {'AT':0,'GC':0 }
s=list(s)
print(s)
for i in s:
    if i in ['A', 'T']:
        dic['AT']=dic['AT']+1
    else:
        dic['GC']=dic['GC']+1
Tan= d['GC']*4+d['AT]*2
print('The temperature of annealing is:',Tan)
