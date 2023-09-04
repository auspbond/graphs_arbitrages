from collections import defaultdict


# A modified version of DFS that returns vertexes (and parents) with a pre-visit and post-visit time
def clock_dfs(graph, traversal_order):
    visitations = defaultdict(list)
    parents = dict()
    status = dict()
    clock = 0
    for x in graph.keys():
        status.update({x: "NEW"})
    for x in traversal_order:
        if status.get(x) == "NEW":
            clock = clock_dfs_visit(graph, x, status, visitations, parents, clock)
    return visitations, parents


# A DFS that tracks a clock, parents, and visitation times
def clock_dfs_visit(graph, vertex, status, visitations, parents, clock):
    status.update({vertex: "ACTIVE"})
    clock += 1
    visitations[vertex].append(clock)
    vertex_edges = graph.get(vertex)

    for x in vertex_edges:
        if status.get(x) == "NEW":
            parents.update({x: vertex})
            clock = clock_dfs_visit(graph, x, status, visitations, parents, clock)
    status.update({vertex: "FINISHED"})
    clock += 1
    visitations[vertex].append(clock)
    return clock


# Classifies edges based on pre- / post-visit times of the vertexes
def classify_edges(edges_list, ordering, parent, vertex_dictionary):
    for x in edges_list:
        if x[0] in ordering.keys() and x[1] in ordering.keys():

            # Determine if the edge is a forward edge
            if ordering.get(x[0])[0] < ordering.get(x[1])[0] \
                    < ordering.get(x[1])[1] < ordering.get(x[0])[1]:
                if parent.get(x[1]) == x[0]:
                    print(x[0], x[1], "tree edge")
                else:
                    end_vertex_parent = parent.get(x[1])
                    second_parent = parent.get(end_vertex_parent)
                    if second_parent == x[0] and x[0] in vertex_dictionary.get(end_vertex_parent):
                        print(x[0], x[1], "illegal edge")
                    else:
                        print(x[0], x[1], "forward edge")

            # Determine if the edge is a cross edge
            elif ordering.get(x[1])[1] < ordering.get(x[0])[0]:
                if not ordering.get(x[0])[1] < ordering.get(x[1])[1]:
                    print(x[0], x[1], "cross edge")
                else:
                    print(x[0], x[1], "illegal edge")

            # Determine if the edge is a back edge
            elif ordering.get(x[1])[1] > ordering.get(x[0])[1] \
                    > ordering.get(x[0])[0] > ordering.get(x[1])[0]:
                if x[0] in parent.keys() and x[1] not in parent.keys():
                    print(x[0], x[1], "back edge")
                else:
                    print(x[0], x[1], "illegal edge")


def main():
    num_vertices = int(input())
    vertex_dictionary = defaultdict(list)

    for _ in range(num_vertices):
        vertexes = ([x for x in input().split(" ")])
        for _ in range(1, len(vertexes)):
            vertex_dictionary[vertexes[0]].append(vertexes[_])

    vertex_traversal_order = ([x for x in input().split(" ")])

    edge_query_num = int(input())
    edges_list = []

    for _ in range(edge_query_num):
        edge = ([x for x in input().split(" ")])
        edges_list.append(edge)

    ordering, parents = clock_dfs(vertex_dictionary, vertex_traversal_order)
    classify_edges(edges_list, ordering, parents, vertex_dictionary)


if __name__ == "__main__":
    main()
