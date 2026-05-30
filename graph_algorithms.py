# explanations for these functions are provided in requirements.py

# Explanations for graph algorithm functions
#
# get_degree_distribution(): returns a dictionary representing the degree distribution of the graph.
#                            the keys are the degree, and the values is the number of nodes with that
#                            degree.

from graph import Graph
import random
from collections import deque

'''
first bfs (bfs random) = random node to get the furthest node 
second bfs (def bfs_max_distance, calls bfs )= gets the max distance 

bfs_random = uses random num gen; inputs random num to bfs; returns [node, distance]
bfs = uses node; returns [node, distance]
bfs_max_distance = calls bfs; uses node to find max distance; returns distance
get_diameter = calls bfs_max_distance a few times, then picks the max
'''

# [int, int] being [node, distance]
def bfs_random(graph:Graph) -> list[int, int]:
	random_num = random.randint(0, graph.get_num_nodes()-1)
	return bfs(graph, random_num)
	
# [int, int] being [node, distance]
def bfs(graph:Graph, node:int) -> list[int, int]:
	deq = deque([node])
	seen = set([node])
	distance = {}
	distance[node] = 0

	while deq:
		cur = deq.popleft()
		
		neighbors = graph.get_neighbors(cur)
		for neighbor in neighbors:
			if neighbor not in seen:
				seen.add(neighbor)
				deq.append(neighbor)
				distance[neighbor] = distance[cur] + 1
	furthest_node = max(distance, key=distance.get)
	dist = distance[furthest_node]
	return [furthest_node, dist]

# returns distance
def bfs_max_distance(graph:Graph) -> int:
	bfs1 = bfs_random(graph)
	dis1 = bfs1[1]
	bfs2 = bfs(graph, bfs1[0])
	dis2 = bfs2[1]

	return max(dis1, dis2)


# get_diameter(): return the approximate graph diameter using a heuristic function.
def get_diameter(graph: Graph) -> int:
	if graph.get_num_nodes() < 10:
		return bfs_max_distance(graph)
	else:
		return max(bfs_max_distance(graph), bfs_max_distance(graph), bfs_max_distance(graph))
	

	

# get_clustering_coefficient(): return the graph's global clustering coefficient.
def get_clustering_coefficient(graph: Graph) -> float:
	clusters = {}
	total_nodes = graph.get_num_nodes()
	cluster_total = 0

	for i in range(total_nodes):
		# k = number of neighbors of u 
		k = graph.get_num_neighbors(i)
		#print(f"k: {k}")

		max_num_edges = (k * (k-1))/2
		#print(f"max_num_edges: {max_num_edges}")

		actual_neighbor_edges = graph.count_edges_between_neighbors(i)
		#print(f"actual_neighbor_edges: {actual_neighbor_edges}")

		cluster = (actual_neighbor_edges / max_num_edges)
		clusters[i] = cluster
		cluster_total += cluster
		
		#print(f"cluster: {cluster}")
			

	#print("All the clusters of each node: ")
	#print(clusters)

	#print(f"cluster_total: {cluster_total}")
	
	cluster_avg = cluster_total / total_nodes

	return cluster_avg


def get_degree_distribution(graph: Graph) -> dict[int, int]:
	raise NotImplementedError
