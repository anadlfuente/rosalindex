a=int(input('Enter a:'))
b=int(input('Enter b:'))
r=range(a,b+1)
sum=0
for i in r:
    if i % 2 != 0:
         sum= sum+i
print(sum)