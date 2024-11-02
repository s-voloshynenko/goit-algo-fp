import heapq
import networkx as nx

G = nx.Graph()

cities = [
    "Dnipro", "Kyiv", "Kharkiv", "Lviv", "Odesa", "Zhytomyr", 
    "Vinnytsia", "Rivne", "Donetsk", "Luhansk", "Simferopol"
]

G.add_nodes_from(cities)

weighted_edges = [
    ("Kyiv", "Dnipro", 495), ("Kyiv", "Kharkiv", 410), ("Kyiv", "Odesa", 441), 
    ("Kyiv", "Zhytomyr", 139), ("Lviv", "Rivne", 210), ("Rivne", "Zhytomyr", 189),
    ("Vinnytsia", "Zhytomyr", 129), ("Vinnytsia", "Dnipro", 573), ("Lviv", "Vinnytsia", 364),
    ("Kharkiv", "Luhansk", 338), ("Luhansk", "Donetsk", 155), ("Dnipro", "Donetsk", 258),
    ("Dnipro", "Odesa", 455), ("Dnipro", "Simferopol", 539),
]

G.add_weighted_edges_from(weighted_edges)

def dijkstra(graph, start):
    distances = {vertex: float("infinity") for vertex in graph.nodes}
    distances[start] = 0
    priority_queue = [(0, start)]
    visited = set()

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_vertex in visited:
            continue
        visited.add(current_vertex)

        for neighbor in graph.neighbors(current_vertex):
            weight = graph[current_vertex][neighbor].get("weight", 1)
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

start_node = "Kyiv"
shortest_paths = dijkstra(G, start_node)

print(f"Shortest paths from '{start_node}': {shortest_paths}")
