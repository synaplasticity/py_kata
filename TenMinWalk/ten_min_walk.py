def toggle_dir(dir):
    """
    Returns opposite of the given direction.
    dir : single char. e.g.: 'n'
    """
    direction = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}

    return direction[dir]


def isValidWalk(walk_dir):
    len_walk_dir = len(walk_dir)
    if len_walk_dir is not 10:
        return False

    # while len(walk_dir) > 0:
    for a in range(1, len_walk_dir - 1):
        if len(walk_dir) is 0:
            break
        opp_dir = toggle_dir(walk_dir[1])
        if opp_dir in walk_dir:
            del walk_dir[1]
            del walk_dir[walk_dir.index(opp_dir)]

    return len(walk_dir) is 0
