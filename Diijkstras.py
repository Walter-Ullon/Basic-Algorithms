#         |--- 6----- (a) -------1-----|
#         |            |               |
#         |            |               |
#  (start)             3             (fin)
#         |            |               |
#         |            |               |
#         |----2----- (b) -------5-----|



# note: all hashes store neighbors "directionally" i.e.:
# if "a" is "b's" neighbor, then "b" is not "a's" neighbor etc.

# hash that stores all the neighbors of "start" node and their weights
graph = {}
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2
# shows all the neighbors of node "start"
#print graph['start'].keys()
#print len(graph['start'])


# hash that stores all the neighbors of "a" node and their weights
graph['a'] = {}
graph['a']['fin'] = 1

# hash that stores all the neighbors of "b" node and their weights
graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5


# hash that stores all the neighbors of "fin" node and their weights
graph['fin'] = {}


# hash that stores the "cost" for each node
infinity = float("inf")
costs = {}
costs['a'] = 6
costs['b'] = 2
costs['fin'] = infinity


# hash that stores the "parents" of each node
parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None


# array that stores nodes already processed
processed = []


# function that finds the lowest cost node
def find_lowest_cost_node(costs):
    lowest_cost = infinity
    lowest_cost_node = None
    for node in costs:
        if costs[node] < lowest_cost and node not in processed:
            lowest_cost = costs[node]
            lowest_cost_node = node
    return lowest_cost_node



node = find_lowest_cost_node(costs)         # b
while node is not None:
    cost = costs[node]                      # 2
    neighbors = graph[node]                 # {a:3 , fin:5}
    for i in neighbors.keys():              # [a, fin] -- keys
        new_cost = cost + neighbors[i]      # 2 + 3
        if costs[i] > new_cost:             # if 6 > 5
            costs[i] = new_cost             # cost[a] = 5
            parents[i] = node               # parent[a] = b
    processed.append(node)                  # processed b
    node = find_lowest_cost_node(costs)     # next closest node (a)....


# function that returns the full path
def find_path(end_node):
    path = []
    path.append(end_node)
    inParents = parents.keys()
    i = 1

    while inParents:
        path.append(parents[end_node])
        inParents.pop(inParents.index(end_node))
        end_node = path[i]
        i += 1
    path.reverse()
    return path



print "The cheapest path is: " + str(find_path('fin'))