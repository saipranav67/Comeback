# Queue Using Array (List)

size = 5
queue = []

def isEmpty():
    return len(queue) == 0

def isFull():
    return len(queue) == size

def enqueue(value):
    if isFull():
        print("\nQueue is Full")
    else:
        queue.append(value)
        print(f"{value} is inserted into the queue")

def dequeue():
    if isEmpty():
        print("\nQueue is Empty")
    else:
        removed = queue.pop(0)
        print(f"{removed} is removed from the queue")

def display():
    if isEmpty():
        print("\nQueue is Empty")
    else:
        print("\nCurrent Queue elements:", end=" ")
        for item in queue:
            print(item, end=" ")
        print()

def main():
    while True:
        print("\n1. Enqueue")
        print("2. Dequeue")
        print("3. Display Queue")
        print("4. Check if Queue is Empty")
        print("5. Check if Queue is Full")
        print("6. Exit")

        choice = int(input("Enter your choice (1-6): "))

        if choice == 1:
            value = int(input("Enter value to enqueue: "))
            enqueue(value)

        elif choice == 2:
            dequeue()

        elif choice == 3:
            display()

        elif choice == 4:
            if isEmpty():
                print("Queue is Empty")
            else:
                print("Queue is not Empty")

        elif choice == 5:
            if isFull():
                print("Queue is Full")
            else:
                print("Queue is not Full")

        elif choice == 6:
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
