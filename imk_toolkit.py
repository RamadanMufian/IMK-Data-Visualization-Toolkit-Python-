"""
Toolkit IMK & Visualisasi Data (Python)
Berdasarkan Sesi: Human-Computer Interaction and Data Visualization

Isi:
  1. Cek kontras warna WCAG          (aksesibilitas: "perceivable")
  2. Evaluasi heuristik Nielsen      (10 heuristik, severity 0-4, banyak evaluator)
  3. Analisis usability testing      (success rate, waktu, error) + skor SUS
  4. Pemilih jenis grafik            (line / bar / scatter / pie sesuai tujuan)
  5. Grafik menyesatkan vs jujur     (sumbu terpotong vs mulai dari 0) + highlight anomali

Jalankan:
  pip install numpy matplotlib
  python imk_toolkit.py
Semua data di bawah adalah CONTOH. Ganti dengan data evaluasi/pengujian Anda sendiri.
"""
import statistics as st

import matplotlib
import numpy as np

matplotlib.use("Agg")
import matplotlib.pyplot as plt


# ======================================================================
# 1. KONTRAS WARNA (WCAG 2.x)
#    Teks normal minimal 4.5:1, teks besar dan komponen UI minimal 3:1.
# ======================================================================
def _linear(c):
    c /= 255
    return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4


def luminansi(hex_warna):
    h = hex_warna.lstrip("#")
    r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    return 0.2126 * _linear(r) + 0.7152 * _linear(g) + 0.0722 * _linear(b)


def rasio_kontras(fg, bg):
    terang, gelap = sorted((luminansi(fg), luminansi(bg)), reverse=True)
    return (terang + 0.05) / (gelap + 0.05)


def cek_kontras(pasangan):
    print("=== 1. CEK KONTRAS WARNA (WCAG) ===")
    print(f"{'Keterangan':<28}{'Teks':<9}{'Latar':<9}{'Rasio':>7}  Teks normal  Teks besar/UI")
    for nama, fg, bg in pasangan:
        r = rasio_kontras(fg, bg)
        print(f"{nama:<28}{fg:<9}{bg:<9}{r:>6.2f}  {'LULUS' if r >= 4.5 else 'GAGAL':<11}  "
              f"{'LULUS' if r >= 3 else 'GAGAL'}")
    print()


# ======================================================================
# 2. EVALUASI HEURISTIK NIELSEN
#    Severity: 0 bukan masalah, 1 kosmetik, 2 minor, 3 mayor, 4 katastrofik
# ======================================================================
HEURISTIK = [
    "Visibilitas status sistem", "Kesesuaian sistem dengan dunia nyata",
    "Kontrol dan kebebasan pengguna", "Konsistensi dan standar",
    "Pencegahan kesalahan", "Pengenalan dibanding mengingat",
    "Fleksibilitas dan efisiensi", "Desain estetik dan minimalis",
    "Bantu pengguna pulih dari kesalahan", "Bantuan dan dokumentasi",
]


def evaluasi_heuristik(penilaian):
    """penilaian: {evaluator: {nomor_heuristik(1-10): (severity, catatan)}}"""
    print("=== 2. EVALUASI HEURISTIK NIELSEN ===")
    n_eval = len(penilaian)
    hasil = []
    for no in range(1, 11):
        skor = [p[no][0] for p in penilaian.values() if no in p]
        catatan = [p[no][1] for p in penilaian.values() if no in p and p[no][1]]
        rata = st.mean(skor) if skor else 0.0
        hasil.append((no, rata, len(skor), catatan))
    hasil.sort(key=lambda x: x[1], reverse=True)

    print(f"Jumlah evaluator: {n_eval} (Nielsen menyarankan 3-5 agar mayoritas masalah ditemukan)")
    print(f"{'#':<3}{'Heuristik':<40}{'Rata-rata':>10}{'Dinilai':>9}  Prioritas")
    for no, rata, n, _ in hasil:
        prio = "SEGERA" if rata >= 3 else "Terjadwal" if rata >= 2 else "Rendah" if rata > 0 else "-"
        print(f"{no:<3}{HEURISTIK[no - 1]:<40}{rata:>10.1f}{n:>6}/{n_eval}  {prio}")
    print("\nCatatan temuan untuk prioritas tertinggi:")
    for no, rata, _, catatan in hasil[:3]:
        if rata > 0:
            print(f"  - H{no} {HEURISTIK[no - 1]}: " + "; ".join(catatan))
    print()


