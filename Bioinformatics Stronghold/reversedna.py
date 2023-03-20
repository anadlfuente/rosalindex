s=input('Enter the sequence:')
s=s[::-1]#permite invertir el string añadido.
nt=list(s)
sol=''
for i in nt:
    if i == 'A':
        sol=sol+'T'
    elif i == 'T':
        sol=sol+'A'
    elif i == 'G':
        sol=sol+'C'
    elif i == 'C':
        sol=sol+ 'G'
print(sol)
#También puede utilizarse .maketrans y hacer un mapa para reeplazar cada una con la correspondiente.