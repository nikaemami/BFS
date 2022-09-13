import numpy as np

first_row = list(map(int,input().split()))

n = first_row[0]
m = first_row[1]
x = first_row[2]

obstacles = []
for i in range(m):
    obstacles.append(list(map(int,input().split())))

visited = []
queue = []
queue.append(np.zeros(n))

def find_children(v):
    children = []
    for i in range (n):
        temp = copy.copy(v)
        if (v[i] >= 1):
            temp[i] = v[i]-1
            children.append(temp)
        if (v[i] <= x-1):
            temp[i] = v[i]+1
            children.append(temp)
    return(children)

final = []
def BFS(final, s, n, obstacles):
 
        visited = [False] * (2 ** n)
        queue = []
        queue.append(s)
        visited[s] = True
 
        while queue:
            s = queue.pop(0)
            final.append(s)
 
            children = find_children(s)
            for i in children:
                if ((visited[i] == False) and (i not in obstacles)):
                    queue.append(i)
                    visited[i] = True
        return(final)
print('-1')
