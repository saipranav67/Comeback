# Circular Singly Linked List Implementation

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.last = None

    # Insert at beginning or end
    def insert(self, end=False):
        data = int(input("Enter value to insert: "))
        new = Node(data)

        if self.last is None:
            self.last = new
            self.last.next = self.last
            print(f"{data} entered")
            return

        new.next = self.last.next
        self.last.next = new

        if end:
            self.last = new

        print(f"{data} entered")

    # Insert at specific position
    def insert_pos(self):
        self.display()
        data = int(input("Enter value to insert: "))
        pos = int(input("Enter position to insert: "))

        new = Node(data)
        temp = self.last.next
        t = 1

        if pos == 1:
            new.next = temp
            self.last.next = new
            print(f"{data} entered")
            return

        while temp != self.last and t < pos - 1:
            temp = temp.next
            t += 1

        if temp == self.last and t + 1 < pos:
            print("Position out of index")
            return

        new.next = temp.next
        temp.next = new
        print(f"{data} entered")

    # Delete at beginning or end
    def delete(self, end=False):
        if self.last is None:
            print("List is empty")
            return

        if self.last.next == self.last:
            print(f"{self.last.data} deleted")
            self.last = None
            return

        if not end:
            temp = self.last.next
            self.last.next = temp.next
            print(f"{temp.data} deleted")
        else:
            temp = self.last.next
            while temp.next != self.last:
                temp = temp.next
            print(f"{self.last.data} deleted")
            temp.next = self.last.next
            self.last = temp

    # Delete at specific position
    def delete_pos(self):
        self.display()
        pos = int(input("Enter position to delete: "))

        if self.last is None:
            print("List is empty")
            return

        temp = self.last.next
        t = 1

        if pos == 1:
            self.delete(end=False)
            return

        while temp.next != self.last and t < pos - 1:
            temp = temp.next
            t += 1

        if temp.next == self.last and t + 1 < pos:
            print("Position out of index")
            return

        removed = temp.next
        temp.next = removed.next
        print(f"{removed.data} deleted")

    # Display list
    def display(self):
        if self.last is None:
            print("List is empty")
            return

        temp = self.last.next
        pos = 1
        while True:
            print(f"{temp.data} [{pos}]", end=" -> ")
            if temp == self.last:
                break
            temp = temp.next
            pos += 1
        print()


def main():
    lst = CircularLinkedList()

    while True:
        print("\nCircular Linked List Menu")
        print("1. Insert Element")
        print("   By Beginning (1b)")
        print("   By End (1c)")
        print("   By Position (1p)")
        print("2. Delete Element")
        print("   By Beginning (2b)")
        print("   By End (2c)")
        print("   By Position (2p)")
        print("3. Print Linked List")
        print("4. Exit")

        op = input("Enter your choice: ").lower()

        if op[0] == '1':
            if len(op) > 1 and op[1] == 'p':
                lst.insert_pos()
            else:
                lst.insert(end=(len(op) > 1 and op[1] == 'c'))

        elif op[0] == '2':
            if len(op) > 1 and op[1] == 'p':
                lst.delete_pos()
            else:
                lst.delete(end=(len(op) > 1 and op[1] == 'c'))

        elif op[0] == '3':
            lst.display()

        elif op[0] == '4':
            print("Exiting")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
