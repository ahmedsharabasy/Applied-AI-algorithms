def BFS(tree,start,dest):
    queue=list()
    visited=list()
    queue.append(start)
    print('visited',start)
    result=["not reachable",list()]
    while queue:
        node=queue.pop(0)
        visited.append(node)
        if node==dest:
            print('destination node found', node)
            result[0]='reachable'
            break
        print(node,'is not a destination node')
        for child in tree[node]:
            if child not in visited:
                queue.append(child)
        result[1]=visited 
        return result

tree={'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F', 'G'], 'D': ['H', 'J'], 'E': [], 'F': ['I', 'K'],
'G': ['L', 'M'], 'H': [], 'J': [], 'I': [], 'K': [], 'L': [], 'M': []}

result = BFS(tree, 'A', 'M')
print(result[0])
print("Path used to traverse :-", result[1])   
