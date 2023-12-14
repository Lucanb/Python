class Queue:
 
    def __init__(self):
        self.items = []
    
    def empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def push(self,item):
        self.items.insert(0, item)
   
    def pop(self): 
         if not self.empty():
            return self.items.pop()
         else:
            return None

    def peek(self):
        if not self.empty():
            return self.items[-1]
        else:
            return None
        
        
if __name__ == '__main__':

    queue = Queue()
    queue.push(1)
    queue.push(2)
    queue.push(3)

    print(queue.items)
    print(queue.pop())
    print(queue.peek())
    print(queue.size())        