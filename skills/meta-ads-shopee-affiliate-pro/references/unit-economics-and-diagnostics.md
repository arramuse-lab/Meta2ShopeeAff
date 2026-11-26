# Unit Economics, Product Scoring, and Metric Diagnostics

Panduan kuantitatif untuk memfilter produk sebelum beriklan, menghitung batas aman biaya iklan termasuk pajak Indonesia, mendiagnosis kebocoran performa iklan, dan memasang aturan stop-loss otomatis di Meta Ads Manager.

## 1. Winning Product Scorecard (Skala 100 Poin)

Nilai produk sebelum mengeluarkan budget iklan. Hanya jalankan iklan tunggal jika skor >= 70. Jika skor 50 hingga 69, gabungkan ke dalam halaman koleksi (Listicle/Bridge Page). Jika < 50, ganti produk.

| Kriteria | Bobot Maks | Standar Ideal (Skor Penuh) | Tanda Bahaya (Skor Rendah) |
| :--- | :---: | :--- | :--- |
| **Jenis & Besar Komisi** | 30 | Komisi XTRA >= 10% atau komisi bersih >= Rp12.000/order | Komisi Reguler < 5% atau terkena cap komisi kecil |
| **Sweet Spot Harga** | 15 | Rp45.000 hingga Rp250.000 (zona impulse buying Indonesia) — **label estimasi, belum terverifikasi** dari korpus Threads (koreksi 23 Nov 2026); ukur dari data sendiri | < Rp30.000 (margin tipis) atau > Rp500.000 (butuh trust tinggi) |
| **Bukti Permintaan (Demand)** | 15 | Terjual >= 500 pcs/bulan, rating >= 4.7, ulasan foto banyak | Terjual < 50 pcs atau rating < 4.5 |
| **Visual Wow / Problem Solver** | 20 | Manfaat langsung terlihat dalam 3 detik (demo/before-after) | Produk komoditas biasa tanpa keunikan visual |
| **Kesiapan Toko & Promo** | 10 | Shopee Mall / Star+, stok > 100, Gratis Ongkir & Voucher aktif | Stok menipis, toko lambat membalas, tanpa gratis ongkir |
| **Potensi Keranjang Besar (AOV)** | 10 | Toko punya banyak produk pelengkap / audiens biasa beli > 1 pcs | Pembelian satuan sekali pakai tanpa produk pelengkap di toko |

## 2. Kalkulator Unit Ekonomi Anti-Boncos (Indonesia)

Selalu gunakan rumus berikut agar perhitungan tidak menipu:

1. **Biaya Iklan Riil (Actual Spend):**
   `Actual Spend = Ad Spend di Dashboard x 1.11` (sesuaikan ke `1.12` jika tarif PPN 12% berlaku pada tagihan Meta Ads pengguna).

2. **Estimasi Komisi Bersih per Pesanan (Net Commission):**
   `Net Commission = (min(Harga Produk x % Komisi Dasar, Cap Komisi Shopee) + Harga Produk x % XTRA) x (1 - % PPh Efektif)`
   Koreksi 23 Nov 2026 (skema 15 Sep 2025): Komisi Dasar Affiliate 1,5% non-elektronik / 0,5% elektronik, **cap Komisi Shopee Rp10.000/pesanan** (cap hanya berlaku untuk komisi dasar, bukan XTRA); PPh efektif di bracket bawah **2,5%** (DPP 50% x tarif 5%), bukan 5% flat; tanpa NPWP PPh 20% lebih tinggi; afiliator tidak bisa memakai PPh Final UMKM 0,5% (PP 20/2026). Cek ulang % XTRA tiap minggu (proteksi penurunan hanya 7 hari). Tolak produk elektronik (0,5%) dan produk tanpa XTRA kecuali XTRA-nya besar. Contoh: harga Rp135.000, XTRA 12% → dasar min(Rp2.025, Rp10.000) = Rp2.025 + XTRA Rp16.200 = Rp18.225 kotor → bersih Rp17.769 setelah PPh 2,5%.

