#Hamming distance:The minimun number of symbol substitutions required to change one string into another of equal length.
s=list(input('Enter first sequence:'))
t=list(input('Enter second sequence:'))
mut=0
for i in range(len(s)):
    if s[i] != t[i]:
        mut=mut+1
print(mut)
