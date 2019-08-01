#这是一个栈，我开始理解错了，修改名字太麻烦了，所有就算了
class back_queue:
    queue_maxsize = 10

    def __init__(self):
        self.queue_size = 0
        self.queue = []
    def is_empty(self):
        return self.queue == []
    def add(self,li):
        if self.queue_size < back_queue.queue_maxsize:
            self.queue.insert(self.queue_size,li)
            self.queue_size+=1
        else:
            self.queue.pop(0)
            self.queue.insert(self.queue_size,li)
    def remove(self):
        if self.queue_size !=0:
            self.queue_size -=1
            return self.queue.pop()
        return None