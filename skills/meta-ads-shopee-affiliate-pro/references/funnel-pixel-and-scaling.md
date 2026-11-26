# Funnel Architecture, Sub_ID Tracking, Pixel Setup, and Scaling Playbook

Panduan teknis untuk memaksimalkan tingkat konversi dari klik Meta Ads hingga checkout di aplikasi Shopee, memastikan setiap komisi terlacak ke iklan asalnya, dan melakukan scaling tanpa merusak ROAS.

## 1. Decision Tree Pemilihan Funnel

Pilih satu arsitektur utama berdasarkan modal harian dan kesiapan aset teknis pengguna:

| Jalur Funnel | Cocok Untuk | Objektif Meta Ads | Keunggulan Utama | Risiko & Mitigasi |
| :--- | :--- | :--- | :--- | :--- |
| **A. Bridge Page + Meta Pixel (Direkomendasikan)** | Budget >= Rp50.000/hari, ingin optimasi algoritma & retargeting | **Sales (Conversions)** optimasi event klik tombol Shopee (`InitiateCheckout` / custom event) | Algoritma belajar mencari profil pembeli, bisa kumpulkan Custom Audience untuk Retargeting, bisa tampilkan 3 hingga 5 produk (naikkan AOV) | Risiko drop-off jika web lambat. Mitigasi: wajib loading < 1.5 detik, 1 layar langsung terlihat tombol CTA besar |
| **B. Direct Deep Link (Hemat & Cepat)** | Budget mikro Rp25.000 - Rp50.000/hari, validasi cepat tanpa website | **Traffic (Landing Page Views)** atau **Engagement (Post Engagement)** | Tanpa biaya domain/hosting, tidak ada halaman perantara yang mengurangi jumlah klik | Algoritma Traffic suka mencari "clickers" bukan "buyers". Mitigasi: wajib cantumkan harga & promo di kreatif + sematkan link di komentar |
| **C. Shopee Affiliate CPAS** | Affiliate yang sudah mendapat akses katalog kolaboratif seller Shopee | **Sales (Catalog Sales)** optimasi Purchase | Data konversi real-time masuk ke Ads Manager, ROAS terukur otomatis, retargeting dinamis | Tidak semua seller membuka akses CPAS untuk affiliate; tetap periksa margin komisi per SKU |

## 2. Solusi Deep Link (Anti Jebakan Login In-App Browser)

Kesalahan paling mahal di Shopee Affiliate Meta Ads adalah menempelkan URL mentah yang membuka halaman web Shopee di dalam browser bawaan Facebook/Instagram sehingga pengguna diminta login ulang.

- **Aturan Wajib:** Selalu gunakan link pendek resmi dari aplikasi/portal Shopee Affiliate (`https://s.shopee.co.id/...`) yang secara otomatis memicu pembukaan aplikasi Shopee di Android/iOS.
- **Uji Coba Wajib Sebelum Launch:** Buka preview iklan di aplikasi Facebook dan Instagram pada ponsel sendiri, klik tombol CTA, dan pastikan layar langsung berpindah ke **Aplikasi Shopee** (bukan meminta login di browser).
- **Tips Bridge Page:** Pada tombol menuju Shopee di Bridge Page, tambahkan teks penenang seperti *"Buka di Aplikasi Shopee (Klaim Voucher Gratis Ongkir)"* dan gunakan atribut `target="_blank" rel="noopener"` atau skrip redirect dengan jeda 300ms hingga 500ms agar event Meta Pixel sempat terkirim sebelum aplikasi Shopee terbuka.

## 3. Setup Meta Pixel Minimalis pada Bridge Page

Agar algoritma Meta pada objektif **Sales** benar-benar mencari audiens pembeli:

1. **Event 1 (`PageView` + `ViewContent`):** Aktif saat halaman Bridge Page terbuka penuh.
2. **Event 2 (`InitiateCheckout` atau Custom Event `ShopeeOutboundClick`):** Hanya aktif saat pengguna menekan tombol CTA menuju produk Shopee. Jadikan event ini sebagai **Conversion Event** utama pada Ad Set.
3. **Anti-False Firing:** Jangan menembakkan event `InitiateCheckout` saat halaman baru dibuka (tanpa klik tombol), karena akan meracuni data algoritma dengan klik tidak sengaja.
4. **Struktur Halaman Bridge Page Konversi Tinggi (Above-the-Fold):**
   - Headline manfaat + info promo aktif.
   - 1 gambar/GIF produk terbaik (< 80 KB format WebP).
   - 3 poin keunggulan singkat + rating/jumlah terjual.
   - Tombol CTA warna kontras (oranye/hijau) yang langsung terlihat tanpa scroll: *"Cek Harga Promo & Klaim Voucher di Shopee >>"*.
   - Opsional (strategi naikkan AOV): 2 hingga 3 produk pelengkap di bawahnya (*"Sering Dibeli Bersamaan"*).

## 4. Sistem Pelacakan `sub_id` (Wajib untuk Atribusi Akurat)

Shopee Affiliate menyediakan hingga 5 parameter `sub_id` (`sub_id1` sampai `sub_id5`) untuk melacak sumber komisi di laporan dashboard Shopee Affiliate. Gunakan format baku tanpa spasi:

- **`sub_id1`**: Kode produk/niche (contoh: `vacummini`)
- **`sub_id2`**: Kode funnel & tanggal launch (contoh: `bp_nov23` atau `dl_nov23`)
- **`sub_id3`**: Kode audiens/ad set (contoh: `broad_w2545` atau `int_homedecor`)
- **`sub_id4`**: Kode kreatif & hook (contoh: `vid1_hookmasalah` atau `img2_hargamiring`)

