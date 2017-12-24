"""
Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.
"""
# Definition for a undirected graph node


class UndirectedGraphNode:

    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution:
    """
    难点在于对象的传递，必须保存好新生成的点，所以采用字典来保存新生成的复制点
    """
    # @param node, a undirected graph node
    # @return a undirected graph node
    # BFS
    def cloneGraph(self, node):
        if not node:
            return
        node_copy = UndirectedGraphNode(node.label)
        dic = {node: node_copy}
        queue = [node]
        while queue:
            node = queue.pop()
            for neighbor in node.neighbors:
                if neighbor not in dic:
                    neighborCopy = UndirectedGraphNode(neighbor.label)
                    dic[neighbor] = neighborCopy
                    dic[node].neighbors.append(neighborCopy)
                    queue.append(neighbor)
                else:
                    dic[node].neighbors.append(dic[neighbor])
        return node_copy


node0 = UndirectedGraphNode(0)
node1 = UndirectedGraphNode(1)
node2 = UndirectedGraphNode(2)
node0.neighbors.append(node1)
node1.neighbors.append(node0)
node1.neighbors.append(node2)
node2.neighbors.append(node1)
node2.neighbors.append(node2)
solution = Solution()
solution.cloneGraph(node0)