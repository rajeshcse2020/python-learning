def stack_demo():
    stack = []

    # Push
    stack.append('A')
    stack.append('B')
    stack.append('C')
    print("Stack: ", stack)

    # Peek
    topElement = stack[-3]
    print("Peek: ", topElement)

    # Pop
    poppedElement = stack.pop()
    print("Pop: ", poppedElement)

    # Pop
    poppedElement = stack.pop()
    print("Pop: ", poppedElement)

    # Stack after Pop
    print("Stack after Pop: ", stack)

    # isEmpty
    isEmpty = not bool(stack)
    print("isEmpty: ", isEmpty)

    # Size
    print("Size: ",len(stack))

stack_demo()