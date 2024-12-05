#node class for gamesLinkedList
class node:
    def __init__(self, game):
        self.game = game
        self.next = None
        self.prev = None
        self.index = 0