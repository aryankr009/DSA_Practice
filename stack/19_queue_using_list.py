queue = []


queue.append(10)
queue.append(20)
queue.append(30)

print("Queue:", queue)

if queue:
    item = queue.pop(0)
    print("Dequeued:", item)

print("Queue after dequeue:", queue)

if queue:
    print("Front:", queue[0])
else:
    print("Queue is empty")
