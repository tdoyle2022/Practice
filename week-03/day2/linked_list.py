# class LLQueue:
#     def __init__(self):
#         self.total = 0
#         self.queue = []

#     def enqueue(self, data):
#         new_node = Node(data)
#         if not self.queue:
#             self.queue = new_node
#         else:
#             current = self.queue
#             while current.next:
#                 current = current.next
#             current.next = new_node

#         self.total += 1

#     def dequeue(self):
#         val = self.queue[0]
#         self.queue = self.queue[1:]
#         self.total -= 1
#         return val

#     def size(self):
#         return self.total
    
# class Node:
#     def __init__(self, val = None):
#         self.value = val
#         self.next = None
#         self.prev = None

# q = LLQueue()
# q.enqueue(3)
# q.enqueue(4)

# current = q.queue
# while current:
#     print(current.value)
#     current = current.next

class LinkedList:

    def __init__(self):
        self.length = 0
        self.head = None

    def add(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            
            current_node.next = new_node
        self.length += 1
    
    def remove(self, data):
        if self.head == None:
            return 
        
        elif self.length == 1:;

        cur = train.head

        while cur:
            print(cur.data)
            cur = cur.next
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

train = LinkedList()
train.add('cars')
train.add('coal')
train.add('oil')
print(train)

cur = train.head
while cur:
    print(cur.data)
    cur = cur.next