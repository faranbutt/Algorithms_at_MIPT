import heapq

def dk(graph,start):
    priority_queue = []
    heapq.heappush(priority_queue,(0,start))
    distances = {node:float('inf') for node in graph}
    distances[start] = 0
    visited = set()
    while priority_queue:
        current_distance,current_node = heapq.heappop(priority_queue)
        if current_node in visited:
            continue
        visited.add(current_node)
        for neighbour,weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbour]:
                distances[neighbour] = distance
                heapq.heappush(priority_queue,(distance,neighbour))
    return distances

graph = {
    "1":{"2":2,"3":4},
    "2":{"3":1,'4':7},
    "3":{"5":3,},
    "4":{"6":1},
    "5":{"4":2,"6":5},
    "6":{}
    }


start_node = "1"
sd = dk(graph,start_node)
print(sd)