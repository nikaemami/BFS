# BFS
a BFS algorithm is implemented to find the shortest path between two points in an n dimensional space.

<h2>Interstellar:</h2>

We want to find the shortest path between (0,0,...,0) and (x,x,...,x) considering **obstacles** in between.

INPUT: In the first line n,m, and x are given. n is the **number of dimensions**, m is the **number of obstacles**, and x is the **destination point**. In the next m lines, n numbers are given (a1,a2,...,an) which indicate the **coordinates of each obstacle**.

OUTPUT: The length of the shortest path is printed. If no such path exists, -1 is printed.

First, a function is implemented which finds the **children of each node**, as below:

```ruby
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
```

Next, this function is used in the main **bfs** function.

```ruby
def BFS(final, s, n, obstacles)
```

By using the BFS algorithm, the shortest path between points in the n-dimensional space can be found recursively.


