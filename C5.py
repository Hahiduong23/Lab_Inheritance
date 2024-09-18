class Stack:
    def __init__(self):
        self.data = []
    def push(self,item: str):
        if not isinstance(item, str):
            raise ValueError("Ko phải chuỗi")
        self.data.append(item)
    def pop(self):
        if self.is_empty():
            raise IndexError("Ngăn xếp trống")
        return self.data.pop()
    def peek(self):
        if self.is_empty():
            return None
        return self .data[-1]
    def is_empty(self):
        return len(self.data) == 0
    def __str__(self):
        return f"Stack: {', '.join(self.data)}"
    

stack = Stack()

stack.push("apple")
stack.push("banana")
stack.push("cherry")

print(stack)  
print(stack.peek()) 
print(stack.pop())  
print(stack.is_empty())  
print(stack)  
