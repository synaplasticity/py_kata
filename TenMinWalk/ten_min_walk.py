def isValidWalk(walk_dir):
    return len(walk_dir) is 10 and walk_dir.count('n') == walk_dir.count('s') and walk_dir.count('e') == walk_dir.count('w')
