# Balanced Parenthesis using Stack

def is_balanced(expression):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}

    for char in expression:
        # If opening bracket, push to stack
        if char in pairs.values():
            stack.append(char)

        # If closing bracket, check matching
        elif char in pairs:
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()

    # If stack is empty, parentheses are balanced
    return len(stack) == 0


# Driver code
expression = input("Enter the expression to check: ")

if is_balanced(expression):
    print("The parenthesis are balanced")
else:
    print("The parenthesis are not balanced")
