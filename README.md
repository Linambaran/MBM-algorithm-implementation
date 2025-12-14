# Maximum Bipartite Matching (Project Match-X)

Repositori ini berisi implementasi dan benchmarking algoritma untuk menyelesaikan masalah **Maximum Bipartite Matching**.

**Mata Kuliah:** Desain dan Analisis Algoritma  
**Kelompok:** 2 - Linambaran Faradha Qisthas (L0224022)

## Algorithm
Membandingkan dua pendekatan:
1.  **Algo A (Baseline):** DFS Based (Kuhn's Algorithm) - Kompleksitas $O(V \cdot E)$.
2.  **Algo B (Optimized):** Hopcroft-Karp Algorithm - Kompleksitas $O(E \sqrt{V})$.

## Folder Structure
```text
DAA_Instances/
├─ data/                  # Menyimpan file dataset (.json)
├─ run.py                 # Script utama untuk menjalankan benchmark
├─ generate_instances.py  # Script generator dataset graf random
├─ README.md              # Dokumentasi
└─ demo_validation.py     # Output ringkas dan dapat digunakan untuk membandingkan kedua algoritma
```

## How to EXECUTE!
### Clone/Download ZIP Repository
   ```bash
   git clone https://github.com/Linambaran/MBM-algorithm-implementation
   ```
   Note: Setelah git clone/extract, buka terminal dan arahkan ke direktori dimana repositori ini disimpan.
   
### Generate Instances
  ```bash
  python generate_instances.py
  ```
  Note: Di dalam repo ini, terdapat folder **'data'** yang berisi pre-generated instances juga. Jadi, tahapan ini adalah **opsional**.

### Benchmarking Algorithm A (DFS)
  ```bash
   python run.py --instance data/matching_Gxx_Nxx.json --algo A
  ```

### Benchmarking Algorithm B (Hopcroft-Karp)
  ```bash
   python run.py --instance data/matching_Gxx_Nxx.json --algo B
  ```

### Output Comparison Between Them
```bash 
python demo_validation.py --instance data/matching_Gxx_Nxx.json
```

## Output
```bash
-> python run.py --instance data/matching_G10_N1000.json --algo A
Loading instance: data/matching_G10_N1000.json (Project: matching)
--------------------------------------------------
Algorithm  : DFS Kuhn
Result     : 1000 pairs
Time       : 1127.4417 ms
Gap        : 0.0000
--------------------------------------------------

-> python run.py --instance data/matching_G10_N1000.json --algo B
Loading instance: data/matching_G10_N1000.json (Project: matching)
--------------------------------------------------
Algorithm  : Hopcroft-Karp
Result     : 1000 pairs
Time       : 52.0293 ms
Gap        : 0.0000
--------------------------------------------------

-> python demo_validation.py --instance data/matching_G10_N1000.json
--- Hasil Eksekusi ---
Algorithm A (DFS Kuhn) Result: 1000
Algorithm B (Hopcroft-Karp) Result: 1000
Status: MATCH (Valid)
```

![marisa&#39;s-butt-touhou](https://github.com/user-attachments/assets/796db778-b7eb-4363-9cdc-506361a8931b)


