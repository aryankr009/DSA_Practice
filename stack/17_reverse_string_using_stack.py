text = input("Enter a string: ")

stack = []

for char in text:
    stack.append(char)

reverse = ""
while stack:
    reverse += stack.pop()

print("Reversed string:", reverse)
