#main sort
def insertionSort(gamesList):
    if gamesList.head is None:
        return []

    sorted_list = []
    current = gamesList.head

    while current is not None:
        insert_sorted(sorted_list, current)
        current = current.next

    return sorted_list

#helper function
def insert_sorted(sorted_list, new_node):
    if not sorted_list:
        sorted_list.append(new_node)
    else:
        for i in range(len(sorted_list)):
            if new_node.game.name < sorted_list[i].game.name:
                sorted_list.insert(i, new_node)
                break
        else:
            sorted_list.append(new_node)