3. **Batas Maksimal CPC Aman (Break-Even CPC):**
   `EPC per Klik Meta = Net Commission x CR (per Klik Shopee) x Rasio Masuk`
   `Break-Even CPC = EPC per Klik Meta`
   `Target Max CPC Profit (Margin Aman 30%+) = (Break-Even CPC / 1.11) x 0.70`
   Koreksi terpenting 23 Nov 2026: rumus lama tidak mengandung **rasio masuk** (klik Shopee / klik keluar Meta), padahal di lapangan rasio ini 10–30% di IG Reels dan 95–98% hanya di FB Feed. Tanpa faktor ini, CPC "murah" terlihat untung padahal boncos. Contoh: komisi bersih Rp5.000 x CR 1% = BE Rp50; bila rasio masuk 30%, Max CPC Meta yang sebenarnya ≈ **Rp9,50**, bukan Rp31,50. **Bila Max CPC hasil koreksi <Rp20, produk tidak layak diiklan di budget kecil.** Jangan pakai "CPC harus <Rp20" atau "3x harga produk" sebagai aturan kill — denominator yang benar adalah komisi, bukan harga produk.
   Patokan CR realistis Shopee Affiliate (beri label estimasi bila belum ada data validasi sendiri — angka CR di bawah ini **belum terverifikasi** dari korpus Threads, ukur dari sub_id sendiri selama 7 hari):
   - Cold Traffic Direct Link (tanpa deep link / filter lemah): 0.5% hingga 1.0%
   - Cold Traffic Deep Link / Bridge Page berfilter harga: 1.5% hingga 3.0%
   - Retargeting / Momentum Payday & Tanggal Kembar: 3.5% hingga 6.0%+

4. **Metrik Bintang Utara Arbitrase Affiliate (EPC vs Actual CPC):**
   `EPC per Klik Meta = Total Komisi Bersih / Total Outbound Click ke Shopee`
   `EPC per Klik Shopee = EPC per Klik Meta / Rasio Masuk`
   `CPC Efektif per Klik Shopee = Actual CPC Meta / Rasio Masuk`
   Keputusan kill/scale harus memakai **CPC efektif per klik Shopee**, bukan CPC Meta mentah — CPC Rp150 dengan rasio masuk 30% sebenarnya Rp500 per klik Shopee. Nilai EPC vs CPC di **kedua basis** (per klik Meta dan per klik Shopee) dengan ambang yang sama:
   - **PROFIT / SCALE:** `EPC >= Actual CPC x 1.5`
   - **BREAKEVEN / OPTIMASI:** `EPC = Actual CPC x 1.0 hingga 1.4`
   - **BONCOS / KILL:** `EPC < Actual CPC` (setelah memperhitungkan jeda pelaporan H+1)
   Pisahkan selalu **ROAS GMV dari ROAS komisi** — GMV bukan komisi, dan klaim ROAS tanpa menyebut basisnya tidak bisa dipakai sebagai benchmark.

5. **Break-Even ROAS terhadap Komisi:**
   `Break-Even Commission ROAS = 1.15x hingga 1.25x` (sudah menutup PPN Meta Ads dan biaya operasional/domain/tools). Target sehat untuk scaling minimal **1.8x hingga 2.5x** terhadap nilai komisi.

## 3. Matriks Diagnosis Metrik & Troubleshooting Funnel

Urutkan audit dari metrik paling hulu (biaya tayang) ke hilir (closing di Shopee) untuk menemukan titik bocor secara presisi:

