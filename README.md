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
├─ README.md              # Dokumentasi
└─ demo_validation.py     # Output ringkas dan dapat digunakan untuk membandingkan kedua algoritma
```

# How to EXECUTE!
**- Git clone/download as ZIP lalu extract terlebih dahulu repo ini**
   ```bash
   git clone https://github.com/Linambaran/MBM-algorithm-implementation
   ```
**- Buka terminal di direktori repo ini, lalu jalankan:**
  ```bash
  python generate_instances.py
  ```
  Note: Di dalam repo ini, terdapat folder **'data'** yang berisi pre-generated instances juga. Jadi, tahapan ini adalah **opsional**

**- Untuk benchmark Algo A/DFS, jalankan command:**
  ```bash
   python run.py --instance data/matching_Gxx_Nxx.json --algo A
  ```
**- Untuk benchmark Algo B/HK, jalankan command:**
  ```bash
   python run.py --instance data/matching_Gxx_Nxx.json --algo B
  ```
**- Jalankan command berikut untuk membandingkan output kedua algoritma**
```bash 
python demo_validation.py --instance data/matching_Gxx_Nxx.json
```

## Output
<p align="center" width="100%">
  <img width="650" height="480" alt="screenshot-2025-12-14_17 37 25" src="https://github.com/user-attachments/assets/004f9be4-778a-4ff7-a03e-0ad18ead7778" />
</p>

