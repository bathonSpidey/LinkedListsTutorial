class LinkedList():
    def __init__(self):
        self.head = None
        self.length = 0

    def add(self, node):
        if self.head is None:
            self.is_head_none(node)
        else:
            current_node = self.head
            while current_node.tail != None:
                current_node = current_node.tail
            current_node.tail = node
            self.length+=1

    def is_head_none(self, node):
        self.head = node
        self.length+=1
    
    def add_head(self, node):
        if self.head is None:
            self.is_head_none(node)
        else:
            node.tail = self.head
            self.head = node
            self.length+=1

    def search(self, data):
        current_node = self.head
        while current_node != None:
            if current_node.data == data:
                return current_node
            current_node = current_node.tail
        return None

    