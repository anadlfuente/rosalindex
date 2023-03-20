s=input('Enter the sequence:')
dnacount= {'A': 0, 'C':0,'G':0,'T':0}
nucleotide=list(s)
for nt in nucleotide:
    if nt == 'A':
        dnacount['A']=dnacount['A']+1
    elif nt == 'C':
        dnacount['C']=dnacount['C']+1
    elif nt == 'G':
        dnacount['G']=dnacount['G']+1
    elif nt == 'T':
        dnacount['T']=dnacount['T']+1
print(dnacount['A'],dnacount['C'],dnacount['G'],dnacount['T'])