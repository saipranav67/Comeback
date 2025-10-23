def push(l,top,d):
    l.append(d)
    top=top+1
    return top

def pop(l,top):
    if top==-1:
        print("Undeflow")
        return top
    top=top-1
    return top
def printStack(l,top):
    if top==-1:
        print("Underflow")
        return top
    for i in range (top,-1,-1):
        print(l[i])
def peek(l,top):
    if top==-1:
        print("Underflow")
        return top
    print(l[top])

l=[]
top=-1
while True:
    print("""
          1.Push
          2.pop
          3.peek
          4.print
          5.exit.""")
    d=int(input())
    if d==1:
        print("Enter element: ")
        data=int(input())
        top=push(l,top,data)
    if d==2:
        top=pop(l,top)
    if d==3:
        peek(l,top)
    if d==4:
        printStack(l,top)
    if d==5:
        break

