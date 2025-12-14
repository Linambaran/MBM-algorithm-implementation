import json
import random
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / 'data'
DATA_DIR.mkdir(parents=True, exist_ok=True)

def generate_bipartite_graph(n_u, n_v, density, seed):
    random.seed(seed)
    adj = [[] for _ in range(n_u)]
    edge_count = 0
    
    for u in range(n_u):
        for v in range(n_v):
            if random.random() < density:
                adj[u].append(v)
                edge_count += 1
                
    return {
        "project": "matching",
        "description": f"Random Bipartite Graph U={n_u}, V={n_v}, Density={density}",
        "meta": {
            "U": n_u, 
            "V": n_v, 
            "density": density,
            "seed": seed,
            "total_edges": edge_count
        },
        "adj": adj
    }

def main():
    print(f"Generating instances in: {DATA_DIR}")
    
    for i in range(1, 16):
        n_size = i * 100
        
        dens = 0.05 if i % 2 != 0 else 0.2
        
        filename = f"matching_G{i:02d}_N{n_size}.json"
        
        data = generate_bipartite_graph(
            n_u=n_size, 
            n_v=n_size, 
            density=dens, 
            seed=42 + i
        )
        
        output_path = DATA_DIR / filename
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
            
        print(f"[OK] {filename} (Edges: {data['meta']['total_edges']})")

    print("\nSelesai! Jalankan 'python run.py --instance data/matching_G01_N100.json' untuk test.")

if __name__ == '__main__':
    main()