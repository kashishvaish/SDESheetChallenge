# Queue implementation using Python List
class Queue :

    def __init__(self):
        self.queue = []

    '''----------------- Public Functions of Queue -----------------'''
    def isEmpty(self) :
        if len(self.queue) == 0:
            return True
        return False

    def enqueue(self, data) :
        self.queue.append(data)

    def dequeue(self) :
        if self.isEmpty(): return -1
        return self.queue.pop(0)

    def front(self) :
        if self.isEmpty(): return -1
        return self.queue[0]
