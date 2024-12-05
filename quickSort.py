from gamesList import gamesLinkedList

def quickSort(gamesList):
    if gamesList.head is None or gamesList.head.next is None:
        return

    gamesList.head = quicksort_rec(gamesList.head, gamesList.tail)
    current = gamesList.head
    while current.next is not None:
        current = current.next
    gamesList.tail = current

def quicksort_rec(head, tail):
    if head is None or head == tail:
        return head

    new_head, new_tail, pivot = partition(head, tail)
    if new_head != pivot:
        temp = new_head
        while temp.next != pivot:
            temp = temp.next
        temp.next = None
        new_head = quicksort_rec(new_head, temp)
        temp = get_tail(new_head)
        temp.next = pivot
        pivot.prev = temp

    pivot.next = quicksort_rec(pivot.next, new_tail)
    if pivot.next:
        pivot.next.prev = pivot

    return new_head

def partition(head, tail):
    pivot = tail
    prev = None
    current = head
    new_head = None
    new_tail = pivot

    while current != pivot:
        if current is None:
            break
        next_node = current.next
        if current.game.name < pivot.game.name:
            if new_head is None:
                new_head = current
            prev = current
        else:
            if prev:
                prev.next = current.next
            if current.next:
                current.next.prev = prev
            current.next = None
            new_tail.next = current
            current.prev = new_tail
            new_tail = current
        current = next_node

    if new_head is None:
        new_head = pivot

    return new_head, new_tail, pivot

def get_tail(node):
    while node.next is not None:
        node = node.next
    return node