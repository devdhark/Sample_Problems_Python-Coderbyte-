#  Using the Pyhton language, have the function ShortestPath(strArr) take strArr which will be an array of strings which
#  models a non-looping Graph. The structure of the array will be as follows: The first element in the array will be
#  the number of nodes N (points) in the array as a string. The next N elements will be the nodes which can be anything
#  (A, B, C .. Brick Street, Main Street .. etc.). Then after the Nth element, the rest of the elements in the array
#  will be the connections between all of the nodes. They will look like this:
#  (A-B, B-C .. Brick Street-Main Street .. etc.). Although, there may exist no connections at all.

#  An example of strArr may be: ["4","A","B","C","D","A-B","B-D","B-C","C-D"]. It may help to visualize the Graph by
#  drawing out the nodes and their connections. Your program should return the shortest path from the first Node to the
#  last Node in the array separated by dashes. So in the example above the output should be A-B-D. Here is another
#  example with strArr being ["7","A","B","C","D","E","F","G","A-B","A-E","B-C","C-D","D-F","E-D","F-G"].
#  The output for this array should be A-E-D-F-G. There will only ever be one shortest path for the array.
#  If no path between the first and last node exists, return -1. The array will at minimum have two nodes.
#  Also, the connection A-B for example, means that A can get to B and B can get to A.


def shortest_path(lst):
    # code goes here
    # slice array into k, nodes and the connections
    k = int(lst[0])
    nodes = lst[1:k+1]
    conn = lst[k+1:]
    start = nodes[0]
    goal = nodes[k-1]
    # create graph as a dictionary with nodes as key
    graph = {}
    for n in nodes:
        graph.setdefault(n, [])
        for c in conn:
            if n == c[0]:
                graph[n].append(c[2])
    # breath first search implementation
    lst = bfs(graph, start, goal)
    # arrange string into connection notation, ie, "A-B-C-D"
    for i, char in enumerate(lst):
        if i % 2 != 0:
            lst.insert(i, '-')
    # convery list back into string
    lst = "".join(lst)
    return lst


def bfs(graph, start, goal):
    # keep track of visited nodes
    visited = []
    # keep track of all paths
    queue = [[start]]
    # return a single node path if start is goal
    if start == goal:
        return [goal]
    # explore all possible paths
    while queue:
        # pop the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        if node not in visited:
            neighbours = graph[node]
            # construct a new path for all the neighbour nodes
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                # push it into the queue
                queue.append(new_path)
                # return path if neighbour is goal
                if neighbour == goal:
                    return new_path

            # mark node as visited
            visited.append(node)

    # return empty list as no path was found
    return []


# keep this function call here
print(shortest_path(["6", "A", "B", "C", "D", "E", "F",
                     "A-B", "A-D", "B-C", "C-D", "D-E", "E-F"]))
