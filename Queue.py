class Queue:
    def __init__(self): # works as a constructor
        self.queue = []

    # Enqueue (Adding to the rear)
    def enqueue(self, item): # adds item to the end of the queue
        self.queue.append(item)

    # Dequeue (Remove from the front)
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0) #remove first elemnt
        else:
            raise IndexError("Queue is empty")

    # Peek (view the front element)
    def peek(self):
        if not self.is_empty():
            return self.queue[0] #first elemnt
        else :
            raise IndexError("Queue is empty")

    #check if the queue is empty
    def is_empty(self):
        return len(self.queue) == 0

    # Get the size of the queue
    def size(self):
        return len(self.queue)


#Usage
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
print('Queue: ', queue.queue)

print('Dequeue: ', queue.dequeue())
print('Queue after dequeue: ', queue.queue)

print('Front elemnt: ', queue.peek())



