import sys

def solve():
    # Fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    it = iter(input_data)
    t_str = next(it, None)
    if t_str is None: return
    t = int(t_str)
    MOD = 10**9 + 7

    for _ in range(t):
        n = int(next(it))
        adj = [[] for _ in range(n + 1)]
        
        # Only build the graph with type 1 edges
        for _ in range(n - 1):
            u, v = int(next(it)), int(next(it))
            etype, evalue = int(next(it)), int(next(it))
            if etype == 1:
                adj[u].append((v, evalue))
                adj[v].append((u, evalue))

        visited = [False] * (n + 1)
        total_ans = 0

        for i in range(1, n + 1):
            # Process each connected component formed by type 1 edges
            if not visited[i]:
                component_nodes = []
                stack = [i]
                visited[i] = True
                
                # Step 1: Find all nodes in this component
                while stack:
                    u = stack.pop()
                    component_nodes.append(u)
                    for v, w in adj[u]:
                        if not visited[v]:
                            visited[v] = True
                            stack.append(v)
                
                s = len(component_nodes)
                if s < 2: continue # No pairs possible in a single-node component
                
                # Step 2: Iterative Post-order traversal to calculate subtree sizes
                order = []
                parent = {node: -1 for node in component_nodes}
                edge_weight = {node: 0 for node in component_nodes}
                bfs_stack = [component_nodes[0]]
                visited_in_comp = {node: False for node in component_nodes}
                visited_in_comp[component_nodes[0]] = True
                
                while bfs_stack:
                    u = bfs_stack.pop()
                    order.append(u)
                    for v, w in adj[u]:
                        if not visited_in_comp[v]:
                            visited_in_comp[v] = True
                            parent[v] = u
                            edge_weight[v] = w
                            bfs_stack.append(v)
                
                subtree_size = {node: 1 for node in component_nodes}
                # Process nodes bottom-up
                for u in reversed(order):
                    p = parent[u]
                    if p != -1:
                        w = edge_weight[u]
                        n1 = subtree_size[u]
                        n2 = s - n1
                        # Edge contribution to unordered pairs: weight * (size_left * size_right)
                        contribution = (w * n1 * n2) % MOD
                        total_ans = (total_ans + contribution) % MOD
                        subtree_size[p] += n1

        sys.stdout.write(str(total_ans) + "\n")

if __name__ == "__main__":
    solve()
