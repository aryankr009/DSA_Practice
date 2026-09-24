class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def merge_lists(head1, head2):
    dummy = Node(0)
    current = dummy

    while head1 and head2:
        if head1.data <= head2.data:
            current.next = head1
            head1 = head1.next
        else:
            current.next = head2
            head2 = head2.next

        current = current.next

    
    if head1:
        current.next = head1
    else:
        current.next = head2

    return dummy.next


def print_list(head):
    current = head

    while current:
        print(current.data, end=" -> ")
        current = current.next

    print("None")


head1 = Node(1)
head1.next = Node(3)
head1.next.next = Node(5)

head2 = Node(2)
head2.next = Node(4)
head2.next.next = Node(6)

merged = merge_lists(head1, head2)

print("Merged sorted list:")
print_list(merged)
