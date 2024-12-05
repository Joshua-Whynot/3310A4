#binary search algorithm written by joshua whynot on 12/5/24
def binarySearch(gamesList, target_name):
    if gamesList.head is None: #skip empty
        return None

    start = 0
    end = gamesList.length - 1
    #binary search
    while start <= end:
        mid = (start + end) // 2
        mid_node = get_node_at_index(gamesList, mid)

        if mid_node.game.name == target_name:
            return mid_node
        elif mid_node.game.name < target_name:
            start = mid + 1
        else:
            end = mid - 1

    return None

def get_node_at_index(gamesList, index): #get node at index helper function
    current = gamesList.head
    for i in range(index):
        current = current.next
    return current