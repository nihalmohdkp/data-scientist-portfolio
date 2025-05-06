def create_stack():
    stack =[]
    return stack
def push(stack,items):
    stack.append(items)
def pop(stack):
    if stack==[]:
        return 'this is empty'
    else:
        return stack.pop()
def display(stack):
    print(stack)
def peek(stack):
    if stack==[]:
        return 'stack is empty'
    else:
        return stack[-1]
def is_empty(stack):
    if stack==[]:
        return 'stack is empty'
    else:
        return 'stack is not empty'

create_stack
while True:
    wh=int(input('enter the limits'))
    print('1.push\n2.pop2\n3.display\n4.peek\n5.is_empty')
    if wh==1:
        n=int(input('enter the limits'))
        for i in range(n):
            pus=input()
        print(pus)
        print(push)
    elif wh==2:
        print(pop())
    elif wh==3:
        display()
    elif wh==4:
        print (peek(stack))
    elif wh==5:
        print