# Menghitung impas dan membaca laporan

## Sebelum membeli iklan

Tentukan komisi rupiah yang diharapkan dari satu pesanan **valid**. Utamakan rata-rata pesanan tervalidasi untuk produk dan penawaran sebanding. Jika hanya tersedia tarif, gunakan nilai transaksi yang menjadi dasar komisi, batas maksimum, dan syarat tiap komponen sesuai penawaran. Beri label estimasi. Perlakukan bonus sebagai pendapatan setelah syaratnya terpenuhi. Pisahkan potongan yang sudah tercermin dalam komisi dari biaya yang masih harus dibayar.

| Ukuran | Rumus dan satuan |
| --- | --- |
| Pesanan valid untuk impas | Bulatkan ke atas (anggaran iklan + biaya lain yang diperhitungkan) ÷ komisi rata-rata per pesanan valid. |
| Komisi harapan per klik keluar Meta | Komisi per pesanan valid × (pesanan dibuat yang teratribusi ÷ klik keluar Meta) × (pesanan valid ÷ pesanan dibuat). Gunakan periode yang hasil validasinya sudah tersedia. Bila sudah memakai pesanan valid per klik, kalikan dengan komisi per pesanan valid sekali saja. |
| CPC impas biaya iklan | Sama dengan komisi harapan per klik keluar Meta. Bandingkan dengan biaya per klik keluar pada cakupan yang sama. |
| CPC impas termasuk biaya tetap | Untuk anggaran iklan yang dihabiskan penuh, kalikan komisi harapan per klik dengan anggaran iklan ÷ (anggaran iklan + biaya tetap). Berlaku untuk total biaya tetap pada periode uji tersebut. |

Bila sumber tingkat konversi memakai klik Shopee, ubah ke basis klik keluar Meta menggunakan perbandingan klik Shopee teratribusi dengan klik keluar Meta pada kampanye yang sama. Jika perbandingan itu belum diketahui, tampilkan EPC per klik Shopee dan tandai batas CPC Meta belum dapat ditentukan. Jika tingkat validasi belum tersedia, hitung jumlah pesanan yang diperlukan atau tampilkan beberapa skenario dengan asumsi tertulis. Gunakan titik impas untuk menilai kelayakan ekonomi. Pilih strategi penawaran iklan secara terpisah di Ads Manager.

**Contoh simulasi.** Anggaran Rp150.000, biaya produksi tetap Rp30.000, komisi per pesanan valid Rp10.000. Asumsikan 2 pesanan dibuat per 100 klik keluar Meta dan 75% pesanan itu akhirnya valid. Butuh 18 pesanan valid untuk menutup Rp180.000. Setiap klik diperkirakan menghasilkan komisi Rp150. Pada anggaran tersebut, CPC impas setelah biaya produksi adalah Rp125.

Jalankan dari direktori skill. Masukkan angka tanpa pemisah ribuan dan gunakan titik untuk pecahan. Opsi biaya lain menghitung biaya tetap yang diketahui. Tanpa opsi itu, hasil hanya mencakup biaya iklan.

```bash
python3 scripts/simulasi_impas.py --anggaran 150000 --komisi 10000 --biaya-lain 30000 --pesanan-per-100-klik 2 --validasi-persen 75
```

## Setelah iklan tayang

1. Baca nama kolom dan rincian setiap baris di ekspor. Petakan pengeluaran, tayangan, jenis klik, ID iklan, waktu, serta mata uang Meta. Petakan tautan atau penanda sumber, ID pesanan dan baris produk, status, komisi, tanggal pesanan, validasi, serta pembayaran Shopee sesuai kolom yang ada.
2. Samakan periode tayang, kelompok pesanan yang berasal dari trafik itu, zona waktu, dan tanggal pemutakhiran laporan. Gunakan identitas sumber yang bisa ditelusuri. Pakai status terakhir yang relevan untuk salinan pesanan yang sama. Hitung pesanan berdasarkan ID unik, tetapi jumlahkan komisi pada baris produk unik jika laporan merincinya per produk. Hindari menjumlahkan subtotal yang sudah tercakup dalam total. Pembayaran mencairkan komisi yang sudah dicatat.
3. Hitung pada tingkat yang dapat dibuktikan. Jika dua iklan memakai tautan yang sama, laporkan biaya dan klik tiap iklan serta hasil komisi bersama. Jika tautan turut dipakai organik dan sumber pesanan tidak bisa dipisah, tampilkan total komisi sebagai konteks. Tandai komisi dan hasil bersih khusus iklan “belum dapat diatribusikan”. Bila semua sumber tercakup dan kontribusi tiap sumber nol atau positif, total komisi valid dikurangi belanja iklan memberi batas atas hasil iklan dari komisi yang sudah valid sampai tanggal laporan. Hindari membagi komisi berdasarkan persentase klik.
4. Tampilkan rasio dari jumlah pembilang dibagi jumlah penyebut untuk cakupan yang sama. Pakai “belum tersedia” untuk kolom kosong atau “tidak terdefinisi” untuk penyebut nol. Pengeluaran nol dari sisi kreator dapat terjadi pada promosi yang dibiayai penjual.

| Metrik aktual | Perhitungan |
| --- | --- |
| CPM, CTR keluar, CPC keluar | (Belanja ÷ tayangan) × 1.000, (klik keluar ÷ tayangan) × 100%, dan belanja ÷ klik keluar. Jika hanya tersedia klik tautan, beri nama CPC/CTR tautan dan pertahankan basisnya. |
| Biaya per pesanan valid (CPA) | Belanja iklan kreator ÷ jumlah pesanan valid teratribusi. |
| Komisi per klik (EPC) | Komisi tervalidasi teratribusi ÷ klik untuk kampanye itu. Sebutkan apakah penyebutnya klik keluar Meta atau klik Shopee. |
| Kelipatan komisi terhadap belanja (ROAS komisi) | Komisi tervalidasi teratribusi ÷ belanja iklan kreator. Pada 1×, komisi menutup biaya iklan. Biaya produksi atau biaya tambahan dapat membuat hasil total masih negatif. |
| Hasil setelah biaya | Komisi tervalidasi teratribusi − belanja iklan kreator − biaya langsung lain yang diketahui. Bila biaya lain belum tersedia, sebut “hasil setelah biaya iklan” dan beri tahu cakupannya. |
| ROI untuk biaya yang dihitung | Hasil setelah biaya ÷ total biaya yang diperhitungkan × 100%. Pakai basis komisi dan cakupan biaya yang sama di seluruh laporan. |

Sajikan komisi estimasi yang masih menunggu, nilai penjualan barang (GMV), dan pembayaran sebagai kolom terpisah bila relevan. Tanggal pencairan bisa berbeda dari tanggal belanja iklan yang menghasilkan pesanan itu.
