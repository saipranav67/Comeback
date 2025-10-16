import java.util.*;
public class AA_Lab2 {
    public static void main(String[] args) {
        int a[]=new int[5];
        int top=-1,d;
        Scanner in = new Scanner(System.in);
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
                top=push(a,top,data);
            }
            if(d==2){
                top=pop(a,top);
            }
            if(d==3){
                peek(a,top);
            }
            if(d==4){
                print(a,top);
            }
            in.close();
        }
    }
    public static int push(int a[],int top,int data){
        if(top<a.length){
            top++;
            a[top]=data;
        }
        else{
            System.out.println("Stack Overflow");

        }
        return top;
    }
    public static int pop(int a[],int top){
        if(top<0){
            System.out.println("Underflow");
        }
        if(top>=0){
        System.out.println(a[top]+" is poped");
        top--;}
        return top;
    }
    public static void peek(int a[],int top){
        if(top<0){
            System.out.println("Underflow");
        }
        System.out.println(a[top]);
    }
    public static void print(int a[],int top){
        if(top<0){
            System.out.println("Underflow");
        }
        for(int i=top;i>=0;i--){
            System.out.println(a[i]);
        }
    
    }    
}
