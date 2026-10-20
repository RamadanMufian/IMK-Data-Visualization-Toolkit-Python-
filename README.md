# 🎨 IMK & Data Visualization Toolkit (Python)

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![WCAG Standard](https://img.shields.io/badge/accessibility-WCAG%202.x-green.svg)](https://www.w3.org/WAI/standards-guidelines/wcag/)
[![Heuristic](https://img.shields.io/badge/evaluation-10%20Nielsen%20Heuristics-orange.svg)](https://www.nngroup.com/articles/ten-usability-heuristics/)
[![SUS Benchmark](https://img.shields.io/badge/usability-SUS%20Score-purple.svg)](https://measuringu.com/sus/)

Toolkit komprehensif berbasis Python untuk mendukung praktisi, peneliti, dan pengembang dalam menerapkan prinsip-prinsip **Interaksi Manusia dan Komputer (IMK / HCI - *Human-Computer Interaction*)**, audit aksesibilitas desain antarmuka, pengujian kegunaan (*usability testing*), serta pembuatan **visualisasi data yang etis dan efektif**.

---

## 📋 Daftar Isi

1. [Fitur Utama](#-fitur-utama)
2. [Latar Belakang Teoretis](#-latar-belakang-teoretis)
3. [Struktur File](#-struktur-file)
4. [Instalasi & Prasyarat](#-instalasi--prasyarat)
5. [Cara Penggunaan](#-cara-penggunaan)
6. [Dokumentasi Modul & Fungsi](#-dokumentasi-modul--fungsi)
   - [1. Cek Kontras Warna (WCAG 2.x)](#1-cek-kontras-warna-wcag-2x)
   - [2. Evaluasi Heuristik Nielsen](#2-evaluasi-heuristik-nielsen)
   - [3. Usability Testing & Skor SUS](#3-usability-testing--skor-sus)
   - [4. Pemilih Jenis Grafik (Chart Chooser)](#4-pemilih-jenis-grafik-chart-chooser)
   - [5. Visualisasi Data Jujur vs Menyesatkan](#5-visualisasi-data-jujur-vs-menyesatkan)
7. [Hasil Eksekusi & Interpretasi](#-hasil-eksekusi--interpretasi)
8. [Panduan Kustomisasi Data](#-panduan-kustomisasi-data)
9. [Referensi Standar](#-referensi-standar)

---

## 🌟 Fitur Utama

Toolkit ini mengintegrasikan 5 pilar fundamental IMK & visualisasi informasi dalam satu file terpadu ([imk_toolkit.py](file:///c:/Users/ASUS/Downloads/IMK/imk_toolkit.py)):

* 🔍 **Audit Aksesibilitas Kontras Warna (WCAG 2.x)**: Menghitung rasio kontras luminansi relatif antara *foreground* (teks) dan *background* untuk memastikan keterbacaan sesuai level kepatuhan AA/AAA.
* 📋 **Agregasi Evaluasi Heuristik Nielsen**: Memproses penilaian multipel evaluator terhadap 10 heuristik Jakob Nielsen, menghitung rata-rata *severity rating* (0–4), mengklasifikasikan prioritas perbaikan, dan merangkum temuan kritis.
* ⏱️ **Analisis Kuantitatif Usability Testing & Skor SUS**: Menghitung metrik keberhasilan tugas (*success rate*), durasi pengerjaan (median waktu), frekuensi error, serta kalkulasi otomatis skor *System Usability Scale* (SUS) berbobot 0–100.
* 📊 **Rekomendasi Pemilihan Grafik Tepat Sasaran**: Mesin inferensi sederhana untuk menentukan jenis visualisasi optimal (*bar*, *line*, *scatter*, *pie*) berdasarkan sasaran analisis.
* 📉 **Generasi Grafik Etis & Deteksi Anomali**: Mendemonstrasikan perbedaan grafik batang menyesatkan (*truncated axis*) vs jujur (*baseline zero*), penerapan *data-ink ratio* Edward Tufte, serta penggunaan atribut visual pra-atentif (*pre-attentive attributes*) untuk menyorot anomali secara instan.

---

## 🧠 Latar Belakang Teoretis

| Komponen | Standar / Tokoh | Penjelasan & Formula |
| :--- | :--- | :--- |
| **Kontras Warna** | **W3C WCAG 2.1** | Formula Luminansi Relatif $L = 0.2126R + 0.7152G + 0.0722B$. Rasio: $\frac{L_1 + 0.05}{L_2 + 0.05}$. Ambang: Teks normal $\ge 4.5:1$, Teks besar/komponen $\ge 3:1$. |
| **Heuristik Usability** | **Jakob Nielsen (NN/g)** | 10 aturan praktis desain antarmuka. Evaluasi ideal dengan 3–5 evaluator independen untuk menemukan $\approx 75\text{--}80\%$ masalah *usability*. Skala *severity*: 0 (Bukan masalah) s.d. 4 (Katastrofik). |
| **Skor SUS** | **John Brooke (1986)** | Kuisioner 10 butir pertanyaan skala Likert 1–5. Soal ganjil ($X = \text{skor} - 1$), soal genap ($X = 5 - \text{skor}$). Total skor dikalikan $2.5$. Benchmark industri rata-rata: **68**. |
| **Visualisasi Etis** | **Edward Tufte** | Memaksimalkan *Data-Ink Ratio* (menghapus *chartjunk*, garis batas dan grid berlebih). Batang komparasi wajib dimulai dari sumbu $0$ agar representasi area visual sebanding dengan nilai riil. |

---

## 📁 Struktur File

```text
IMK/
├── imk_toolkit.py      # Kode utama (5 modul fungsi evaluasi, analisis & visualisasi)
├── hasil_imk.png       # Grafik keluaran Matplotlib perbandingan jujur vs menyesatkan
└── README.md           # Dokumentasi teknis proyek
```

---

## 💻 Instalasi & Prasyarat

### Prasyarat
- Python 3.8 atau versi yang lebih baru.
- Manajer paket `pip`.

### Dependensi Pihak Ketiga
Toolkit ini menggunakan pustaka standar Python (`statistics`) dan pustaka komputasi/grafis berikut:

```bash
pip install numpy matplotlib
```

---

## 🚀 Cara Penggunaan

Cukup jalankan script utama dari terminal / Command Prompt / PowerShell:

```bash
python imk_toolkit.py
```

Setelah dijalankan, program akan:
1. Menampilkan laporan teks audit WCAG di terminal.
2. Menampilkan tabel evaluasi heuristik dan prioritas perbaikan.
3. Mencetak matriks usability testing dan skor SUS.
4. Menampilkan rekomendasi jenis grafik.
5. Menghasilkan dan menyimpan gambar grafik visualisasi ke file [hasil_imk.png](file:///c:/Users/ASUS/Downloads/IMK/hasil_imk.png).

---

## 📖 Dokumentasi Modul & Fungsi

### 1. Cek Kontras Warna (WCAG 2.x)

Modul ini mengonversi kode warna heksadesimal ke representasi RGB linier, menghitung luminansi relatif sRGB, dan menguji rasio kontras terhadap standar WCAG.

* **Fungsi:** `cek_kontras(pasangan)`
* **Parameter:** `pasangan` — daftar *tuple* berformat `(nama_komponen, hex_foreground, hex_background)`.
* **Kriteria Kelulusan:**
  - Teks Normal: Rasio $\ge 4.5:1$
  - Teks Besar / Komponen UI Interaktif: Rasio $\ge 3.0:1$

```python
cek_kontras([
    ("Teks utama dasbor", "#17202f", "#ffffff"),
    ("Tombol aktif", "#f3f5f8", "#0b6e6e"),
    ("Abu muda di atas putih", "#b0b7c3", "#ffffff")
])
```

---

### 2. Evaluasi Heuristik Nielsen

Mengumpulkan umpan balik dari para evaluator berdasarkan 10 Heuristik Usability Nielsen:
1. *Visibilitas status sistem*
2. *Kesesuaian sistem dengan dunia nyata*
3. *Kontrol dan kebebasan pengguna*
4. *Konsistensi dan standar*
5. *Pencegahan kesalahan*
6. *Pengenalan dibanding mengingat*
7. *Fleksibilitas dan efisiensi*
8. *Desain estetik dan minimalis*
9. *Bantu pengguna pulih dari kesalahan*
10. *Bantuan dan dokumentasi*

* **Fungsi:** `evaluasi_heuristik(penilaian)`
* **Skala Severity Rating:**
  - `0`: Bukan masalah usability
  - `1`: Masalah kosmetik (perbaikan opsional)
  - `2`: Masalah minor (prioritas rendah)
  - `3`: Masalah mayor (prioritas tinggi / terjadwal)
  - `4`: Masalah katastrofik / kritis (wajib diperbaiki **SEGERA** sebelum rilis)
* **Logika Prioritas Otomatis:**
  - Rata-rata $\ge 3.0$: `SEGERA`
  - $2.0 \le \text{Rata-rata} < 3.0$: `Terjadwal`
  - $0.0 < \text{Rata-rata} < 2.0$: `Rendah`

---

### 3. Usability Testing & Skor SUS

Menganalisis performa empiris pengguna saat menyelesaikan tugas pengujian (*task-based usability test*) dan mengukur persepsi kemudahan penggunaan melalui System Usability Scale (SUS).

* **Fungsi 1:** `skor_sus(jawaban)`
  - Parameter: `list` berisi 10 nilai integer (skala 1–5).
  - Mengonversi jawaban kuesioner menjadi skala standar 0–100.
* **Fungsi 2:** `analisis_usability(sesi, sus_responden)`
  - Metrik yang dihitung:
    - **Success Rate per Task & Keseluruhan**: Persentase peserta yang berhasil menyelesaikan misi.
    - **Median Waktu (detik)**: Median durasi penyelesaian tugas (tahan terhadap *outlier* dibanding rata-rata).
    - **Rata-rata Error per Peserta**: Rata-rata kesalahan yang dilakukan pengguna pada tiap tugas.
    - **Interpretasi SUS**: Skor $\ge 68$ dikategorikan **di atas rata-rata**; skor $< 68$ memerlukan investigasi perbaikan.

---

### 4. Pemilih Jenis Grafik (Chart Chooser)

Menghindari kesalahan penyajian informasi dengan merekomendasikan jenis visualisasi berdasarkan intensi analisis data.

* **Fungsi:** `pilih_grafik(tujuan)`
* **Daftar Kategori yang Didukung:**
  - `"tren"` $\rightarrow$ **Line Chart** (melihat dinamika & fluktuasi data antar waktu).
  - `"bandingkan"` $\rightarrow$ **Bar Chart** (membandingkan magnitudo antar kategori/grup diskrit).
  - `"korelasi"` $\rightarrow$ **Scatter Plot** (mengidentifikasi keterkaitan/sebaran antara 2 variabel numerik kontinu).
  - `"proporsi"` $\rightarrow$ **Pie / Donut Chart** (komposisi bagian dari 100%, idealnya $\le 5$ segmen).

---

### 5. Visualisasi Data Jujur vs Menyesatkan

Fungsi `buat_grafik(nama_file="hasil_imk.png")` menghasilkan perbandingan visual 3 panel:

1. **Panel Kiri (Grafik Menyesatkan - Truncated Y-Axis):**
   - Menampilkan perbandingan dua nilai yang selisihnya sangat kecil (Produk A = 97 vs Produk B = 100), namun batas bawah sumbu Y dipotong di angka `96`.
   - *Dampak buruk:* Menciptakan ilusi optik bahwa Produk B memiliki nilai 4–5 kali lipat lebih unggul dari Produk A.
2. **Panel Tengah (Grafik Jujur - Zero Baseline):**
   - Menampilkan data yang sama persis, tetapi sumbu Y dimulai dari `0` dan dilengkapi label nilai langsung (*direct data labels*).
   - *Dampak baik:* Pembaca langsung memahami bahwa perbedaan kedua produk tersebut sebenarnya sangat tipis.
3. **Panel Kanan (Deteksi Anomali & Atribut Pra-atentif):**
   - Visualisasi tren 12 bulan menggunakan *Line Chart*.
   - Menerapkan uji statistik Z-Score ($|z| > 2.5$). Titik anomali (outlier) ditandai dengan warna merah terang kontras (*pre-attentive visual attribute*), sedangkan tren normal diberi warna netral redup agar tidak mendistraksi pembaca.
   - Mengeliminasi *chartjunk* (bingkai atas dan kanan dihilangkan, grid lembut hanya pada sumbu Y).

---

## 📊 Hasil Eksekusi & Interpretasi

### Contoh Output Terminal

```text
=== 1. CEK KONTRAS WARNA (WCAG) ===
Keterangan                  Teks     Latar     Rasio  Teks normal  Teks besar/UI
Teks utama dasbor           #17202f  #ffffff   14.65  LULUS        LULUS
Teks sekunder               #4f5b70  #ffffff    5.75  LULUS        LULUS
Tombol aktif (teks terang)  #f3f5f8  #0b6e6e    4.96  LULUS        LULUS
Abu muda di atas putih      #b0b7c3  #ffffff    1.95  GAGAL        GAGAL
Teks merah anomali          #b3261e  #ffffff    6.30  LULUS        LULUS

=== 2. EVALUASI HEURISTIK NIELSEN ===
Jumlah evaluator: 3 (Nielsen menyarankan 3-5 agar mayoritas masalah ditemukan)
#  Heuristik                               Rata-rata  Dinilai  Prioritas
5  Pencegahan kesalahan                          3.7     3/3  SEGERA
1  Visibilitas status sistem                     2.7     3/3  Terjadwal
9  Bantu pengguna pulih dari kesalahan           2.7     3/3  Terjadwal
3  Kontrol dan kebebasan pengguna                2.5     2/3  Terjadwal
4  Konsistensi dan standar                       1.0     1/3  Rendah
8  Desain estetik dan minimalis                  1.0     1/3  Rendah
10 Bantuan dan dokumentasi                       1.0     1/3  Rendah

Catatan temuan untuk prioritas tertinggi:
  - H5 Pencegahan kesalahan: Hapus data tanpa konfirmasi; Form bisa dikirim kosong; Tidak ada konfirmasi hapus
  - H1 Visibilitas status sistem: Tidak ada indikator loading saat filter; Status simpan tidak jelas; Proses lambat tanpa umpan balik
  - H9 Bantu pengguna pulih dari kesalahan: Pesan 'Error 400' tanpa solusi; Pesan error teknis; Pesan error kurang jelas

=== 3. ANALISIS USABILITY TESTING ===
Tugas                         Sukses  Median waktu  Error/peserta
Filter wilayah Jakarta           75%          10 dt           1.0
Temukan anomali                  75%          22 dt           0.8

Success rate keseluruhan: 75%
Skor SUS: 75.6 dari 4 responden -> di atas rata-rata (>=68)

=== 4. PEMILIH GRAFIK ===
  tren        -> line chart (perubahan dari waktu ke waktu)
  bandingkan  -> bar chart (membandingkan antar kategori)
  korelasi    -> scatter plot (hubungan dua variabel numerik)
  proporsi    -> pie/donut chart (bagian dari keseluruhan (maksimal sekitar 5 bagian))

=== 5. GRAFIK === tersimpan: hasil_imk.png (anomali terdeteksi di bulan [8])
```

---

## 🛠️ Panduan Kustomisasi Data

Anda dapat menyesuaikan data uji coba di bagian blok `if __name__ == "__main__":` pada file [imk_toolkit.py](file:///c:/Users/ASUS/Downloads/IMK/imk_toolkit.py):

### Mengubah Data Evaluasi Heuristik
Format penilaian adalah *dictionary* per nama evaluator, dengan kunci nomor heuristik (1–10) dan nilai berupa pasangan `(skor_severity, "catatan_kualitatif")`:
```python
penilaian_baru = {
    "Evaluator A": {
        1: (3, "Tidak ada progress bar saat upload berkas"),
        5: (4, "Tombol hapus akun tidak meminta konfirmasi sandi")
    },
    "Evaluator B": {
        1: (3, "Layar blank putih saat memuat data besar"),
        2: (1, "Istilah teknis database ditampilkan di UI pengguna")
    }
}
evaluasi_heuristik(penilaian_baru)
```

### Mengubah Data Usability Testing
```python
sesi_baru = [
    {"tugas": "Checkout Produk", "berhasil": True, "detik": 45, "error": 0},
    {"tugas": "Checkout Produk", "berhasil": False, "detik": 120, "error": 4},
]
# Kuesioner SUS: 10 pertanyaan skala 1-5 per peserta
sus_baru = [
    [5, 1, 4, 1, 5, 2, 4, 1, 5, 1], # Peserta 1 (sangat positif)
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3], # Peserta 2 (netral)
]
analisis_usability(sesi_baru, sus_baru)
```

---

## 📚 Referensi Standar

1. **W3C Web Accessibility Initiative (WAI)**: *Web Content Accessibility Guidelines (WCAG) 2.1 Contrast Minimum (Level AA)* — [W3C Understanding WCAG 2.1](https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html)
2. **Nielsen Norman Group**: *10 Usability Heuristics for User Interface Design* oleh Jakob Nielsen — [NNGroup Heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/)
3. **MeasuringU**: *Measuring Usability with the System Usability Scale (SUS)* oleh Jeff Sauro, PhD — [MeasuringU SUS](https://measuringu.com/sus/)
4. **The Visual Display of Quantitative Information**: Edward R. Tufte (Prinsip *Data-Ink Ratio* dan kejujuran visual).
5. **Colin Ware**: *Information Visualization: Perception for Design* (Teori persepsi dan atribut pra-atentif).

---

*Dibuat untuk keperluan evaluasi, edukasi, dan standarisasi riset Interaksi Manusia dan Komputer (IMK).*
