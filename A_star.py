graph = {
    'S': {'A': 3, 'B': 2},
    'A': {'C': 2},
    'B': {'C': 4, 'D': 5},
    'C': {'G': 4},
    'D': {'G': 1},
    'G': {}
}

h = {
    'S': 5,
    'A': 3,
    'B': 4,
    'C': 2,
    'D': 1,
    'G': 0
}


def astar(start, goal):

    open_list = [start]
    closed = []

    g = {start: 0}
    parent = {start: None}

    while open_list:

        current = open_list[0]

        # Find minimum f = g + h
        for node in open_list:
            if g[node] + h[node] < g[current] + h[current]:
                current = node

        print("Current:", current)

        if current == goal:

            path = []

            while current is not None:
                path.append(current)
                current = parent[current]

            path.reverse()

            print("Path:", " -> ".join(path))
            print("Cost:", g[goal])
            return

        open_list.remove(current)
        closed.append(current)

        for neighbor, cost in graph[current].items():

            new_cost = g[current] + cost

            if neighbor not in g or new_cost < g[neighbor]:

                g[neighbor] = new_cost
                parent[neighbor] = current

                if neighbor not in open_list and neighbor not in closed:
                    open_list.append(neighbor)


astar('S', 'G')