# ======================================================================
# 3. USABILITY TESTING + SUS
# ======================================================================
def skor_sus(jawaban):
    """10 jawaban skala 1-5. Item ganjil (positif): nilai-1. Item genap (negatif): 5-nilai. Total x 2,5."""
    assert len(jawaban) == 10 and all(1 <= j <= 5 for j in jawaban), "SUS butuh 10 jawaban skala 1-5"
    total = sum((j - 1) if i % 2 == 0 else (5 - j) for i, j in enumerate(jawaban))
    return total * 2.5


def analisis_usability(sesi, sus_responden):
    """sesi: list dict {tugas, berhasil, detik, error}"""
    print("=== 3. ANALISIS USABILITY TESTING ===")
    tugas = sorted({s["tugas"] for s in sesi})
    print(f"{'Tugas':<28}{'Sukses':>8}{'Median waktu':>14}{'Error/peserta':>15}")
    for t in tugas:
        d = [s for s in sesi if s["tugas"] == t]
        sukses = sum(s["berhasil"] for s in d) / len(d)
        print(f"{t:<28}{sukses:>7.0%}{st.median(s['detik'] for s in d):>12.0f} dt"
              f"{st.mean(s['error'] for s in d):>14.1f}")
    total_sukses = sum(s["berhasil"] for s in sesi) / len(sesi)
    print(f"\nSuccess rate keseluruhan: {total_sukses:.0%}")

    skor = [skor_sus(j) for j in sus_responden]
    rata = st.mean(skor)
    # Patokan umum: skor SUS rata-rata sekitar 68; di atas itu dianggap di atas rata-rata
    label = "di atas rata-rata (>=68)" if rata >= 68 else "di bawah rata-rata (<68), perlu perbaikan"
    print(f"Skor SUS: {rata:.1f} dari {len(skor)} responden -> {label}\n")


# ======================================================================
# 4. PEMILIH JENIS GRAFIK
# ======================================================================
PANDUAN_GRAFIK = {
    "tren": ("line chart", "perubahan dari waktu ke waktu"),
    "bandingkan": ("bar chart", "membandingkan antar kategori"),
    "korelasi": ("scatter plot", "hubungan dua variabel numerik"),
    "proporsi": ("pie/donut chart", "bagian dari keseluruhan (maksimal sekitar 5 bagian)"),
}


def pilih_grafik(tujuan):
    if tujuan not in PANDUAN_GRAFIK:
        raise ValueError(f"Tujuan harus salah satu dari {list(PANDUAN_GRAFIK)}")
    jenis, alasan = PANDUAN_GRAFIK[tujuan]
    return f"{jenis} ({alasan})"


