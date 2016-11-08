# Leon Zhu

# to print a dictionary nicely
import pprint

def make_tree():
    with open("batch_payment.csv", encoding="utf-8") as batchfile:
        graph = dict()
        # for i, n_line in zip(range(1969207), batchfile):
        for line in batchfile:
            tempstring = batchfile.readline()
            # print(tempstring)
            if len(tempstring.split(", ")) == 5:
                A = tempstring.split(", ")[1]
                B = tempstring.split(", ")[2]
                if A in graph:
                    graph[A].append(B)
                else:
                    graph[A] = [B]
        # pprint.pprint(graph)
        return graph

def traverse_tree(graph):
    with open("stream_payment.csv", encoding="utf-8") as streamfile:
        # do a breadth first search
        print(streamfile.readline())
        tempstring = streamfile.readline()
        print(tempstring)
        A = tempstring.split(", ")[1]
        B = tempstring.split(", ")[2]
        print(bfs(graph, A, B))

def bfs(graph, start, end):
    # counter for depth of tree
    level = 0
    # maintain a queue of paths
    queue = list()
    # push the root into the queue
    queue.append([start])
    # placeholder to track when next depth is reached
    queue.append(['level'])
    while queue:
        # get the first path from the queue
        path = queue.pop(0)
        # increment level at placeholder
        if path == ['level']:
            level+=1
            queue.append(['level'])
            path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        # path found or condition met
        if level > 4:
            return 'Unverified'
        if node == end:
            # print(path)
            return 'Verified'
        # enumerate all adjacent nodes, construct a new path and push it into the queue
        for adjacent in graph.get(node, []):
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)
    # if no connection exists
    if queue == []:
        return "Unverified"

# main
data = make_tree()
traverse_tree(data)