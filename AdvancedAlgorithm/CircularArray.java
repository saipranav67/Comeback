import java.util.*;

public class CircularArray {
    public static void main(String[] args) {
        int[] arr = new int[5];
        int front = -1, rear = -1;
        Scanner in = new Scanner(System.in);

        while (true) {
            System.out.println("""
            1. Add
            2. Delete
            3. Print
            4. Exit
            """);

            int c = in.nextInt();

            if (c == 4) break;

            switch (c) {
                case 1: { // Add
                    System.out.print("Enter data: ");
                    int data = in.nextInt();

                    // Check if full
                    if ((rear + 1) % arr.length == front) {
                        System.out.println("Queue is full");
                    } else {
                        if (front == -1) front = 0; // first insertion
                        rear = (rear + 1) % arr.length;
                        arr[rear] = data;
                        System.out.println("Inserted: " + data);
                    }
                }
                break;

                case 2 : { // Delete
                    if (front == -1) {
                        System.out.println("Queue is empty");
                    } else {
                        System.out.println("Deleted: " + arr[front]);
                        if (front == rear) {
                            // Only one element left
                            front = rear = -1;
                        } else {
                            front = (front + 1) % arr.length;
                        }
                    }
                }
                break;

                case 3 : { // Print
                    if (front == -1) {
                        System.out.println("Queue is empty");
                    } else {
                        System.out.println("Queue contents:");
                        int i = front;
                        while (true) {
                            System.out.print(arr[i] + " ");
                            if (i == rear) break;
                            i = (i + 1) % arr.length;
                        }
                        System.out.println();
                    }
                }
                break;

                default : System.out.println("Invalid choice");
            }
        }

        in.close();
    }
}