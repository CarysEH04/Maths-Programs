def josephus_problem(n, k):
    circle = list(range(1, n+1))
    index = k-1
    not_killed = _rec(circle, index)
    not_killed = str(not_killed)
    if not_killed[len(not_killed)-1] == '1':
        suffix = 'st'
    elif not_killed[len(not_killed)-1] == '2':
        suffix = 'nd'
    elif not_killed[len(not_killed)-1] == '3':
        suffix = 'rd'
    else:
        suffix = 'th'
    return 'The ' + str(not_killed) + suffix + ' person will survive'

def _rec(size, kill):
    if len(size) == 1:
        return size[0]
    else:
        kill = kill%len(size)
        size1 = size[0:kill]
        size2 = size[kill+1:]
        size = size2+size1
        return _rec(size, kill)

print(josephus_problem(11, 2))