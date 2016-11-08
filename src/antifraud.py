# Leon Zhu

import sys
# to print a dictionary nicely
import pprint

def make_tree():
    with open(sys.argv[1], encoding="utf-8") as batchfile:
        graph = dict()
        #for i, n_line in zip(range(1969207), batchfile):
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
    with open(sys.argv[2], encoding="utf-8") as streamfile:
        # for i, n_line in zip(range(7), streamfile):
        for line in streamfile:
            tempstring = streamfile.readline()
            # print(tempstring)
            if len(tempstring.split(", ")) == 5:
                A = tempstring.split(", ")[1]
                B = tempstring.split(", ")[2]
                feature = bfs(graph, A, B)
                with open(sys.argv[3], 'a') as outfile:
                    if feature[0] == 1:
                        outfile.write('trusted\n')
                    else:
                        outfile.write('unverified\n')
                with open(sys.argv[4], 'a') as outfile:
                    if feature[1] == 1:
                        outfile.write('trusted\n')
                    else:
                        outfile.write('unverified\n')
                with open(sys.argv[5], 'a') as outfile:
                    if feature[2] == 1:
                        outfile.write('trusted\n')
                    else:
                        outfile.write('unverified\n')

def bfs(graph, start, end):
    # counter for depth of tree
    level = 0
    feat = [0, 0, 0]
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
        if level == 1 and node == end:
            feat[0] = 1
        if level <= 2 and node == end:
            feat[1] = 1
        if level > 4:
            break
        if level < 5 and node == end:
            #print(level)
            #print(path)
            feat[2] = 1
            break
        # enumerate all adjacent nodes, construct a new path and push it into the queue
        for adjacent in graph.get(node, []):
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)
    return feat

# main
data = make_tree()
traverse_tree(data)