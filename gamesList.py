#doubly linked list of games
class gamesLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    #add function
    def addGame(self, node):
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.length += 1
        
    #delete function
    def deleteGame(self, node):
        if node == self.head:
            self.head = node.next
        else:
            node.prev.next = node.next
        if node == self.tail:
            self.tail = node.prev
        else:
            node.next.prev = node.prev
        self.length -= 1
    

 
    