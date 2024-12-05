#sorts a linked list of game data structs and searches through them based on name
#sort will be given the linked list. the name is stored in llist.node.game.name. return the node if found

def linearSearch(llist, name):
    current = llist.head
    while current != None:
        if current.game.name == name:
            return current
        current = current.next
    return None
