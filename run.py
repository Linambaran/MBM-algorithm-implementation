import json
import argparse
import time
import sys
from collections import deque
from typing import Any

def algo_A(instance: Any, project: str) -> int: # DFS: O(V * E)
    if project != "matching":
        raise NotImplementedError(f"Algo A tidak mendukung project: {project}")

    adj = instance['adj']
    n_left = instance['meta']['U']
    n_right = instance['meta']['V']
    
    match_right = [-1] * n_right
    
    def dfs(u, visited):
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                if match_right[v] < 0 or dfs(match_right[v], visited):
                    match_right[v] = u
                    return True
        return False

    matching_size = 0
    for u in range(n_left):
        visited = [False] * n_right
        if dfs(u, visited):
            matching_size += 1
            
    return matching_size

def algo_B(instance: Any, project: str) -> int: # Hopcroft-Karp: O(E * sqrt(V))
    if project != "matching":
        raise NotImplementedError(f"Algo B tidak mendukung project: {project}")

    adj = instance['adj']
    n_left = instance['meta']['U']
    n_right = instance['meta']['V']
    
    pair_u = [-1] * n_left
    pair_v = [-1] * n_right
    dist = {}
    NIL = -1
    INF = float('inf')

    def bfs():
        queue = deque()
        for u in range(n_left):
            if pair_u[u] == NIL:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = INF
        dist[NIL] = INF
        
        while queue:
            u = queue.popleft()
            if dist[u] < dist[NIL]:
                for v in adj[u]:
                    if dist[pair_v[v]] == INF:
                        dist[pair_v[v]] = dist[u] + 1
                        queue.append(pair_v[v])
        return dist[NIL] != INF

    def dfs(u):
        if u != NIL:
            for v in adj[u]:
                if dist[pair_v[v]] == dist[u] + 1:
                    if dfs(pair_v[v]):
                        pair_v[v] = u
                        pair_u[u] = v
                        return True
            dist[u] = INF
            return False
        return True

    matching_size = 0
    while bfs():
        for u in range(n_left):
            if pair_u[u] == NIL:
                if dfs(u):
                    matching_size += 1
    return matching_size

def evaluate(instance: Any, result: int, project: str) -> float:
    return 0.0

def main():
    p = argparse.ArgumentParser(description="Benchmarking Maximum Bipartite Matching")
    p.add_argument('--instance', required=True, help='Path ke file JSON (contoh: data/matching_G01.json)')
    p.add_argument('--algo', choices=['A', 'B'], default='A', help='Pilih algoritma: A (DFS) atau B (Hopcroft-Karp)')
    args = p.parse_args()

    try:
        with open(args.instance, 'r', encoding='utf-8') as f:
            inst = json.load(f)
    except FileNotFoundError:
        print(f"Error: File '{args.instance}' tidak ditemukan.")
        sys.exit(1)

    project = inst.get("project", "unknown")
    print(f"Loading instance: {args.instance} (Project: {project})")

    t0 = time.perf_counter()
    if args.algo == 'A':
        result = algo_A(inst, project)
        algo_name = "DFS Kuhn"
    else:
        result = algo_B(inst, project)
        algo_name = "Hopcroft-Karp"
    dt = (time.perf_counter() - t0) * 1000.0

    gap = evaluate(inst, result, project)

    print("-" * 50)
    print(f"Algorithm  : {algo_name}")
    print(f"Result     : {result} pairs")
    print(f"Time       : {dt:.4f} ms")
    print(f"Gap        : {gap:.4f}")
    print("-" * 50)

if __name__ == '__main__':
    main()