# ======================================================================
# 5. GRAFIK MENYESATKAN VS JUJUR
# ======================================================================
def buat_grafik(nama_file="hasil_imk.png"):
    warna_utama, warna_redup, warna_anomali = "#0b6e6e", "#9db3c4", "#b3261e"

    # Data contoh: dua produk dengan selisih kecil (97 vs 100)
    produk, nilai = ["Produk A", "Produk B"], [97, 100]
    fig, ax = plt.subplots(1, 3, figsize=(14, 4.2))

    # (a) Menyesatkan: sumbu Y dipotong sehingga B tampak 'jauh' lebih tinggi
    ax[0].bar(produk, nilai, color=warna_redup)
    ax[0].set_ylim(96, 100.5)
    ax[0].set_title("Menyesatkan: sumbu mulai dari 96", color=warna_anomali, fontsize=11)

    # (b) Jujur: sumbu mulai dari 0 + label langsung, tanpa kisi berlebihan
    batang = ax[1].bar(produk, nilai, color=warna_utama)
    ax[1].set_ylim(0, 110)
    ax[1].bar_label(batang, fontsize=11)
    ax[1].set_title("Jujur: sumbu mulai dari 0", fontsize=11)

    # (c) Line chart: HANYA anomali yang diberi warna menyala (atribut pra-atentif)
    bulan = np.arange(1, 13)
    penjualan = np.array([52, 54, 53, 57, 58, 60, 62, 150, 63, 65, 66, 68])
    z = (penjualan - penjualan.mean()) / penjualan.std()
    anomali = np.abs(z) > 2.5
    ax[2].plot(bulan, penjualan, color=warna_utama, lw=2)
    ax[2].scatter(bulan[anomali], penjualan[anomali], color=warna_anomali, marker="D", s=70, zorder=3)
    for b, p in zip(bulan[anomali], penjualan[anomali]):
        ax[2].annotate("Anomali", (b, p), textcoords="offset points", xytext=(8, -4), color=warna_anomali)
    ax[2].set_ylim(0, 170)
    ax[2].set_xticks(bulan)
    ax[2].set_title("Warna menyala hanya untuk anomali", fontsize=11)

    for a in ax:  # data-ink ratio: buang elemen yang tidak menambah informasi
        a.spines[["top", "right"]].set_visible(False)
        a.yaxis.grid(True, color="#e3e7ee", lw=0.8)
        a.set_axisbelow(True)
    plt.tight_layout()
    plt.savefig(nama_file, dpi=120)
    plt.close(fig)
    print(f"=== 5. GRAFIK === tersimpan: {nama_file} (anomali terdeteksi di bulan {[int(b) for b in bulan[anomali]]})\n")


# ======================================================================
# DEMO
# ======================================================================
if __name__ == "__main__":
    cek_kontras([
        ("Teks utama dasbor", "#17202f", "#ffffff"),
        ("Teks sekunder", "#4f5b70", "#ffffff"),
        ("Tombol aktif (teks terang)", "#f3f5f8", "#0b6e6e"),
        ("Abu muda di atas putih", "#b0b7c3", "#ffffff"),
        ("Teks merah anomali", "#b3261e", "#ffffff"),
    ])

    evaluasi_heuristik({
        "Evaluator 1": {1: (3, "Tidak ada indikator loading saat filter"), 3: (2, "Tidak ada tombol urungkan"),
                        5: (4, "Hapus data tanpa konfirmasi"), 9: (3, "Pesan 'Error 400' tanpa solusi"), 10: (1, "")},
        "Evaluator 2": {1: (2, "Status simpan tidak jelas"), 3: (3, "Sulit membatalkan filter"),
                        5: (3, "Form bisa dikirim kosong"), 9: (3, "Pesan error teknis"), 8: (1, "")},
        "Evaluator 3": {1: (3, "Proses lambat tanpa umpan balik"), 5: (4, "Tidak ada konfirmasi hapus"),
                        9: (2, "Pesan error kurang jelas"), 4: (1, "")},
    })

    sesi = [
        {"tugas": "Filter wilayah Jakarta", "berhasil": True, "detik": 8, "error": 0},
        {"tugas": "Filter wilayah Jakarta", "berhasil": True, "detik": 12, "error": 1},
        {"tugas": "Filter wilayah Jakarta", "berhasil": True, "detik": 9, "error": 0},
        {"tugas": "Filter wilayah Jakarta", "berhasil": False, "detik": 40, "error": 3},
        {"tugas": "Temukan anomali", "berhasil": True, "detik": 20, "error": 0},
        {"tugas": "Temukan anomali", "berhasil": True, "detik": 25, "error": 1},
        {"tugas": "Temukan anomali", "berhasil": False, "detik": 60, "error": 2},
        {"tugas": "Temukan anomali", "berhasil": True, "detik": 18, "error": 0},
    ]
    sus = [  # 10 jawaban per responden, skala 1-5 (contoh)
        [4, 2, 5, 1, 4, 2, 5, 2, 4, 2],
        [5, 1, 4, 2, 4, 1, 5, 1, 5, 2],
        [3, 3, 4, 2, 3, 2, 4, 3, 3, 3],
        [4, 2, 4, 2, 5, 1, 4, 2, 4, 1],
    ]
    analisis_usability(sesi, sus)

    print("=== 4. PEMILIH GRAFIK ===")
    for tujuan in PANDUAN_GRAFIK:
        print(f"  {tujuan:<11} -> {pilih_grafik(tujuan)}")
    print()
    buat_grafik()
