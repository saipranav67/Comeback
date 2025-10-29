class Node:
    def __init__(self,d):
        self.data=d
        self.next=None

class SLL:

    def __init__(self):
        self.head=None
    
    def addNode(self,d):
        Newnode=Node(d)
        if(self.head==None):
            self.head=Newnode
        else:
            temp=self.head
            while(temp.next!=None):
                temp=temp.next
            temp.next=Newnode
        print("Value added")

    def addNodeAfterValue(self,d1,d2):
        if(self.head==None):
            print("Single Linked List is Empty")
        else:
            Newnode=Node(d2)
            temp=self.head
            while(temp.data!=d1 and temp.next!=None):
                temp=temp.next
            if(temp.data==d1):
                Newnode.next=temp.next
                temp.next=Newnode
                print("Value added")

            else:
                print("Value Not Present in Single Linked List")
    
    def addNodeBasedOnPos(self,d1,d2):
        Newnode=Node(d2)
        if(self.head==None):
            if(d1==1):
                Newnode.next=self.head
                self.head=Newnode
                print("Value added")

            else:
                print("Single Linked List is Empty")
        else:
            if(d1==1):
                Newnode.next=self.head
                self.head=Newnode
            else:
                temp=self.head
                for i in range(2,d1):
                    if(temp==None):
                        break
                    temp=temp.next
                if(temp==None):
                    print("Position Not Available in Single Linked List")
                    return
                Newnode.next=temp.next
                temp.next=Newnode
                print("Value added")
    
    def deleteBasedOnValue(self,d):
        if(self.head==None):
            print("Single Linked List is Empty")
        else:
            temp=self.head
            if(temp.data==d):
                self.head=self.head.next
                print("Value Deleted")
            else:
                while(temp.next!=None and temp.next.data!=d):
                    temp=temp.next
                if(temp.next==None):
                    print("Value Not present in Single Linked List")
                else:
                    temp.next=temp.next.next
                    print("Value Deleted")
    
    def deleteBasedOnPos(self,d):
        if(self.head==None):
            print("Single Linked List is Empty")
            return
        if(d==1):
            self.head=self.head.next
            print("Value Deleted")
        else:
            temp=self.head
            for i in range(2,d):
                if(temp==None):
                    break
                temp=temp.next
            if(temp.next==None):
                print("Position not available in Single Linked List")
            else:
                temp.next=temp.next.next
                print("Value Deleted")    

    def display(self):
        if(self.head==None):
            print("SIngle Linked List is Empty")
            return
        temp=self.head
        while(temp!=None):
            print(temp.data)
            temp=temp.next
        
s1=SLL()
while True:
    a=int(input("""
1.Add Node
2.Add Node At Position
3.Add Node After Value
4.Delete Node Based on Position
5.Delete Node Based on Value
6.Print 
7. Exit\n
Enter Choice: """))
    if a==1:
        data=int(input("Enter data: "))
        s1.addNode(data)
    elif a==2:
        pos=int(input("Enter Position: "))
        data=int(input("Enter Data: "))
        s1.addNodeBasedOnPos(pos,data)
    elif a==3:
        val=int(input("Enter Value: "))
        data=int(input("Enter Data: "))
        s1.addNodeAfterValue(val,data)
    elif a==4:
        pos=int(input("Enter Position: "))
        s1.deleteBasedOnPos(pos)
    elif a==5:
        val=int(input("Enter Value: "))
        s1.deleteBasedOnValue(val)
    elif a==6:
        s1.display()
    elif a==7:
        break
    else:
        print("Invalid Choice")


