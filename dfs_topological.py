from collections import defaultdict


# Reverses the graph
def reverse_graph(graph):
    reversed_graph = defaultdict(list)
    for x in graph.keys():
        for y in graph.get(x):
            if y:
                reversed_graph[y].append(x)
    return reversed_graph


# A topological dfs that tracks a clock and adds to a list of vertexes in topological order
def topological_sort_dfs(graph, vertex, status, clock, s):
    status.update({vertex: "ACTIVE"})
    vertex_edges = graph.get(vertex)
    for x in vertex_edges:
        if status.get(x) == "ACTIVE":
            exit()
        if status.get(x) == "NEW":
            clock = topological_sort_dfs(graph, x, status, clock, s)
    status.update({vertex: "FINISHED"})
    s[clock - 1] = vertex
    clock -= 1
    return clock


# Topological Sort initialization that returns a list of vertexes in topological order
def topological_sort(graph):
    status = dict()
    clock = len(graph.keys())
    s = [None] * clock
    for x in graph.keys():
        status.update({x: "NEW"})
    for x in graph.keys():
        if status.get(x) == "NEW":
            clock = topological_sort_dfs(graph, x, status, clock, s)
    return s


def main():
    num_vertices = int(input())
    vertex_dictionary = defaultdict(list)

    for _ in range(num_vertices):
        vertexes = ([x for x in input().split(" ")])
        if len(vertexes) > 1:
            for _ in range(1, len(vertexes)):
                vertex_dictionary[vertexes[0]].append(vertexes[_])
        else:
            vertex_dictionary[vertexes[0]].append([])

    reversed_graph = reverse_graph(vertex_dictionary)
    order = topological_sort(reversed_graph)

    for x in range(len(order) - 1, -1, -1):
        if reversed_graph.get(order[len(order) - 1])[0]:
            print(reversed_graph.get(order[x])[0], end=" ")
            break

    for x in range(len(order) - 1, -1, -1):
        print(order[x], end=" ")


if __name__ == "__main__":
    main()