Cara pakai:
1. Buat Custom Link terpisah untuk setiap **Ad (kreatif)** di portal Shopee Affiliate dengan memasukkan `sub_id1` hingga `sub_id4`.
2. Pada H+1 dan H+2, buka Laporan Konversi Shopee Affiliate -> filter berdasarkan `sub_id`.
3. Cocokkan total komisi per `sub_id4` dengan total biaya iklan (`Amount Spent x 1.11`) pada Ad terkait di Meta Ads Manager.
4. Hanya pertahankan dan scale iklan yang terbukti mencetak **Net ROAS >= 1.5x** berdasarkan kecocokan `sub_id`.

## 5. Protokol Scaling Aman & Momentum Kalender Belanja Indonesia

Jangan pernah melipatgandakan budget secara mendadak (misal dari Rp50.000 langsung Rp300.000) karena akan mereset fase learning dan meledakkan CPM/CPC.

### A. Syarat Masuk Fase Scaling

- Iklan sudah konsisten profit (Net ROAS >= 1.8x setelah PPN) selama **2 hingga 3 hari berturut-turut** berdasarkan rekonsiliasi `sub_id`.
- Stok produk di toko Shopee masih melimpah dan promo/Komisi XTRA belum akan berakhir dalam waktu dekat.

### B. 3 Metode Scaling Terukur

1. **Vertical Scaling (Naik Bertahap):** Naikkan budget Ad Set pemenang sebesar **20% hingga 30% setiap 24 hingga 48 jam** pada jam 00.00 WIB.
2. **Horizontal Scaling (Duplikasi ke CBO Pemenang):** Kumpulkan 2 hingga 3 Ad Set / Kreatif pemenang (gunakan **Post ID** yang sama agar seluruh like, komentar, dan social proof tetap terbawa!) ke dalam satu kampanye **CBO (Campaign Budget Optimization)** baru dengan budget awal 2x hingga 3x dari budget testing harian.
3. **Retargeting Biaya Murah (Khusus Pengguna Bridge Page / Video Ads):**
   - Buat Custom Audience: *Pengunjung Bridge Page 14 hari terakhir* dan *Video Viewers 50% (ThruPlay) 14 hari terakhir*.
   - Alokasikan 10% hingga 15% dari total budget harian khusus untuk iklan pengingat promo (*"Masih ragu? Voucher gratis ongkir tinggal hari ini!"*).

### C. Strategi Kalender Belanja Indonesia (Budget Pacing)

- **Tanggal Tua (Tanggal 15 hingga 23):** Daya beli cenderung melambat dan CR turun. Turunkan budget 20% hingga 30%, fokuskan ke testing kreatif murah atau kumpulkan audiens hangat (Video Views / Bridge Page Views).
- **Payday Sale (Tanggal 25 hingga 3) & Tanggal Kembar (1.1, 2.2 ... 11.11, 12.12):** Conversion Rate melonjak tajam karena gaji turun dan banjir voucher Shopee. Mulai aktifkan scaling dan kampanye Retargeting sejak **H-2 hingga H+1** puncak promo.
- **Jam Tayang Efektif (Jika menggunakan Lifetime Budget / Ad Scheduling):** Prioritaskan jam aktif belanja Indonesia yaitu pagi (07.00 hingga 09.00 WIB), istirahat siang (11.30 hingga 13.30 WIB), dan prime time malam (19.00 hingga 22.30 WIB).

## 6. Perlindungan Budget, Rasio Masuk per Placement & Tracking Lanjutan (Koreksi 23 Nov 2026)

**Overspend Meta.** Daily budget adalah rata-rata mingguan, bukan cap harian — Meta boleh spend sampai **175%/hari** (maks 7x/minggu), dan hari pertama learning phase volatil. Mitigasi: pakai **lifetime budget atau account spending limit sebagai hard cap**, dan schedule mulai **00.01** keesokan hari (jangan start siang hari). Aturan "budget +20% me-reset learning" tidak pernah diterbitkan Meta — itu mitos; yang benar: learning phase keluar setelah ~50 optimization events per ad set sejak edit signifikan terakhir.

**Rasio masuk per placement.** Tidak ada placement universal: FB Feed mencapai rasio masuk **95–98%** di lapangan, IG Reels **30–50%**, direct link tanpa deep link bisa 10%. Tes placement di ad set terpisah dan ukur rasio masuk, bukan CPC. Bila rasio masuk <30% setelah 100+ klik, perbaiki deep link/placement dulu, bukan kreatif. Target LPV 75–85% hanya realistis di FB Feed.

**Dashboard Meta bukan satu-satunya sumber kebenaran.** Cross-check laporan komisi/pembayaran Shopee sebelum mematikan iklan. Tanpa dedup browser-server (event_id + event_name identik di Pixel dan CAPI), Meta bisa double-count dan ROAS terhitung 2x. Tracking lanjutan bila budget memungkinkan: **EMQ** (Event Match Quality, target 7+, ideal 8,8–9,3 untuk Purchase) via CAPI, **Value Rules**, dan **Audience Segments**. TOFU→MOFU→BOFU jalankan sebagai campaign terpisah per tahap. Sebelum scaling, cek hygiene akun (payment method valid) — jangan buru-buru bikin akun/BM baru saat ada restriksi.

**Jangan campur format dalam satu ad set CBO.** Reels Rp140rb/lead vs image Rp68rb/lead dalam satu ad set: image dapat 0 spend. Pisah ad set per format (per-format testing).