| Gejala Metrik | Patokan Sehat (ID) | Akar Masalah Utama | Tindakan Perbaikan Cepat |
| :--- | :--- | :--- | :--- |
| **CPM Terlalu Mahal** | Rp15.000 - Rp35.000 (Broad) | Audiens terlalu sempit, kompetisi ketat, atau kualitas iklan/engagement rendah | Perluas targeting ke Broad, ubah gaya kreatif menjadi lebih native/organik, lakukan comment seeding |
| **Hook Rate (3s Video Plays / Impressions) Rendah** | >= 25% (Bagus >= 35%) | 3 detik pertama tidak menghentikan jempol (scroll-stopper gagal) | Ganti 3 detik awal dengan gerakan visual kuat, teks kontras, atau pertanyaan pemicu masalah |
| **Hold Rate (ThruPlay / 3s Plays) Rendah** | >= 40% - 50% (koreksi riset hook 23 Nov 2026; angka lama 15–25% terlalu rendah) | Isi video membosankan, terlalu panjang, atau tidak langsung ke demo produk | Potong durasi video jadi 15 hingga 25 detik, percepat pergantian scene tiap 2 hingga 3 detik, majukan produk/payoff-nya |
| **CTR (All) Tinggi, Outbound CTR Rendah** | Outbound CTR >= 1.5% (Target >= 2.5%) | Konten menghibur/clickbait tapi CTA lemah atau audiens cuma baca komentar | Perjelas instruksi klik di akhir video & awal teks, sematkan link di komentar teratas |
| **LPV / Link Click Ratio Rendah** | Per placement, bukan universal (koreksi 23 Nov 2026): FB Feed 95–98%, IG Reels 30–50% adalah lapangan-normal-buruk; target 75–85% hanya realistis di FB Feed | Halaman Bridge Page terlalu lambat (> 3 detik), jebakan login in-app browser, atau banyak klik bot Audience Network | Matikan Audience Network, pakai deep link `shopee://` / shortlink resmi, kompres gambar (< 100 KB), pakai HTML/landing page ultra-ringan; bila rasio masuk <30% setelah 100+ klik, perbaiki deep link/placement dulu, bukan kreatif |
| **Outbound Click Tinggi, Order Shopee Nihil (H+1)** | CR >= 1.5% | Price shock (harga tidak disebut di iklan), jebakan login browser, stok habis, atau ulasan toko jelek | Tulis harga/promo di iklan, wajib pakai shortlink app-open (`s.shopee.co.id`), audit halaman produk Shopee |
| **Frequency Tinggi & CPC Mulai Naik** | Frequency < 2.5 (Cold) | Audiens jenuh melihat iklan yang sama (Ad Fatigue) | Segera duplikasi dengan kreatif baru (ganti hook/angle) sebelum ROAS anjlok |

## 4. Template Automated Rules (Stop-Loss Anti-Boncos)

Pasang aturan otomatis berikut di Meta Ads Manager (Menu Automated Rules) pada level **Ad** atau **Ad Set** agar budget tidak habis saat pengguna tidak memantau layar:

### Rule 1: Auto-Kill Kreatif Gagal Hook (Cut Loss Dini)

- **Apply to:** All Active Ads (Campaign Testing)
- **Action:** Turn off ads
- **Conditions:**
  - `Amount Spent` >= Rp20.000 (atau 0.8x Net Commission)
  - AND `Outbound CTR` < 1.0%
- **Time Range:** Today (atau Lifetime saat hari pertama testing)
- **Schedule:** Runs continuously (setiap 30 menit)
- Catatan koreksi 23 Nov 2026: rule ini hanya kill dini berbasis CTR; jangan jadikan kill final — spend Rp20rb terlalu kecil untuk menilai order.

### Rule 2: Auto-Kill CPC Kemahalan (Pelindung Margin)

- **Apply to:** All Active Ads
- **Action:** Turn off ads
- **Conditions:**
  - `Amount Spent` >= Rp50.000 (koreksi 23 Nov 2026: ambang lama Rp25.000 terlalu kecil — Rp20rb pada CPC Rp150 = ±133 klik Meta → ±40 klik Shopee → ekspektasi order <0,5 pada CR 1%)
  - AND `Cost per Outbound Click` > `[Masukkan Nilai Max CPC Aman Koreksi + 15%]` — hitung CPC efektif per klik Shopee (CPC / rasio masuk) bila rasio masuk diketahui
- **Time Range:** Today
- **Schedule:** Runs continuously

### Rule 2b: Auto-Kill Final (Spend Besar, 0 Order) — baru, koreksi 23 Nov 2026

- **Apply to:** All Active Ad Sets
- **Action:** Turn off ad sets
- **Conditions:**
  - `Amount Spent` >= Rp150.000 hingga Rp200.000 (total, lifetime)
  - AND 0 pesanan valid (cek laporan Shopee H+1/H+2 per sub_id)
  - ATAU EPC per klik Meta < CPC x 1,0 selama 2 hari berturut-turut setelah ≥100 klik Shopee
- **Time Range:** Lifetime

### Rule 3: Auto-Alert Pemenang (Notifikasi Scale)

- **Apply to:** All Active Ad Sets
- **Action:** Send notification only (jangan auto-increase drastis tanpa cek komisi Shopee H+1)
- **Conditions:**
  - `Amount Spent` >= Rp30.000
  - AND `Cost per Outbound Click` <= `[Masukkan Nilai Target Max CPC Profit]`
  - AND `Outbound CTR` >= 2.5%
- **Time Range:** Yesterday / Last 2 Days
