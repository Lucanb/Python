class Stack:
    
    def __init__(self):
        self.items=[]

    def empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)    
    
    def peek(self):
        if not self.empty():
            return self.items[-1]
        else:
            return None

    def pop(self):
        if not self.empty(): 
            return self.items.pop()
        else:
            return None
        
    def push(self,number):
        self.items.append(number)    
           
if __name__ == '__main__':
    
    my_stack = Stack()
    my_stack.push(1)
    my_stack.push(2)
    my_stack.push(3)

    print(my_stack.items)
    print(my_stack.pop())
    print(my_stack.peek())
    print(my_stack.size())           