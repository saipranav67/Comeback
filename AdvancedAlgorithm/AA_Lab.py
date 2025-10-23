class Node:
    def __init__(self,d):
        self.data=d
        self.next=None
        
class Stack:
    
    def __init__(self):
        self.head=None
        
    def push(self,d):
        Newnode=Node(d)
        if (self.head==None):
            self.head=Newnode
        else:
            Newnode.next=self.head
            self.head=Newnode
    
    def pop(self):
        if(self.head==None):
            print("Underflow")
            return
        self.head=self.head.next
        
    def top(self):
        if(self.head==None):
            print("Underflow")
            return
        print(self.head.data)
          
    def display(self):
        if(self.head==None):
            print("Underflow")
            return
        temp=self.head
        while(temp!=None):
            print(temp.data)
            temp=temp.next
            
s1=Stack()
while (True):
    print("""
          Enter Choice-
          1.Push
          2.Pop
          3.Top
          4.Print
          5.Exit\n
          """)
    d=int(input())

    if(d==1):
        print("Enter Data: ")
        data=int(input())
        s1.push(data)
    elif(d==2):
        s1.pop()
    elif(d==3):
        s1.top()
    elif(d==4):
        s1.display()
    elif(d==5):
        break
    else:
        print("Enter correct choice")