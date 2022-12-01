
# find the shortest that Sam will travel to deliver items.


import math

maxsize = float('inf')

# helper functions


def firstMinEdge(adj, i):
    """
    find the minimum edge cost incident
    """
    min = maxsize
    for k in range(N):
        if adj[i][k] < min and i != k:
            min = adj[i][k]

    return min


def copyToFinal(current_path):
    """
    copy the solution to final_path[] and update final_res

    """
    final_path[:N + 1] = current_path[:]
    final_path[N] = current_path[0]


def secondMinEdge(adj, i):
    """
    find the second minimum edge cost incident
    """
    first, second = maxsize, maxsize
    for j in range(N):
        if i == j:
            continue
        if adj[i][j] <= first:
            second = first
            first = adj[i][j]

        elif (adj[i][j] <= second and adj[i][j] != first):
            second = adj[i][j]

    return second


def TravellingSalesmanProblemRec(adj, current_bound, current_weight,
                                 level, current_path, visited_nodes):
    """
    recursive function to find the optimal tour for sam
    """
    global final_res

    # base case is when we have reached level N which means we have covered all the towns once
    if level == N:

        # check if there is an edge from last vertex in path back to the first vertex
        if adj[current_path[level - 1]][current_path[0]] != 0:

            # curr_res has the total weight of the solution we got
            curr_res = current_weight + \
                adj[current_path[level - 1]][current_path[0]]
            if curr_res < final_res:
                copyToFinal(current_path)
                final_res = curr_res
        return

    # build the search space tree recursively
    for i in range(N):

        # Consider next vertex if it is not same
        if (adj[current_path[level - 1]][i] != 0 and visited_nodes[i] is False):
            temp = current_bound
            current_weight += adj[current_path[level - 1]][i]

            # different computation of current_bound for level 2 from the other levels
            if level == 1:
                current_bound -= ((firstMinEdge(adj,
                                                current_path[level - 1]) + firstMinEdge(adj, i)) / 2)
            else:
                current_bound -= ((secondMinEdge(adj,
                                                 current_path[level - 1]) + firstMinEdge(adj, i)) / 2)

            # current_bound + current_weight is the actual lower bound for the node that we have arrived on.
            if current_bound + current_weight < final_res:
                current_path[level] = i
                visited_nodes[i] = True

                # call TravellingSalesmanProblemRec for the next level
                TravellingSalesmanProblemRec(adj, current_bound, current_weight,
                                             level + 1, current_path, visited_nodes)

            # prune the node by resetting all changes to current_weight and current_bound
            current_weight -= adj[current_path[level - 1]][i]
            current_bound = temp

            # reset the visited_nodes array
            visited_nodes = [False] * len(visited_nodes)
            for j in range(level):
                if current_path[j] != -1:
                    visited_nodes[current_path[j]] = True


def TravellingSalesmanProblem(adj):

    # Calculate initial lower bound for the root node
    current_bound = 0
    current_path = [-1] * (N + 1)
    visited_nodes = [False] * N

    # Compute initial bound
    for i in range(N):
        current_bound += (firstMinEdge(adj, i) + secondMinEdge(adj, i))

    current_bound = math.ceil(current_bound / 2)

    visited_nodes[0] = True
    current_path[0] = 0

    # Invoke TravellingSalesmanProblemRec for current_weight equal to 0 and level 1
    TravellingSalesmanProblemRec(
        adj, current_bound, 0, 1, current_path, visited_nodes)


# Application of algorithm to the use case
# Adjacency matrix for the given graph - towns and distances
adj = [[0, 12, 10, 19, 8],
       [12, 0, 3, 7, 6],
       [10, 3, 0, 2, 20],
       [19, 7, 2, 0, 4],
       [8, 6, 20, 4, 0]]

# number of cities(nodes)
N = 5

# towns and distances
towns = {"AB": 12, "AC": 10, "AD": 19, "AE": 8, "BC": 3,
         "BD": 7, "BE": 6, "CD": 2, "CE": 20, "DE": 4}

# path for sam to follow
final_path = [None] * (N + 1)

# keep track of visited_nodes cities
visited_nodes = [False] * N

# stores the final minimum weight of shortest tour for sam
final_res = maxsize

# call the function to find the shortest path by passing the adjacency matrix of the towns
TravellingSalesmanProblem(adj)

print("Sam will follow the cities : ", end=' ')
for i in range(N + 1):
    path = final_path[i]
    print(chr(ord('A') + path), end=' ')


# the running time of the algorithm is O(n!)

# add test cities - matrix  - @brenda
# add memoization - @modester
# add total distance in kms - @deji
# confirm time complexity - @deji
