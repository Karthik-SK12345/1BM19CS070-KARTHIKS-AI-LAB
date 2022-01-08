def bfs(src, target):
    queue = []
    queue.append(src)

    exp = []  # explored states
    while len(queue) > 0:  # while all states havent been explored
        # dequeing first element printing it and then exploring all its possible states
        source = queue.pop(0)
        exp.append(source)  # the given stated has been explored

        print(source)
        if source == target:
            print("success")
            return
        pos_moves = []
        pos_moves = possible_moves(source, exp)
        for moves in pos_moves:
            if moves not in exp and moves not in queue:
                queue.append(moves)


def gen(source, dir, b):
    # function to generate the next state
    new_state = source.copy()
    if dir == 'd':
        new_state[b + 3], new_state[b] = new_state[b], new_state[b + 3]
    if dir == 'u':
        new_state[b - 3], new_state[b] = new_state[b], new_state[b - 3]
    if dir == 'r':
        new_state[b + 1], new_state[b] = new_state[b], new_state[b + 1]
    if dir == 'l':
        new_state[b - 1], new_state[b] = new_state[b], new_state[b - 1]
    return new_state


def possible_moves(source, explored):
    direction = []  # possible directions it can move in
    # we see which direction we can move based on index of blank space
    # index of blank space
    b = source.index(-1)
    if b not in [0, 1, 2]:
        direction.append('u')
    if b not in [6, 7, 8]:
        direction.append('d')
    if b not in [0, 3, 6]:
        direction.append('l')
    if b not in [2, 5, 8]:
        direction.append('r')
    # finding(generating) new state for each direction when that direction is tried
    possible_states = []
    for dir in direction:
        possible_states.append(gen(source, dir, b))

    # list comprehension to add only the unvisited states
    return [un_move for un_move in possible_states if un_move not in explored]


src = []
goal = []
print("enter the values from 1 to 8 row-wise and -1 for blank:")
for i in range(9):
    src.append(int(input("Enter the val for index {}:".format(i))))
print("source:")
print(src)
print("enter the values from 1 to 8 row-wise and -1 for blank:")
for i in range(9):
    goal.append(int(input("Enter the val for index {}:".format(i))))
print("goal:")
print(goal)
print(20 * "*")
bfs(src, goal)  # passing source and target to user
