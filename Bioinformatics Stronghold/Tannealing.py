s=input('Enter the oligo sequence:')
dic= {'AT':0,'GC':0 }
s=list(s)
for i in s:
    if i in ['A', 'T']:
        dic['AT']=dic['AT']+1
    else:
        dic['GC']=dic['GC']+1
Tan=dic['GC']*4+dic['AT']*2
print('The temperatur of annealing is:',Tan,'ºC')
