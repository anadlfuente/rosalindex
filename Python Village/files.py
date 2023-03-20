f=open('input.txt','r')
sum=0
for line in f:
    line =line.strip()
    if sum % 2 != 0:
        print(line)
    sum=sum+1
