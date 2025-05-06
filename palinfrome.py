num=int(input('enter a number'))
rev=0
y=num
while num>0:
    x=num%10
    rev=rev*10+x
    num=num//10
print (rev)

if rev==y:
    print(f"{y} is a palindrome")
else:
    print(f'{y} is not palindrome')

