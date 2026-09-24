from collections import deque

def generate_binary(n):
    queue = deque()
    result = []

    queue.append("1")

    for _ in range(n):
        current = queue.popleft()
        result.append(current)

        # Add next binary numbers
        queue.append(current + "0")
        queue.append(current + "1")

    return result


n = int(input("Enter n: "))

print("Binary numbers:")
print(generate_binary(n))
