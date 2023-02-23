
class Queue:
    def __init__(self):
        self.total = 0
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)
        self.total += 1

    def dequeue(self):
        val = self.queue[0]
        self.queue = self.queue[1:]
        self.total -= 1
        return val

    def size(self):
        return self.total
test_queue = Queue()


test_queue.enqueue(3)
test_queue.enqueue(6)
test_queue.enqueue(9)

print(test_queue.queue)

test_queue.dequeue()

print(test_queue.queue)
print(test_queue.size())