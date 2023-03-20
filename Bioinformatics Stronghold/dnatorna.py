dna=input('Enter the DNA sequence:')
nucleotide=list(dna)
rna= ''
for i in nucleotide:
    if i == 'T':
        rna=rna +'U'
    elif i == 'A' or 'G' or 'C':
        rna=rna + i
print(rna)