stack = []
stack.append(10)
stack.append(20)
stack.append(30)

print("Stack:", stack)

item = stack.pop()
print("Popped:", item)
print("Stack after pop:", stack)

if stack:
    print("Top:", stack[-1])
else:
    print("Stack is empty")
