limit=int(input('enter your limit:'))
count=0
n1=0
n2=1
print ('fibinocci series =', end=' ')
while count<limit:
    print(n1,end=' ')
    x=n1+n2
    n1=n2
    n2=x
    count+=1
