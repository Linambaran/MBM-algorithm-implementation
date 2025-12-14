# Maximum Bipartite Matching (Project Match-X)

Repositori ini berisi implementasi dan benchmarking algoritma untuk menyelesaikan masalah **Maximum Bipartite Matching**.

**Mata Kuliah:** Desain dan Analisis Algoritma  
**Kelompok:** 2 - Linambaran Faradha Qisthas (L0224022)

## Algoritma
Membandingkan dua pendekatan:
1.  **Algo A (Baseline):** DFS Based (Kuhn's Algorithm) - Kompleksitas $O(V \cdot E)$.
2.  **Algo B (Optimized):** Hopcroft-Karp Algorithm - Kompleksitas $O(E \sqrt{V})$.

## Struktur Folder
```text
DAA_Instances/
├─ data/                  # Menyimpan file dataset (.json)
├─ run.py                 # Script utama untuk menjalankan benchmark
├─ generate_instances.py  # Script generator dataset graf random
└─ README.md              # Dokumentasi ini