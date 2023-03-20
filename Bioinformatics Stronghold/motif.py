s=input('Enter the sequence:')
t=input('Enter the motif:')
l=len(t)
num=''
for i in range(len(s)):
    motif= s[i:i+l]
    if motif == t:
        num=num +str(i+1)+ ' '
print(str(num))