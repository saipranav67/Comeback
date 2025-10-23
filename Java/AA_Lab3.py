class Node:
    def __init__(self,d):
        self.data=d
        self.next=None
        
class Queue:
    
    def __init__(self):
        self.head=None
        
    def enqueue(self,d):
        Newnode=Node(d)
        if (self.head==None):
            self.head=Newnode
        else:
            temp=self.head
            while(temp.next!=None):
                temp=temp.next
            temp.next=Newnode
    
    def dequeue(self):
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
            
q1=Queue()
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
        q1.enqueue(data)
    elif(d==2):
        q1.dequeue()
    elif(d==3):
        q1.top()
    elif(d==4):
        q1.display()
    elif(d==5):
        break
    else:
        print("Enter correct choice")