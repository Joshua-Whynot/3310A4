#standard binary search implementation written by joshua whynot on 12/6/24
def binarySearch(list, target_name):
    start = 0
    end = len(list) - 1

    while start <= end:
        mid = (start + end) // 2
        mid_node = list[mid]

        if mid_node.game.name == target_name:
            return mid_node
        elif mid_node.game.name < target_name:
            start = mid + 1
        else:
            end = mid - 1

    return None