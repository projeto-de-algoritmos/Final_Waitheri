def less(i, j, ordering):
    if ordering == 0 and i.pos.x < j.pos.x:
        return True
    elif ordering == 1 and i.pos.y < j.pos.y:
        return True
    return False

def exch(rooms, i, j):
    tmp = rooms[i]
    rooms[i] = rooms[j]
    rooms[j] = tmp

def partition (rooms, left, right, ordering):
    room = rooms[right]
    i = left
    for j in range(left, right):
        if less(rooms[j], room, ordering):
            exch(rooms, j, i)
            i += 1

    exch(rooms, i, right)
    return i

def quickSelect (rooms, left, right, k, ordering):
    if left >= right: return
    i = partition(rooms, left, right, ordering)
    if (i > k): quickSelect(rooms, left, i - 1, k, ordering)
    if (i < k): quickSelect(rooms, i + 1, right, k, ordering)
