# Rumus Ringkas (Versi Otomatisasi)

Rumus yang dipakai loop monitor dan Automated Rules untuk memberi vonis. Versi lengkap ada di `meta-ads-shopee-affiliate-pro`, `references/unit-economics-and-diagnostics.md` bagian 2.

## 1. Biaya iklan riil

`Biaya Riil = Spend di Dashboard x 1,11` (PPN; sesuaikan ke 1,12 bila tarif PPN 12% berlaku).

## 2. Komisi bersih per pesanan

`Komisi Bersih = (min(Harga Produk x % Komisi Dasar, Cap Komisi Shopee) + Harga Produk x % XTRA) x (1 - % PPh Efektif)`

Ketentuan skema 15 Sep 2025: komisi dasar affiliate 1,5% non-elektronik / 0,5% elektronik, cap komisi Shopee Rp10.000 per pesanan (cap hanya berlaku untuk komisi dasar, bukan XTRA). PPh efektif di bracket bawah 2,5% (DPP 50% x tarif 5%), bukan 5% flat; tanpa NPWP PPh 20% lebih tinggi. Cek ulang % XTRA tiap minggu (proteksi penurunan hanya 7 hari). Tolak produk elektronik (0,5%) dan produk tanpa XTRA kecuali XTRA-nya besar.

Contoh: harga Rp135.000, XTRA 12% → dasar min(Rp2.025, Rp10.000) = Rp2.025 + XTRA Rp16.200 = Rp18.225 kotor → bersih Rp17.769 setelah PPh 2,5%.

## 3. Max CPC aman

`EPC per Klik Meta = Komisi Bersih x CR (per Klik Shopee) x Rasio Masuk`

`Break-Even CPC = EPC per Klik Meta`

`Target Max CPC Profit (Margin Aman 30%+) = (Break-Even CPC / 1,11) x 0,70`

Koreksi terpenting 23 Nov 2026: rumus lama tidak mengandung rasio masuk (klik Shopee dibagi klik keluar Meta), padahal di lapangan rasio ini 10-30% di IG Reels dan 95-98% hanya di FB Feed. Tanpa faktor ini, CPC murah terlihat untung padahal boncos. Contoh: komisi bersih Rp5.000 x CR 1% = BE Rp50; bila rasio masuk 30%, Max CPC Meta yang sebenarnya sekitar Rp9,50, bukan Rp31,50. Bila Max CPC hasil koreksi < Rp20, produk tidak layak diiklan di budget kecil.

Patokan CR realistis Shopee Affiliate (label estimasi, ukur dari sub_id sendiri selama 7 hari):

- Cold Traffic Direct Link (tanpa deep link / filter lemah): 0,5% hingga 1,0%
- Cold Traffic Deep Link / Bridge Page berfilter harga: 1,5% hingga 3,0%
- Retargeting / Momentum Payday dan Tanggal Kembar: 3,5% hingga 6,0%+

## 4. Vonis EPC vs CPC

`EPC per Klik Meta = Total Komisi Bersih / Total Outbound Click ke Shopee`

`EPC per Klik Shopee = EPC per Klik Meta / Rasio Masuk`

`CPC Efektif per Klik Shopee = CPC Aktual Meta / Rasio Masuk`

Keputusan kill/scale harus memakai CPC efektif per klik Shopee, bukan CPC Meta mentah. CPC Rp150 dengan rasio masuk 30% sebenarnya Rp500 per klik Shopee. Nilai EPC vs CPC di kedua basis (per klik Meta dan per klik Shopee) dengan ambang yang sama:

- PROFIT / SCALE: `EPC >= CPC Aktual x 1,5`
- BREAKEVEN / OPTIMASI: `EPC = CPC Aktual x 1,0 hingga 1,4`
- BONCOS / KILL: `EPC < CPC Aktual` (setelah memperhitungkan jeda pelaporan H+1)

Pisahkan selalu ROAS GMV dari ROAS komisi. GMV bukan komisi, dan klaim ROAS tanpa menyebut basisnya tidak bisa dipakai sebagai benchmark.
