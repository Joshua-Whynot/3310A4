#standard quicksort implementation written by joshua whynot on 12/6/24
def quickSort(gamesList):
    if gamesList.head is None:
        return []

    nodes = []
    current = gamesList.head
    while current is not None:
        nodes.append(current)
        current = current.next

    return quicksort_rec(nodes)

#recursive helper function
def quicksort_rec(nodes):
    if len(nodes) <= 1:
        return nodes

    pivot = nodes[len(nodes) // 2]
    left = [x for x in nodes if x.game.name < pivot.game.name]
    middle = [x for x in nodes if x.game.name == pivot.game.name]
    right = [x for x in nodes if x.game.name > pivot.game.name]

    return quicksort_rec(left) + middle + quicksort_rec(right)