class Stack:
    def __init__(self,size=5):
        self.status=[]*size
        self.size=size
        self.top=-1
    
    def push(self,value):
        if self.top==self.size-1:
            print("Stack Oveflow ")
            return
        self.top+=1
        self.status[self.top]=value
    def pop(self):
        if self.top==-1:
            print("Stack Underflow")
            return
        self.top-=1
        return self.status[self.top+1]
    def peek(self):
        if self.top==-1:
            print("Stack is empty")
            return
        print(self.stauts[self.top]) 
    def isFull(self):
        return self.top==self.size-1
    def isEmpty(self):
        return self.top==-1
    

uds=Stack(10)
rds=Stack(10)