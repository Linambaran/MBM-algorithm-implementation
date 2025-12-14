import json
import argparse
import sys
from run import algo_A, algo_B

def main():
    p = argparse.ArgumentParser(description="Demo Validasi Output untuk Laporan")
    p.add_argument('--instance', required=True, help='Path ke file JSON')
    args = p.parse_args()

    try:
        with open(args.instance, 'r') as f:
            inst = json.load(f)
    except FileNotFoundError:
        print("File tidak ditemukan.")
        sys.exit(1)

    project = inst.get("project", "matching")

    print("--- Hasil Eksekusi ---")

    res_a = algo_A(inst, project)
    print(f"Algorithm A (DFS Kuhn) Result: {res_a}")

    res_b = algo_B(inst, project)
    print(f"Algorithm B (Hopcroft-Karp) Result: {res_b}")

    if res_a == res_b:
        print("Status: MATCH (Valid)")
    else:
        print(f"Status: MISMATCH (Diff: {abs(res_a - res_b)})")

if __name__ == '__main__':
    main()