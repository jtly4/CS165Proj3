# explanations for member functions are provided in requirements.py
# each file that uses a graph should import it from this file.

# Explanations for Graph public member functions
#
# init(): initialize the graph a given number of nodes and given edges.
#         edges are represented as tuples (u, v), where each edge is between node with index u and
#         node with index v.
#         the autograder will never add duplicate edges to the graph.
# get_num_nodes(): returns the number of nodes in the graph.
# get_num_edges(): returns the number of edges in the graph.
# get_neighbors(): given a node index, return an iterable type over the collection of its neighbors.
#                  the iterable type can be a list, set, generator, etc.
#                  each neighbor should appear exactly once.

from collections.abc import Iterable

class Graph:
	def __init__(self, num_nodes: int, edges: Iterable[tuple[int, int]]):
		self.num_nodes = num_nodes
		# pick data structure (adjacency set, or dictionary[int, set[int]])
		# implement how to set up edges being added 
		self.edges = edges
		self.neighbors = {}
		self._set_neighbors(edges)

	def get_num_nodes(self) -> int:
		return self.num_nodes

	def get_num_edges(self) -> int:
		return len(self.edges)
	
	def _set_nodes(self):
		pass
	
	def _set_neighbors(self, edges):
		if not edges:
			self.neighbors = {}
			return
			#if self.get_num_nodes > 0:
			#	self._set_nodes()

		for edge in self.edges:
			node1 = edge[0]
			node2 = edge[1]
			if node1 not in self.neighbors:
				self.neighbors[node1] = set()
			if node2 not in self.neighbors:
				self.neighbors[node2] = set()
			
			self.neighbors[node1].add(node2)
			self.neighbors[node2].add(node1)		

	def get_neighbors(self, node: int) -> Iterable[int]:
		if node not in self.neighbors:
			return {}
		
		else:
			return self.neighbors[node]
		
	def are_neighbors(self, node1: int, node2: int) -> bool:		
		neighbors1 = self.get_neighbors(node1)
		
		if node2 in neighbors1:
			return True
		else:
			return False
		
	def count_edges_between_neighbors(self, node):
		neighbors_to_check = self.get_neighbors(node)
		#print(f"neighbors of {node}: {neighbors_to_check}")
		#print("-"*10)
		count = 0
		for neighbor in neighbors_to_check:
			neighbor_of_neighbor = self.get_neighbors(neighbor)
			intersection = neighbors_to_check & neighbor_of_neighbor
			#print(f"neighbors of {neighbor}: {neighbor_of_neighbor}")
			#print(f"intersection of {node} and {neighbor}: {intersection}")
			count += len(intersection)

		count = count/2

		return count
		
	def get_num_neighbors(self, node:int) -> int:
		return len(self.get_neighbors(node))


	# feel free to define new methods in addition to the above
	# fill in the definitions of each required member function (above),
	# and for any additional member functions you define
