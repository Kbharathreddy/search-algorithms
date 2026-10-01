
graph={'A':[[('B',1)],[('C',1),('D',1)]],'B':[[('E',1)],[('F',2)]],'C':[[('G',1)]],'D':[[('H',1)]]}

def ao_star(node):
    if node not in graph:
        return 0
    best_cost = 999
    best_option=None

    for option in graph[node]:

        cost=0

        for child,edge_cost in option:
            cost+=edge_cost+ao_star(child)

        if cost<best_cost:
            best_cost=cost
            best_option=option

    print("Node:",node,"Best option:",best_option,"Cost:",best_cost)

    return best_cost
result=ao_star('A')
print("optimal cost:",result)