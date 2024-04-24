#There are n people standing in a circle, every kth person will be executed until 1 person remains
def josephus_problem(n, k):
    circle = list(range(1, n+1))
    index = k-1
    not_killed = str(_rec(circle, index))
    suffix = returnSuffix(not_killed)
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

def returnSuffix(number):
    if not_killed[len(not_killed)-1] == '1':
        suffix = 'st'
    elif not_killed[len(not_killed)-1] == '2':
        suffix = 'nd'
    elif not_killed[len(not_killed)-1] == '3':
        suffix = 'rd'
    else:
        suffix = 'th'
    return suffix

print(josephus_problem(11, 2))
