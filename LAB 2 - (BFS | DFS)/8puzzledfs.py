src = [1,2,3,-1,4,5,6,7,8]
target = [-1, 1, 3, 6, 2, 5, 7, 4, 8]
visited_states =[]

def next_state(cur,move,idx) :
    temp = cur[:]
    if move == 'D' : temp[idx],temp[idx+3] = temp[idx+3],temp[idx]
    if move == 'R' : temp[idx],temp[idx+1] = temp[idx+1],temp[idx]
    if move == 'L' : temp[idx],temp[idx-1] = temp[idx-1],temp[idx]
    if move == 'U' : temp[idx],temp[idx-3] = temp[idx-3],temp[idx]
    return temp

def gen_states(cur) :
    moves = []
    states = []
    idx = cur.index(-1)
    if idx>2 : moves.append('U')
    if idx%3>0 : moves.append('L')
    if idx<6 : moves.append('D')
    if idx%3<2 : moves.append('R')
    for move in moves :
        state = next_state(cur,move,idx)
        states.append(state)
    return states
    
def dfs(cur,target,visited_states) :
    if cur == target :
        print(cur)
        print("target reached!")
        exit()
    print(cur)
    visited_states.append(cur)
    nxt_states = gen_states(cur)
    for state in nxt_states :
        if not state in visited_states :
            dfs(state,target,visited_states)

dfs(src,target,visited_states)
