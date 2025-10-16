import java.util.*;
class Node{
    int data;
    Node next;

    Node(int d){
        this.data=d;
        this.next=null;
    }
}

class Stack{

    Node head;

    public void push(int d){
        Node newnode = new Node(d);
        if (head==null){
            head=newnode;
        }
        else{
            newnode.next=head;
            head=newnode;
        }
    }

    public void pop(){
        if(head==null){
            System.out.println("underflow");
            return;
        }
        System.out.println(head.data+" Item Poped");
        head=head.next;
    }

    public void print(){
        if(head==null){
            System.out.println("underflow ");
            return;
        }
        Node temp=head;
        while(temp!=null){
            System.out.println(temp.data);
            temp=temp.next;
        }
    }

    public void peek(){
        if(head==null){
            System.out.println("underflow");
            return;
        }
        System.out.println(head.data+" Peek Item");
    }
}
public class AA_Lab{
    public static void main(String[] args) {
        Stack s1=new Stack();
        Scanner in = new Scanner(System.in);
        int d;
        while(true){
            System.out.println("""
                    1.push
                    2.pop
                    3.peek
                    4.print 
                    5.Exit
                    """);
            d=in.nextInt();
            if(d==5){
                break;
            }
            if(d==1){
                System.out.println("Enter Number: ");
                int data=in.nextInt();
                s1.push(data);
            }
            if(d==2){
                s1.pop();
            }
            if(d==3){
                s1.peek();
            }
            if(d==4){
                s1.print();
            }
        }
    }
}