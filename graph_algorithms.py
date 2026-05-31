# explanations for these functions are provided in requirements.py



from graph import Graph
import random
from collections import deque
import math

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
	
def round_down(val, dec=0):
	scale = 10 ** dec
	return math.floor(val * scale) / scale

def degen_ordering(graph: Graph):
	total_nodes = graph.get_num_nodes()
	current_degree = {i: graph.get_num_neighbors(i) for i in range(total_nodes)}

	L = []
	D = dict(sorted(graph.degree_distribution_nodes.items()))
	HL = set()
	Nv = {i: [] for i in range(total_nodes)}

	for i in range(total_nodes):
		smallest_deg = min(k for k in D if len(D[k]) > 0)
		vertex = D[smallest_deg].popleft()
		L.append(vertex)
		HL.add(vertex)

		for neighbor in graph.get_neighbors(vertex):
			
			if neighbor not in HL:
				neighbor_deg = current_degree[neighbor]
				current_degree[neighbor] -= 1
				D[neighbor_deg].remove(neighbor)
				if (neighbor_deg - 1) not in D:
					D[neighbor_deg - 1] = deque()
				D[neighbor_deg - 1].append(neighbor)
				Nv[neighbor].append(vertex)

	return [L, Nv]
				

def counting_triangles(graph: Graph):
	triangles = 0
	items = degen_ordering(graph)
	L = items[0]
	Nv = items[1]

	for vertex in L:
		earlier_neighbors = Nv[vertex]
		for i in range(len(earlier_neighbors)):
			for j in range(i+1, len(earlier_neighbors)):
				u = earlier_neighbors[i]
				w = earlier_neighbors[j]
				if graph.are_neighbors(u, w):
					triangles += 1

	return triangles

# get_clustering_coefficient(): return the graph's global clustering coefficient.
def get_clustering_coefficient(graph: Graph) -> float:

	total_nodes = graph.get_num_nodes()
	cluster_total = 0
	triangles = counting_triangles(graph)
	two_paths = 0

	for i in range(total_nodes):
		k = graph.get_num_neighbors(i)
		max_num_edges = (k * (k-1))/2
		two_paths += max_num_edges

	coeff = (3 * triangles) / two_paths

	return coeff


	'''
	for i in range(total_nodes):
		# k = number of neighbors of u 
		k = graph.get_num_neighbors(i)
		max_num_edges = (k * (k-1))/2
		
		print("~"*10)
		print(f"checking node {i}")
		print(f"k: {k}")
		print(f"max_num_edges: {max_num_edges}")
		
		
		actual_neighbor_edges = graph.count_edges_between_neighbors(i)
		#print(f"actual_neighbor_edges: {actual_neighbor_edges}")
		if max_num_edges == 0:
			cluster = 0.0
		else: 
			cluster = (triangles / max_num_edges)
		
		clusters[i] = cluster
		cluster_total += cluster			
	
	for key, values in clusters.items():
		print(key, ':', values)
	print("="*10)
	print(f"cluster_total: {cluster_total}")
	
	cluster_avg = round_down((cluster_total / total_nodes), 1)
	'''
	


# get_degree_distribution(): returns a dictionary representing the degree distribution of the graph.
#                            the keys are the degree, and the values is the number of nodes with that
#                            degree.

def get_degree_distribution(graph: Graph) -> dict[int, int]:
	return graph.degree_distribution_amount