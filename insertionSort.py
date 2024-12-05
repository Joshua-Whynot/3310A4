from gamesList import gamesLinkedList

#main sort
def insertionSort(gamesList):
    if gamesList.head is None:
        return

    sorted_list = gamesLinkedList()
    current = gamesList.head

    while current is not None:
        next_node = current.next
        current.prev = current.next = None
        insert_sorted(sorted_list, current)
        current = next_node

    gamesList.head = sorted_list.head
    gamesList.tail = sorted_list.tail

#helper function
def insert_sorted(sorted_list, new_node):
    if sorted_list.head is None:
        sorted_list.head = sorted_list.tail = new_node
    elif new_node.game.name < sorted_list.head.game.name:
        new_node.next = sorted_list.head
        sorted_list.head.prev = new_node
        sorted_list.head = new_node
    else:
        current = sorted_list.head
        while current.next is not None and current.next.game.name < new_node.game.name:
            current = current.next
        new_node.next = current.next
        if current.next is not None:
            current.next.prev = new_node
        else:
            sorted_list.tail = new_node
        current.next = new_node
        new_node.prev = current