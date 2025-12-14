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

## How to EXECUTE!
1. Git clone/download as ZIP lalu extract terlebih dahulu repo ini.
2. Buka terminal di direktori repo ini, jalankan command **python generate_instances.py** jika folder data belum ada (bisa diabaikan karena repo ini sudah terdapat contoh dataset yang telah di-generate).
3. Untuk benchmark **Algo A/DFS**, jalankan command **python run.py --instance data/matching_G01_N100.json --algo A**.
4. Untuk benchmark **Algo B/HK**, jalankan command **python run.py --instance data/matching_G01_N100.json --algo B**.
5. Command **python demo_validation.py** hanya untuk keperluan membandingkan output, yang mana seharusnya tidak akan ada perbedaan (kecuali terdapat bug).

## Output
<img width="643" height="538" alt="image" src="https://github.com/user-attachments/assets/a4df23c9-31bb-4305-b18c-ded7680579f8" />
