# Catatan Lapangan Threads — Meta Ads × Shopee Affiliate

Disusun 23 November 2026 dari riset Threads (akun arramuse) yang dilakukan atas permintaan pengguna:
Shopee Affiliate × Meta Ads 1 bulan, Meta Ads umum, Shopee Affiliate umum, mitigasi boncos
3 bulan, hook iklan mendalam, dan reset pembelajaran 3 tahun (Nov 2023 – Nov 2026).
File ini adalah **sintesis**, bukan salinan mentah postingan.

## Cara membaca file ini

Label klaim yang dipakai di seluruh file:

- **[RESMI]** — dokumentasi / pengumuman resmi Meta, Shopee, atau DJP.
- **[ANEKDOT]** — klaim satu kreator Threads tanpa bukti terverifikasi.
- **[BOT]** — jawaban akun `@meta.ai` di kolom komentar (jawaban AI generatif, bukan
  pernyataan resmi Meta; langkahnya boleh dipakai, angkanya jangan dikutip sebagai fakta).
- **[SEKUNDER]** — blog / agensi / panduan pihak ketiga, belum terverifikasi ke sumber resmi.

**Kejujuran soal "riset 3 tahun":** korpus Threads yang berhasil ditarik hampir semuanya
Mei–Nov 2026, dengan hanya 2 postingan pra-2026 (Apr 2024 dan Okt 2024). Tidak ditemukan
postingan Threads 2023–2024 yang sezaman. Jadi 2023–2024 di bawah direkonstruksi dari
sumber resmi + retrospeksi praktisi di Threads 2026, bukan dari postingan sezaman.
2025–2026 didukung Threads + sumber resmi.

Batasan lain: API Threads hanya mengembalikan 1–8 postingan per halaman; isi carousel
berupa gambar tidak terbaca teksnya; sebagian besar utas ramai adalah funnel jualan
(ebook / kelas / pendampingan). Tidak ada riset yang kena rate limit 429.

## 1. Peta evolusi 3 tahun

### 2023–2024 — Akhir era manual, komisi masih besar, direct link liar

**Meta Ads [RESMI]:** Harga rata-rata per iklan Meta turun YoY sepanjang 2023
(Q1 −17%, Q2 −16%, Q3 −6%, Q4 +2%), impresi tumbuh +21% s.d. +34% — lelang longgar.
Q4 2023 harga berbalik naik, dan naik terus setiap kuartal sampai Q3 2026 (+6% s.d. +14% YoY).
Agu 2022 Meta meluncurkan Advantage+ Shopping Campaigns (ASC): 1 ad set, sampai 150
kombinasi kreatif. 2023 Meta mengonsolidasi model ranking ke "Lattice"; ODAX melebur
11 objective lama jadi 6 outcome (Sales, Leads, Engagement, dst). Akar otomasi: iOS 14.5
ATT (Apr 2021) memutus identifier iOS → sinyal Pixel terdegradasi. Pixel diganti nama
menjadi "Dataset" di Events Manager (rollout 2024; ID sama, tidak perlu re-tagging).
CAPI jadi standar pendamping Pixel.
Praktik lapangan era ini [ANEKDOT retrospeksi]: targeting interest/behaviour/demographic
yang "jlimet, banyak", hypertargeted interest, banyak ad set sempit, lookalike standalone,
PPE (Page Post Engagement) untuk social proof murah.

**Shopee Affiliate [RESMI]:** Skema komisi era ini jauh lebih besar dari sekarang:
artikel Agu 2024 mencatat komisi pengguna baru 20% (maks Rp10.000) dan pengguna lama 10%
(maks Rp10.000), plus komisi Shopee hingga 4%. Artikel Jan 2025 menyebut skema 10%/5%.
Trennya jelas menurun. **8 Okt 2024: guncangan pertama** — komisi Shopee hanya untuk
produk bertanda Komisi XTRA dan (untuk Live/Video) kreator Top Creator; banyak afiliator
melaporkan komisi produk yang biasa dipromosikan menjadi Rp0.
CPAS (Collaborative Performance Advertising Solution) sudah berjalan untuk brand sejak
awal 2024: studi kasus Omnicom untuk brand beauty di Indonesia, Feb–Apr 2024, mengklaim
ROAS 6,18x dan 41.000+ penjualan di Shopee. **CPAS sejak awal adalah alat seller/brand
(Mall, Preferred, official), bukan affiliate individu.**
[ANEKDOT] Menurut @origin2market (Mei 2026), sekitar pertengahan 2025 ia menjalankan
direct link affiliate via Meta Ads, mengejar klik massal demi *indirect order*, lalu
**akun Shopee Affiliate-nya ditutup Shopee** karena "dulu Shopee nggak boleh ngiklan"
dan Shopee curiga saat klik banyak tapi order kecil.

### 2024–2025 — Andromeda, komisi dipangkas, lalu kolaborasi resmi

**Meta Ads [RESMI]:** Semester II 2024 Meta men-deploy **Andromeda**; dijelaskan publik
lewat blog Meta Engineering **2 Des 2024**. Andromeda adalah **sistem retrieval**:
dari puluhan juta iklan, dipersempit ke ribuan kandidat per orang, baru lalu ranking +
lelang. Dilaporkan: kapasitas model retrieval naik 10.000x, recall +6%, kualitas iklan
+8% pada segmen terpilih. **Andromeda tidak punya setting di Ads Manager.**
Feb 2025: Advantage+ Shopping diganti nama jadi **Advantage+ Sales** — bukan sekadar
rebranding: ASC adalah tipe campaign terpisah (1 ad set, maks 150 ads, ada existing-customer
budget cap); Advantage+ Sales adalah **status yang dicapai campaign Sales biasa bila
3 tuas ON** (campaign budget + Advantage+ audience + tanpa pembatasan placement), boleh
multi ad set (masing-masing maks 50 ads), existing-customer budget cap dihapus.
Jan 2025: detailed targeting exclusions dihapus; Meta mengklaim campaign tanpa exclusions
berperforma 22% lebih baik (angka klaim Meta sendiri). Nov 2024 Meta merekomendasikan
minimal **20 iklan yang terdiversifikasi** dalam ASC dan **20–30% budget untuk testing**
iklan baru. Juni 2025: sistem manual 8-event AEM (Aggregated Events Measurement, warisan
iOS 14) dihapus; tuas kualitas sinyal berpindah ke EMQ via CAPI.

**Shopee Affiliate [RESMI]:** 15 Apr 2025: biaya layanan affiliate 0,5% dari total komisi
(maks Rp20.000). 17 Apr 2025: Proteksi Komisi XTRA — kalau penjual menurunkan % XTRA,
% lama tetap berlaku 7 hari. **15 Sep 2025: skema komisi baru untuk media sosial** —
Affiliate: 1,5% non-elektronik / 0,5% elektronik, cap Komisi Shopee Rp10.000/pesanan;
Partner: 3,5%, cap Rp50.000. Komisi XTRA tetap tanpa batas. Cookie/atribusi tetap
**7 hari** sejak klik. **22 Okt 2025: Meta–Shopee mengumumkan kemitraan** (diliput
Retail Asia, TechEdt, dll.): Shopee jadi mitra pertama Facebook Affiliate Partnerships —
kreator bisa menautkan akun FB/IG ke Shopee Affiliate dan menandai produk di postingan/Reels;
plus Collaborative Ads untuk Facebook Live (beta di Indonesia, Thailand, Vietnam, Filipina).
3 Nov 2025: skema Live/Video disesuaikan — Komisi Shopee 7%/3% hanya untuk Kreator
Golden Tick dengan syarat XTRA ≥6% (non-elektronik) / ≥1% (elektronik).

**Aturan direct link — kontradiksi tertulis [RESMI, via ringkasan pihak ketiga dari
halaman resmi]:** S&K Program Afiliasi Individu (diperbarui 22 Okt 2026) Pasal 6.2(f):
transaksi dari iklan **tanpa persetujuan Shopee sebelumnya** tidak memenuhi syarat komisi.
Pasal 6.3(n): larangan iklan berbayar untuk link **clickbait**. Halaman Bantuan Shopee
"ketentuan promosi melalui iklan berbayar" menyebut Meta Ads (FB & IG) termasuk platform
yang **sesuai ketentuan**, dengan syarat: tidak mengganggu sistem pelacakan Shopee, pakai
link affiliate langsung tanpa dimodifikasi/disamarkan/dilewatkan perantara, dan simpan
dokumentasi pengaturan iklan untuk verifikasi. **Kesimpulan: aturan tertulisnya ganda
dan penegakannya tidak konsisten** — di atas kertas Meta Ads "boleh dengan syarat", tapi
pasal 6.2(f) memberi Shopee dasar menolak komisi dari iklan tanpa persetujuan. Inilah yang
menjelaskan pola "dulu ditutup, sekarang dibiarkan" tanpa pengumuman perubahan aturan
yang eksplisit. Jangan samakan tiga hal yang sering dicampuradukkan: (a) Kemitraan
Afiliasi FB/IG = penautan organik, resmi sejak Okt 2025; (b) CPAS = iklan katalog
brand/seller, ada sejak ≤2024; (c) Meta Ads direct-link affiliate = strategi trafik
individu di zona abu-abu S&K 6.2(f). **Verifikasi langsung S&K Shopee Affiliate
(27 Agu 2026 / 22 Okt 2026) disarankan sebelum memakai jalur ini sebagai klaim resmi.**

### 2025–2026 — Advantage+ sebagai default, ledakan Shopee × Meta Ads, lalu rasionalisasi

**Meta Ads [RESMI]:** 2025 Meta menyatukan struktur campaign: campaign Sales/App/Leads
baru **default menyala dalam format Advantage+** (Advantage+ audience, placements,
campaign budget ON); mematikan satu tuas = campaign manual. API v25.0 (Feb 2026):
campaign ASC/AAC lama tidak bisa lagi dibuat; v26.0 memblokir edit campaign legacy.
12 Jan 2026: jendela atribusi view 7-hari/28-hari dihapus; default tersisa 7-day click +
1-day view [SEKUNDER]. Andromeda generasi kedua diumumkan 28 Okt 2026: >1 miliar iklan
dinilai per detik per server GPU. **Daily budget adalah rata-rata mingguan, bukan cap
harian**: Meta "may spend up to 75% over your daily promotional budget" (maks 175%/hari,
maks 7x/minggu); dengan ad-set budget sharing bisa 210%/hari. Dokumen API Meta masih
menulis angka lama 25% — ada inkonsistensi antar-dokumen Meta sendiri.
Learning phase: keluar setelah **~50 optimization events per ad set sejak significant
edit terakhir** (biasanya dalam seminggu); edit signifikan me-reset hitungan.
**Learning Limited** = sistem menilai ad set tidak akan mencapai 50 event/7 hari.
Mitos yang dikoreksi sumber sekunder: **aturan "budget +20% me-reset learning" tidak
pernah diterbitkan Meta**; bahasa resmi hanya "may also be significant, depending on
magnitude".

**Shopee × Meta Ads di lapangan [ANEKDOT, 2026]:** Mar 2026: @sasa_suratman
mendokumentasikan akunnya dinonaktifkan/diberhentikan dari Affiliate, lalu hapus akun
dan daftar ulang di hari yang sama dengan data yang sama — diterima. Mei 2026:
@origin2market melaporkan >600 klik di Ads Manager tapi hanya 61 klik terbaca di Shopee
dan 1 order; ia menutup Shopee Affiliate × Meta Ads. Jul 2026: @iqrmmm_ mengklaim modal
Rp15 jt (Apr) berputar jadi Rp86 jt (Jun). Agu 2026: gelombang "Day 1" — @skillforlady
(17 Agu, 1.746 likes) dan @dreaminahome.studio (26–27 Agu) mempopulerkan jalur
**boost post IG → direct link Shopee**, dengan klaim rasio trafik masuk 80–90% dan CR
normal 2–3% (komentar @indrapgun), serta peringatan klik bot Meta dari Brazil/AS.
22 Sep 2026: @liemptr melaporkan setup CPAS kini lewat Collaboration Center, selesai
~15 menit, tanpa form dan tanpa tunggu 14 hari seperti dulu. Ini jalur **seller/brand**.
Nov 2026: konsensus baru mengeras di @bennysoehardi (17 Nov, 243 likes): klik bocor
sampai 70%, solusinya LPV + mobile only + placement IG Reels/Story, klaim klik naik 1,6x.
@ifralaryanto (17 Nov) mengklaim klik Meta dan Shopee sinkron/malah lebih besar di Shopee
— tapi postingannya berjualan ebook. @roybercerita (23 Nov): "Biang kerok Meta Ads–Shopee
itu adalah Facebook itu sendiri" — placement FB yang merusak.

**Yang berubah vs yang tetap:**

| Berubah | Tetap |
|---|---|
| Targeting: interest stack sempit → Broad/Advantage+ audience (suggestion, bukan filter) | Learning phase ~50 event/ad set; jangan otak-atik saat learning |
| Struktur: banyak ad set × interest → 1-1-5 / 1-1-3, adu kreatif | Testing 3 hari, evaluasi berkala, scale 20% bertahap |
| Budget: ABO dominan → CBO/Advantage campaign budget sebagai default & scale | ABO tetap alat testing; CBO tetap alat scale |
| Kreatif: sedikit, statis → volume + variasi angle; Ads Library sebagai riset | Kreatif & LP yang menentukan menang; CTR rendah = masalah kreatif/audiens; klik banyak tak beli = masalah LP/harga |
| Tracking: Pixel saja → Pixel + CAPI + EMQ + dedup event_id | Prinsip: optimasi butuh sinyal konversi yang cukup |
| Campaign: ASC tipe terpisah → Advantage+ Sales sebagai status default | Funnel TOFU→MOFU→BOFU masih diajarkan ke pemula |
| Daily budget dipahami sebagai cap → rata-rata mingguan (175%/hari, 7x/minggu) | — |

**Koreksi kesalahpahaman soal Andromeda:** Andromeda soal retrieval, bukan targeting;
yang mematikan interest adalah kombinasi ATT + penghapusan opsi detailed targeting +
Advantage+ audience sebagai default. Andromeda hanya memperkuat efeknya karena butuh
volume kreatif untuk di-retrieve. Narasi "Andromeda mengubah segalanya" sebagian adalah
*rebranding dari prinsip lama* (konten bagus menang) yang kini dipaksakan oleh hilangnya
kontrol targeting.

## 2. Mitigasi boncos #1: perbaiki klik bocor dulu

Klik Meta tercatat dan dibayar, tapi tidak sampai ke aplikasi Shopee / tidak tercatat
di dashboard Shopee. Ini penyebab boncos nomor 1 di hampir semua utas.

- @bennysoehardi, 17 Nov 2026 — bocor sampai 70%; klaim cara di bawah bikin klik
  1,6x lebih banyak. https://www.threads.com/@bennysoehardi/post/Df0_INpn-QD
  (243 likes, 74 balasan — postingan paling ramai di korpus Shopee Affiliate).
- @dreaminahome.studio, 26–28 Agu 2026 — rasio masuk di kebanyakan orang cuma 10–20%.
  https://www.threads.com/@dreaminahome.studio/post/Dcfoj0jlJE6
- @origin2market, 13 Mei 2026 — >600 klik Meta vs 61 di Shopee + 1 order, bocor ~90%.
  https://www.threads.com/@origin2market/post/DYSKU9ME7ge
- @ifralaryanto (komentar di utas @bangtajud77, 15 Nov): "Biasanya banyak bocornya.
  Fokus utama affiliate itu kalau udah running harus mikir gimana cara biar klik ga
  bocor. Terus baru mikir produk sama strategi konten."
- @bangtajud77, 15 Nov 2026 — sudah coba berkali-kali, habis hampir Rp1 juta, belum
  dapat komisi. Komentarnya, @trikaryati_ juga habis ~Rp1 juta, kembali cuma Rp200 ribu
  (ROAS 0,2x). https://www.threads.com/@bangtajud77/post/DfwKBjQlGVf

Sub-mitigasi yang disebut, dengan ambang:

- **Performance goal → Landing Page View (LPV), bukan Link Click / Max Click.**
  @bennysoehardi, 17 Nov. Alasan: objektif klik mengirim klik termurah, bukan orang
  yang benar-benar sampai. Catatan kritis dari @putraa_hadiii (komentar, 17 Nov):
  Meta tidak bisa mengoptimasi LPV ke Shopee tanpa pixel, karena data sampai-ke-Shopee
  tidak dibalikkan ke Meta — jadi LPV menyaring klik, tapi bukan optimasi konversi
  sungguhan tanpa Pixel/Bridge Page.
- **Device mobile only.** @bennysoehardi, 17 Nov.
- **Placement IG Reels & Story** — klaim total klik aktual Meta vs Shopee paling bagus
  di 2 placement ini. **Mazhab lawan:** @nengwulan.id, 22 Nov (komentar) — FB Feed &
  Reels, CPC ~Rp150, selisih Meta vs Shopee hanya 2–5%; di IG CPC <Rp50 tapi
  "bocor halus". @bennysoehardi sendiri mengakui ada aliran yang strong di FB Feed &
  Reels. @dimasrano (komentar, 13 Mei): placement FB bikin klik banyak dan CPC murah
  tapi zonk di Shopee. **Kesimpulan: tidak ada placement universal — tes keduanya,
  ukur rasio masuk, bukan CPC.** Bukti lapangan terbaru (riset 3 tahun): FB Feed
  mencapai 95–98% masuk (@nengwulan.id), sementara IG Reels 30–50% adalah kenyataan
  lapangan — jadi target LPV 75–85% di skill hanya realistis di FB Feed, bukan universal.
- **Deep link (Buka di Aplikasi).** Generate dari dashboard Affiliate Shopee di browser
  (affiliate.shopee.co.id, Chrome/Safari HP atau laptop), centang "Buka di Aplikasi /
  App Deep Link" sehingga link jadi `shopee://`, jangan ditimpa shortener berlapis
  (bit.ly/s.id). Menu Custom Link / Ubah Link beda fungsi: untuk mengubah link
  non-produk (Shopee Video, Live, event, homepage) jadi link affiliate yang valid.
  SubID diisi lewat form Custom Link (Subid1–Subid5, huruf+angka, tanpa spasi), bukan
  ditempel manual — menghasilkan shortlink `shope.ee/...` (catat: domain ini berbeda
  dari `s.shopee.co.id` yang dipakai di tempat lain; cek mana yang aktif di akun).
  **Sumber: jawaban @meta.ai (bot) di utas @bangtajud77, 15 Nov — jawaban AI, bukan
  pengalaman lapangan, tapi langkahnya cocok dengan ketentuan resmi Shopee yang sudah
  ada di skill. Perlu verifikasi ke Help Center Shopee sebelum dijadikan instruksi
  resmi.**
- **Indonesia only.** @indrapgun, 27 Agu 2026 — bot Meta ikut klik dari Brazil, AS, dll.
- **Rasio klik masuk wajib minimal 80%, biasanya dapat 80–90%.** @indrapgun, 27 Agu 2026.
  Ini cocok dengan LPV Ratio sehat 75–85% di skill — 80% berada di dalam rentang itu.
  **Koreksi dari riset 3 tahun:** jadikan rasio masuk sebagai **gate per placement**,
  bukan satu angka universal. Target 75–85% hanya realistis di FB Feed.
- **Kalau 7 hari berturut-turut tidak bocor → gas.** @dreaminahome.studio, 26 Agu 2026.
  Sebaliknya: "di gas 1 juta malah remuk" — scale besar sebelum validasi menghancurkan
  hasil. Untuk budget kecil, pakai 3 hari untuk sinyal awal, 7 hari untuk scale besar.

## 3. Nilai iklan dari biaya per order / EPC, bukan dari CPC, klik, atau ROAS dashboard

CPC murah adalah jebakan paling berulang. IG klik murah tapi jarang checkout; FB klik
mahal tapi checkout bagus — bisa jadi FB lebih murah per order.

- @bigsundigital (komentar, 22 Nov): "bandingin biaya per checkout, jangan per klik.
  IG kliknya murah tapi jarang CO, FB kliknya mahal tapi CO-nya bagus, bisa jadi FB
  malah lebih murah per order."
- @a__gee (komentar, 31 Okt): "Kalau adsetnya banyak, jangan lihat ROAS dulu.
  Bandingkan biaya per order dengan untung kotor per order."
  https://www.threads.com/@hudayat_h/post/DfJXoMtEiMj
- @firmanalexramadani, 7 Nov 2026 — awal November ROAS di dashboard Meta jadi 0 koma,
  tapi cek dashboard pembayaran terkonfirmasi menunjukkan pemasukan riil sama seperti
  Oktober. Mitigasi: cross-check ke data pembayaran nyata, jangan panik mematikan iklan
  dari dashboard Meta saja. https://www.threads.com/@firmanalexramadani/post/DfcRuFxmZoW
- @gregory.purba, 11 Mei 2026 — CPC <Rp100, CTR >5%, closing <1%, tetap boncos;
  "CPC/traffic murah ≠ profit". https://www.threads.com/@gregory.purba/post/DYMkaPCE9OO
- @asepsyahbudi di utas @iqrmmm_ (1 Jul 2026): "4 bulan boncos sama bocor klik biasanya
  bukan salah algoritma, tapi budget ngalir ke klik yang gak niat beli. coba persempit
  audiens ke yang beneran buying intent, matiin placement yang cuma nyedot klik murah,
  terus ukur dari jumlah order bukan jumlah klik."

**Pisahkan ROAS GMV dari ROAS komisi di semua contoh** — klaim ROAS 4–100× di Threads
adalah GMV brand, bukan komisi affiliate; mencampurnya adalah sumber utama ekspektasi
salah. ROAS komisi 1,2 di hari ke-3 (@bin_sugiyanto, Jun 2026) dianggap lapangan
sebagai zona ragu, bukan scale. Tidak ada postingan affiliate yang menunjukkan scale
pada ROAS komisi 1,8–2,5×; mayoritas affiliate melaporkan ROAS komisi <1 (boncos).

## 4. Testing hemat + era Andromeda: kreatif > struktur

- **Struktur 1-1-5** — @hudayat_h, 31 Okt 2026: 1 Campaign, 1 Ad Set, 5 Ads (kreatif).
  Alasan: era Andromeda, yang diperhatikan adalah kualitas dan variasi konten, bukan
  memperbanyak campaign/ad set. Budget testing Rp35–50rb sudah cukup, dan ia pakai
  **CBO** untuk fase testing. https://www.threads.com/@hudayat_h/post/DfJXoMtEiMj
  (143 likes, 52 balasan)
- **Berhenti cari tombol/struktur magic** — @adsbywhd, 16 Nov 2026: placement dan
  audience sudah serba dibantu AI (Andromeda); skill yang dibutuhkan bukan lagi setting
  campaign, tapi membuat kreatif, landing page, dan membaca data.
  https://www.threads.com/@adsbywhd/post/DfxTdvcEsTo (99 likes)
- **Paksa buka manual placement lewat Meta AI** — @chandrapropertyads, 24 Okt 2026:
  di Ads Manager, buka level Ad Set, buka fitur Meta AI di pojok kanan bawah, ketik
  perintah "Buka manual placement". Beberapa komentator mengonfirmasi berhasil
  (termasuk sampai IG only). Ini bukan setting resmi yang didokumentasikan — sifatnya
  trik lewat chatbot Meta AI, bisa spesifik akun / sementara.
  https://www.threads.com/@chandrapropertyads/post/De3N1AXGDTm
- **Riset winning ads via Ads Library** — @afuza.ads, 9 Jun 2026: buka Meta Ads Library,
  cari 5 brand dengan target market mirip, cek iklan yang masih aktif 30–60+ hari,
  simpan ke Sematin. Didukung @danielsukareview, 23 Nov 2026: menemukan iklan di Ads
  Library yang sudah running **841 hari**.
  https://www.threads.com/@afuza.ads/post/DZWPvt6FIVR
- **TOFU → MOFU → BOFU** — @armansatrio, 26 Agu 2026 (268 likes): Meta Ads bukan
  "pasang iklan → tunggu penjualan"; bangun proses funnel bertahap. Tiap step funnel
  sebaiknya punya campaign khusus (@shobri__).
- **Testing per format** — @bin_sugiyanto (terverifikasi), 28 Jun 2026: per produk
  2 campaign — Scale pakai CBO, Testing pakai ABO; tiap ad set beda format (carousel,
  single image, video, plus satu untuk testing angle baru); kalau 3 hari testing jelek,
  tambah konten baru atau matikan ad set dan ganti baru; kalau winning pindah ke scale.
- **Pembagian kerja yang stabil sejak ~2025 [ANEKDOT]:** **ABO untuk testing**
  (kontrol budget per ad set/audiens, data terbaca bersih per variabel); **CBO untuk
  scale** (setelah winner ketemu). Pengecualian terdokumentasi: campur image +
  Reels/video dalam 1 ad set CBO = jebakan — Reels Rp140rb/lead vs image Rp68rb/lead,
  image 0 spend (@ianfatah, Okt 2026). Solusi lapangan: pisah ad set per format.
- **Varian yang bertentangan:** @lukitjoe — 1-2-2 dengan ABO, 2 ad set beda hook/headline;
  @abeljava, 4 Nov — tetap pisah ad set, pernah ada satu angle yang melempem dalam satu
  ad set tapi bagus saat dipisah; @bin_sugiyanto — testing ABO + scale CBO, kebalikan
  dari @hudayat_h. @abeljava menolak 1-1-5: takut Meta tidak bisa mengoptimasi objektif
  kalau banyak kreatif dalam satu ad set. **Kesimpulan: 1-1-5 adalah default yang
  diperdebatkan, bukan hukum.**
- **Andromeda dan seleksi iklan:** @dualipatdigital, 11 Okt 2026: "Banyak iklan ≠
  banyak peluang tayang. Mesin Andromeda dari Meta menyaring iklan sebelum masuk lelang.
  Kalau 100 iklan lu cuma beda teks diskon, besar kemungkinan semuanya dibaca sebagai
  1 ide yang sama. Yang bikin iklan dibaca 'beda': → visual: model, produk, background
  → **hook 3 detik pertama** → format: foto, video, carousel. Mending 3 iklan yang
  beda beneran daripada 100 fotokopian."
  https://www.threads.com/@dualipatdigital/post/DeVjPhDAUNE
- **Durasi test:** test 3 hari (@mayessence8: test 3 hari @ Rp100rb/hari; @bin_sugiyanto:
  evaluasi 3 hari). @hudayat_h: kalau dari 5 konten hanya 1–2 yang dapat spend — ada
  closing → lanjutkan; tidak ada closing → kill supaya budget pindah ke ads lain.
  @ilhamulaaa, 22 Nov: iklan jalan 3 hari hasilnya tidak jelas, "nggak tega matiin…
  tunggu sehari lagi" — besoknya tetap boncos. "Masalahnya bukan di iklanmu aja, tapi
  di cara kita mutusinnya, yang kebanyakan memakai feeling."
- **Peringatan budget:** @r.aditya.w — 1-1-5 bisa cepat bakar budget kalau 5 kreatif
  jalan bareng tanpa patokan matiin iklan; tentukan dulu batas testnya sebelum launch.
- **Value Rules** — @itsafuzamaruf, 14 Apr 2026: sudah handle ribuan campaign, hal yang
  hampir tidak dipakai kebanyakan klien tapi dampaknya besar adalah Value Rules.
  Detailnya ada di gambar/carousel, tidak terbaca dari teks.
- **Audience Segments** — @farenaldi, 6 Agu 2026: disebut underrated tools di Meta Ads,
  banyak yang belum pakai.
- **Otomatisasi reporting** — @pupungsp, 12 Okt 2026: dulu manual Ads Manager → report
  → CSV → Google Sheet; sekarang input ad account ID, pilih metric & breakdown, tarik
  data — menghemat waktu untuk yang pegang banyak klien.

## 5. Hook — taksonomi, angka, dan testing (riset mendalam)

Korpus Threads khusus hook ternyata **tipis**: query utama hanya mengembalikan
2 postingan per halaman. Laporan ini menggabungkan Threads (praktik lapangan Indonesia),
teori web yang mapan (Motion, Billo, AdLibrary, Drizzle), dan skill ini sendiri.

Prinsip dasar: **satu-satunya pekerjaan hook adalah membuat orang berhenti dan
menonton/membaca di 1–3 detik pertama**. Hook yang baik menggabungkan tiga saluran
sekaligus — **visual hook**, **spoken hook**, dan **text overlay hook** — karena feed
Meta autoplay dan default tanpa suara.

| # | Jenis hook | Contoh 3 detik pertama | Cocok untuk |
|---|---|---|---|
| 1 | Pattern Interrupt | *"Stop moisturizing your face."* | Semua produk, kategori jenuh |
| 2 | Identity Call-Out | *"Khusus buat [ibu rumah tangga / anak kos] yang sering kesal karena [masalah]..."* | Produk niche, audiens jelas |
| 3 | Pain Agitation / Masalah Harian | *"Capek [masalah spesifik] tiap hari padahal solusinya cuma Rp[harga]?"* | Problem-solving: rumah, kecantikan, kesehatan |
| 4 | Curiosity Gap | *"Wait until you see what happened when I switched creative strategies..."* | Produk / mekanisme baru, cold traffic unaware |
| 5 | Social Proof | *"Pantesan sudah terjual [X] ribu pcs dan ratingnya 4.9, ternyata sebagus ini pas dicoba langsung."* | Produk terjual ribuan, rating tinggi |
| 6 | Contrarian / Myth-Busting | *"Everything you've been told about _____ is wrong."* | Audiens skeptis, solution-aware |
| 7 | Result-First / Before-After | *"[Person] went from [bad state] to [good state]. Here's exactly how."* | Hasil visual jelas |
| 8 | Question | *"Spending money on Facebook ads with zero results?"* | Cold traffic |
| 9 | Perbandingan Harga / Value | *"Di mall harganya Rp[mahal], ternyata di Shopee Official-nya cuma Rp[murah] pas promo hari ini!"* | Hampir wajib untuk Shopee Affiliate — sekaligus filter harga |
| 10 | Demo Visual | Visual masalah nyata + demo langsung produk menyelesaikan masalah (detik 4–12) | Produk yang butuh demo detail |
| 11 | Storytelling | Memulai dari tengah konflik, bukan perkenalan produk | Review jujur, cerita pemakaian |
| 12 | Emotion-Driven | Prompt @kontenhustle #2: 5 versi hook yang menyentuh emosi (marah, takut gagal, penasaran, terinspirasi) + alasan emosinya | Konten UGC / native |
| 13 | Hook Penyesalan / Review Jujur | *"Nyesel banget baru tau ada alat ini, tau gitu dari dulu nggak usah keluar uang ratusan ribu buat [alternatif mahal]."* | Produk murah pengganti alternatif mahal |

**Kerangka pengikat:** 5 tahap kesadaran Eugene Schwartz (Unaware → Problem-Aware →
Solution-Aware → Product-Aware / Most Aware). Salah tahap = hook meleset total.
Komentar @natasyaph_ (29 Jul 2026): "Coba pilih 1 level aware dulu kak. Terus bikin
ads copy + creative yang sesuai level mereka" — kalau budget terbatas, fokus ke satu
level aware saja. Struktur video standar: **Hook (0–3 detik) → Body
(agitasi/demo/bukti) → CTA**. Template: 15 detik (Hook 0–3, Agitate 3–8, Solution 8–13,
CTA 13–15), 30 detik (Hook 0–3, Problem 3–8, Solution 8–18, Proof 18–25, CTA 25–30),
60 detik (Hook 0–3, Problem 3–10, Mechanism 10–20, Proof 20–35, Offer 35–50, CTA 50–60).

**Prinsip yang bikin orang berhenti scroll:** spesifik, bukan generik
(@traderloin, 22 Nov 2026: "hook sekeren apa pun kalo isinya generik ya tetep ketauan");
visual dulu, kata-kata kedua; satu ide per hook, satu janji per hook; hook harus cocok
dengan body-nya (@armansatrio, 14 Sep 2026: "video menarik untuk ditonton belum tentu
menarik untuk diklik"); buat hook dengan AI sebagai generator, bukan penulis akhir
(@kontenhustle, 30 Okt 2025 — 5 prompt ChatGPT: Hook Idea Generator, Emotion-Driven
Hook Maker, Hook Rewriter Pro, Scroll-Stopping Headline Lab, Hook Based on Audience Pain;
isi 5 prompt ada di komentar utas itu sendiri).
**Yang bikin orang langsung skip:** logo / perkenalan brand dulu di detik 0–3; intro
lambat; teks kecil yang tidak terbaca di HP; hook generik; hook yang janjinya tidak
dibayar di detik 4–15; foto yang sama terus-menerus (creative fatigue).

**Definisi dan benchmark (web, data praktisi — bukan angka resmi Meta):**

- **Hook Rate = (3-second video plays ÷ impressions) × 100.** Di Ads Manager, kolomnya
  "3-Second Video Plays" dibagi "Impressions". Tambahkan lewat Columns → Customize
  columns → Custom metrics (tidak ada bawaan).
- **Hold Rate = (ThruPlays ÷ 3-second video plays) × 100.** ThruPlay = video diputar
  sampai selesai atau minimal 15 detik.
- **Billo, H1 2026** — rata-rata Hook Rate Meta **25,44%** dari 88.329 iklan video
  berobjektif sales (Jan–Jun 2026, masing-masing >1.000 impressions, spend $122M).
  Tertinggi: Toys & Games 28,79%, Business & Industrial 28,74%, Health & Beauty 28,11%.
  Terendah: Animals & Pet Supplies 21,32%, Electronics 22,21%. Tidak ada industri yang
  rata-ratanya di atas 29%. Hook Rate ≥30% berarti sudah di atas rata-rata semua industri.
- **AdLibrary (2026):** baseline 25%, bagus 30%+, scalable 35%+; di bawah 15% = rusak
  (kill/rebuild total); 15–25% = di bawah baseline; di atas 45% = outlier, verifikasi
  apakah itu clickbait/bot.
- **Hold Rate:** target 40–50%. Hook Rate saja tidak memprediksi CTR — hook yang kuat
  hanya memberi kesempatan menjual, sisanya video yang harus menjual.
- **Pola drop-off:** penurunan paling tajam antara detik ke-3 dan ke-6. **65% penonton
  yang melewati 3 detik lanjut ke 10 detik, dan 45% lanjut ke 30 detik.**
- **Diagnosis Hook vs Hold:** Hook rendah + Hold sehat = terlalu sedikit yang berhenti,
  tapi yang berhenti suka isinya → ganti detik 0–3 saja. Hook tinggi + Hold rendah =
  pembuka menjanjikan sesuatu yang detik berikutnya tidak berikan → majukan produk/payoff-nya.
  Hook dan Hold tinggi + CTR lemah = perhatian beres, masalahnya di offer, CTA, atau
  landing page.
- **Patokan berjenjang (baru, dari riset ini):** <15% rebuild total; 15–25% rework
  1,5 detik pertama; 25–30% baseline; 30–35% bagus; 35%+ scale (dengan syarat EPC).
  Patokan skill ≥25% **cocok penuh** dengan baseline web (25% rata-rata Billo).
- **Angka Threads (anekdot, satu iklan):** @armansatrio, 13 Sep 2026 — satu iklan video:
  Pemutaran 3 detik: 42.641, CTR: 5,04%, CPC: Rp43. Ia mengklarifikasi: itu CTR per
  klik rasio tayang (bukan all — kalau all sekitar 7%), dan "jangan cuma fokus di CTR
  kak, percuma CTR tinggi kalau gk terjadi konversi, apalagi main LP, banyak orang yang
  udh klik tapi kalau LP nya bermasalah kayak lemot atau isi LP ny berantakan, bisa
  jadi orang langsung keluar, tapi meta udah ngebaca itu jadi klik."
  https://www.threads.com/@armansatrio/post/DdOkvm7gZbm
- **Tidak ditemukan di Threads:** distribusi Hook Rate per niche Indonesia, angka Hold
  Rate, dan korelasi Hook Rate → EPC/ROAS secara terukur. Itu celah data.

**Hook bagus vs clickbait / melanggar kebijakan:** Hook bagus spesifik, relevan dengan
audiens dan tahap kesadarannya, janjinya dibayar di body video dalam 15 detik, menyebut
harga/promo secara jujur (khusus affiliate — ini sekaligus filter pembeli), dan visualnya
native. Clickbait: curiosity gap tanpa payoff; Hook Rate >45% tapi Hold Rate anjlok dan
tidak ada klik yang berujung order; hook yang menarik *penonton* tapi bukan *pembeli*.
Melanggar kebijakan: personal attributes ("Apakah kulitmu kusam/berjerawat?"), klaim
medis / hasil absolut ("Pasti putih/kurus/sembuh dalam 3 hari"), impersonasi merek
("Shopee Indonesia Official"), clickbait / trafik manipulatif / penyamaran tautan,
harga menyesatkan (harga di hook harus sama dengan harga di Shopee saat diklik).

**Cara testing hook yang hemat:** uji hook secara terisolasi — ubah **hanya 2–3 detik
pertama**, pertahankan offer, product shot, body, CTA, audiens, dan durasi yang sama.
5 variasi per produk (1-1-5), idealnya 5 hook/angle berbeda. Kill: Spend ≥Rp20.000
AND Outbound CTR <1,0% (kill dini); dari sisi Hook Rate <15% = rebuild total,
15–25% = rework 1,5 detik pertama. **Jangan** menilai konversi Shopee real-time di
jam pertama — laporan komisi Shopee jeda beberapa jam sampai H+1. Scale: Hook Rate
≥30% + Hold Rate ≥40% + Outbound CTR ≥2,5% + CPC ≤ Target Max CPC Profit — dan yang
menentukan akhirnya tetap **EPC ≥1,5× CPC dan Net ROAS ≥1,8x selama 2–3 hari
berturut-turut berdasarkan rekonsiliasi sub_id**. @yonassahirin: hanya butuh 1–2 video
winning untuk bertahan 3 bulan sampai bertahun-tahun — scale pemenang dengan Post ID
yang sama (agar social proof terbawa), bukan membuat ulang video yang sama.
Validasi gratis sebelum bayar (Fase 0): uji hook organik dulu di Reels/TikTok/Shopee
Video; hanya iklankan konten dengan retensi tinggi atau banyak komentar menanyakan link.

**Hubungan hook dengan funnel Shopee Affiliate — hook punya dua pekerjaan, bukan satu:**
(a) hentikan jempol dalam 3 detik agar CPM murah, dan (b) **saring niat beli** dengan
menyebut kisaran harga, fungsi spesifik, atau info promo — agar hanya calon pembeli
serius yang mengklik. Hook yang hanya melakukan (a) menghasilkan CPC murah dan klik
bocor. Message match hook → body → Bridge Page → Shopee: kalau hook menjanjikan harga
Rp69.000 tapi halaman Shopee menampilkan Rp129.000 (voucher habis / varian salah), CR
jatuh. Pola yang berulang untuk checkout: (a) hook masalah spesifik + harga di 3 detik
pertama; (b) demo nyata di detik 4–12; (c) bukti sosial yang bisa dicek (ribuan terjual,
rating 4.9); (d) CTA urgensi yang jujur. **Attribution per hook adalah syarat mutlak:**
tanpa `sub_id4` unik per kreatif/hook (contoh: `vid1_hookmasalah`), tidak mungkin tahu
hook mana yang menghasilkan komisi — risikonya mematikan hook pemenang karena dashboard
Meta menampilkan CPC-nya lebih mahal dari hook clickbait yang CPC-nya murah tapi EPC-nya nol.

## 6. Winning product — riset produk dulu, jangan bayar iklan sebelum produknya winning

- @nengwulan.id, 22 Nov 2026: masalahnya bukan settingan dasar (sudah paham) tapi
  "belum menemukan produk yang winning".
  https://www.threads.com/@nengwulan.id/post/DgCyGeUmAUw
- @ddyrust: "Benerin dulu cara riset produknya, baru cari audiensnya." @heng_4452:
  produknya tidak membuat orang tertarik masuk ke Shopee. @stackmaster07:
  "Jangan lupakan riset produk yaaa." @yossie.sr: "riset & nguliknya diperdalam lagi,
  jangan buru-buru bayar iklan — riset produknya, riset pasarnya, cek algoritma akunmu,
  beda platform beda interest."
- @nirbita.tanaya (28 Agu): "Traffic-nya ga bocor, tapi buying power audiencenya
  kurang." @mutiarapradina_ (28 Agu): harus menemukan orang yang memang tertarik
  belanja, bukan sekadar kepo. @yonathanwijaya88: "cari itu trik biar dapat orang yg
  klik punya impulse buying yg tinggi."
- **Evolusi kriteria:** 2025 — "LP" yang dibahas komunitas bukan landing page buatan
  sendiri, melainkan **Landing Page Festival Kreator yang disediakan Shopee** — halaman
  berisi produk yang sudah ditentukan Shopee untuk diikuti kreator (@para_malinda,
  Feb 2025) [ANEKDOT]. 2026 — pergeseran ke komisi-per-pesanan dan sinyal data:
  @saddamsaness (Agu 2026): "berhenti share produk komisi 2rb… 300 klik cuma dapet
  80rb; pas ganti strategi, 90 pesanan = Rp478,4rb komisi" [ANEKDOT]. Kriteria yang
  muncul berulang di tools & diskusi 2026: (1) produk sedang diiklankan seller,
  (2) komisi per produk, (3) jumlah affiliator yang mempromosikan 7 hari terakhir,
  (4) varian terlaris dari ulasan, (5) sampel gratis tersedia, (6) kesiapan toko.
- **Harga:** tidak ada satu pun postingan Threads yang menyebut angka sweet spot.
  Bukti tidak langsung: contoh pasar di SENA berkisar Rp8,3rb–62rb (masker) dan jersey
  Rp65rb. Jadi sweet spot Scorecard Rp45–250rb **[tidak dikonfirmasi maupun dibantah]**
  oleh bukti Threads 2026 — tandai sebagai gap.
- **Kategori:** sinyal 2026 mengarah ke rumah tangga/home decor, masak/dapur (video
  panci listrik anak kos, Nov 2026), fashion olahraga (jersey) [ANEKDOT]. Tidak ada
  bukti pergeseran kategori sistematis 2023→2026.
- **Rating/terjual:** tetap dipakai, tapi 2026 ditambah sinyal **umur listing** dan
  **tren penjualan** (Risetika menampilkan terjual/bulan, omzet, umur listing).

**Tools riset produk [FAKTA — Chrome Web Store / situs vendor] — semua independen,
bukan resmi Shopee:**

| Periode | Tool | Status |
|---|---|---|
| Jul 2025 | Encompass (Mrhands) | Ekstensi Chrome, v1.0.5; riset + Affiliate Intelligence |
| Sep 2025 | Shopee Affiliate Max | v1.0.0; tangkap data produk affiliate **bulk + export CSV**, filter kategori/harga/rating |
| 2025→2026 | Tokpee | Rp149.999/bln, **tanpa free trial**, export 1.000 produk/bln, PC/laptop only |
| Jan 2026 | OtomasiAjaShopee | v0.3.112; scraping creator/produk + otomasi Seller Center |
| Sep–Nov 2026 | **Risetika** | v1.0.24, update 9 Nov 2026; trial 3 hari; Pro Max Rp59rb/bln; fokus **seller** (market size, ROAS, umur listing). Dibuat PT Teman Bisnis Nusantara |
| Nov 2026 | **SENA** | v1.81.92, update 10 Nov 2026; trial 10 hari; paling affiliate-spesifik (komisi, status iklan produk, sinyal kompetisi affiliate, sampel gratis, Generate Thread AI). Desktop only, login Google, tidak minta password Shopee |
| Sep 2026 | MasterRiset | Disebut @stackmaster07 sebagai alat riset kompetitor/creator [ANEKDOT] |
| Nov 2026 | Shopee Open API | @yourfutura.labs baru dapat akses integrasi API Shopee [ANEKDOT] — arah masa depan: riset via API resmi, bukan scraping halaman |

**SENA — detail [ANEKDOT @sudutsamar, 13 Okt 2026]:** setelah install dan login pakai
Gmail, buka Shopee seperti biasa, fiturnya muncul di halaman Shopee. Bisa cek kategori
yang lagi tren, varian terlaris, generate link affiliate, dan bikin copywriting untuk
posting di Threads. Bisa juga tahu produk sedang diiklankan seller atau tidak, berapa
komisinya, dan berapa affiliator yang sudah mempromosikan produk itu. Penting: harus
login pakai **akun affiliate, bukan akun seller** — kalau pakai akun seller, tombol
"Buat shortlink" dan info komisi tidak muncul. Hanya bisa via PC/laptop, bukan browser
HP. Ada trial 10 hari. **Koreksi penting:** postingan @labibhusn_ (30 Okt 2026) yang
sempat diduga SENA ternyata **Risetika** — pisahkan: SENA = affiliate-spesifik;
Risetika = seller-spesifik.
**Scrape 100 produk dalam ±5 menit** (@stackmaster07, 22 Agu 2026): data produk real
dari Shopee + info komisi Affiliate-nya, lalu scrape → analisa → pilih produk potensial
→ generate link. Detail tool-nya tidak dibuka di postingan.

**Gate produk (skill, dipertahankan + koreksi):** Gunakan Winning Product Scorecard
(skor ≥70 iklan tunggal, 50–69 gabung koleksi, <50 ganti produk). Prioritas Komisi XTRA
≥10% atau komisi bersih ≥Rp10.000/order. **Hitung komisi bersih dengan cap
[RESMI — skema Sep 2025]:** komisi = min(harga × 1,5%, Rp10.000) + (harga × % XTRA),
lalu × (1 − 0,025) untuk PPh efektif bracket bawah (bukan 5% flat — lihat §8).
Tolak produk elektronik (0,5%) dan produk tanpa XTRA kecuali XTRA-nya besar.
% XTRA harus dicek ulang tiap minggu (proteksi penurunan hanya 7 hari).

## 7. Funnel & tracking — Bridge Page vs direct vs pre-sell vs CPAS

| Funnel | Kapan menang (bukti 2026) | Kelebihan | Risiko / catatan era |
|---|---|---|---|
| **Direct deep link** | Jalur utama organik (Shopee Video, Threads, IG Reels, TikTok) dan Meta Ads objektif traffic. @bennysoehardi (Nov 2026): "masih di trafik… format kreatifnya video. **Gaperlu landing page**" [ANEKDOT] | Friksi nol; klik langsung ke Shopee; cocok untuk produk murah/impulsif | Link mentah dianggap spam, jangkauan ditekan di beberapa platform; sekali produk/link ganti, semua konten lama mati |
| **Bridge Page** | Kreator multi-platform (Threads+IG+FB+YouTube+Pinterest) yang jual produk berganti-ganti. @tips.omcharlie (10 Nov 2026): satu link bridge di bio semua platform; alur klik → bridge → lihat produk → klik beli [ANEKDOT] | Satu pintu: ganti produk cukup edit halaman; klik terlacak per platform; pengunjung ter-kualifikasi dulu | Tambah satu langkah klik (drop-off); butuh halaman sendiri + maintenance; **tidak ada bukti angka konversi** vs direct di Threads |
| **Landing pre-sell (buatan sendiri)** | **Tidak ditemukan buktinya di Threads.** Tidak satu pun postingan membahas LP pre-sell per-section / Clarity / message match | — | Gap riset: klaim-klaim itu konteks saja. Satu-satunya "LP" yang dibahas komunitas adalah LP Festival Kreator milik Shopee |
| **LP Festival Kreator Shopee** | 2025: halaman produk kurasi Shopee untuk festival kreator [ANEKDOT — @para_malinda, Feb 2025] | Resmi, produk sudah ditentukan, tinggal promosikan | Tergantung kampanye Shopee; bukan aset sendiri |
| **CPAS** | **Bukan funnel affiliate.** Untuk seller/brand: iklan katalog Meta → checkout langsung di Shopee. Setup kini ±15 menit via Collaboration Center (dulu isi form + tunggu 14 hari) [ANEKDOT — @liemptr, Sep 2026] | Retargeting + lookalike Meta dengan trust Shopee; tanpa transit website eksternal | Syarat ketat (umumnya Mall/Preferred/official); akun iklan baru/BM agency sering jadi kendala; **tidak bisa bikin UTM khusus untuk tracking di Shopee non-Mall** [ANEKDOT] |

- **Landing pre-sell di domain sendiri (`/go-produk`) + Pixel + CAPI (ViewContent &
  InitiateCheckout) sebelum CTA ke Shopee** — sumber: @meta.ai (bot), 19 Okt 2026 —
  **belum ada yang mengonfirmasi hasil lapangannya; bertentangan dengan mazhab
  @bennysoehardi (tanpa landing page).** Catat sebagai opsi, bukan rekomendasi utama.
- **Landing page per-section + Microsoft Clarity + message match** — @adsbywhd, 15 Nov:
  jangan buat LP satu blok HTML raksasa; buat per section agar bisa A/B test per section;
  CTA di hero, tengah (hingga 2), dan bawah; cek Clarity kenapa traffic tidak jadi
  pembeli. **Catatan: tidak ada bukti Threads untuk ini — tandai sebagai praktik
  internal yang belum terkonfirmasi publik.**
- **Tracking [RESMI/SEKUNDER]:** standar 2024–2026: **Pixel (browser) + CAPI (server)
  berjalan bersama untuk event yang sama**, dideduplikasi via `event_id` yang identik +
  `event_name` yang sama. Tanpa `event_id` sama, Meta menghitung ganda → ROAS
  menggelembung 2x. Estimasi Meta: 30–40% konversi tidak teratribusi pada setup
  Pixel-only di 2026 (angka dari panduan API, bukan dokumen resmi Meta — tandai
  hati-hati). **Event Match Quality (EMQ)**: skor 0–10 per event CAPI berdasarkan
  kelengkapan `user_data` (email/phone ter-hash SHA-256 paling berdampak; target umum
  7+, ideal 8,8–9,3 untuk Purchase). EMQ adalah tuas kualitas sinyal pasca-AEM.
- **Lapangan Indonesia [ANEKDOT]:** @scalewithmirza, 10 Okt 2026 (221 likes) — pasang
  tracking manual dengan EMQ bagus "perjuangannya nggak main-main"; setelah EMQ bagus,
  tetap cek konsistensi Purchase, nilai transaksi, deduplikasi browser-server, dan
  selisih dengan data backend. @timkerjaai.id: "Tricknya ada di UTM parameter + pixel
  event yang tepat, bukan cuma soal LP. Kebanyakan orang skip bagian tracking-nya
  makanya traffic kemana-mana." Untuk LPWA/CTWA (Landing Page → WhatsApp, jalur utama
  Shopee Affiliate + lead lokal), CAPI masih jadi pertanyaan terbuka: "tools CAPI Meta
  Ads buat CTWA offline conversion yang paling akurat sekarang apa?" (@dirgrexi, Jul 2026);
  praktisi membandingkan GASS.id, SendWA, LinktoChat (@hendraretamba, Okt 2026).
  **Celah riset:** tidak ada jawaban mapan/terverifikasi di Threads soal stack CAPI
  terbaik untuk CTWA/LPWA.
- **Sub_ID (skill, dipertahankan):** sub_id1 produk/niche, sub_id2 funnel & tanggal
  launch, sub_id3 audiens/ad set, sub_id4 kreatif & hook; rekonsiliasi H+1/H+2 di
  Laporan Konversi Shopee vs Amount Spent × 1,11 di Ads Manager; hanya scale iklan
  dengan Net ROAS ≥1,5x berdasarkan kecocokan sub_id.
- **UTM template** `source=facebook, medium=cpc, campaign={{campaign.name}}`,
  `content={{adset.name}}_{{ad.name}}` — sumber: jawaban @meta.ai (bot), tandai demikian.

## 8. Ambang kill / scale lapangan vs rumus skill — dan KOREKSI yang wajib dipakai

Rumus skill sebagai pembanding: Biaya riil = spend × 1,11 (PPN); komisi bersih =
(harga × % komisi) × (1 − PPh); Break-Even CPC = komisi bersih × CR (CR cold direct
0,5–1%, deep link/Bridge Page 1,5–3%, retargeting/payday 3,5–6%+); Target Max CPC
Profit = (Break-Even CPC/1,11) × 0,70; EPC vs CPC (scale ≥1,5x, breakeven 1,0–1,4x,
kill <1,0x); Break-Even ROAS komisi 1,15–1,25x, scale 1,8–2,5x; LPV 75–85%;
Hook Rate ≥25%; Outbound CTR ≥1,5% (target 2,5%); Frequency <2,5; Auto-Kill:
spend ≥Rp20rb AND Outbound CTR <1,0%; spend ≥Rp25rb AND CPC > Max CPC +15%.

| Ambang | Lapangan | vs Skill | Penilaian |
|---|---|---|---|
| Biaya riil = spend × 1,11 (PPN) | [RESMI] PPN 11% atas iklan Meta untuk akun Indonesia | **COCOK — pertahankan** | — |
| Komisi bersih = (harga × % komisi) × (1 − PPh) | [RESMI] PPh 21: DPP 50% × komisi × tarif progresif; tarif efektif terendah 5% → potongan efektif hanya **±2,5%** dari komisi, bukan 5%; tanpa NPWP +20% lebih tinggi; PP 20/2026: afiliator/kreator konten adalah pekerjaan bebas — **tidak bisa memakai PPh Final UMKM 0,5%**; pakai tarif progresif PPh 17 (5%–35%). [RESMI] Cap Komisi Shopee Rp10.000/pesanan (Affiliate) sejak Sep 2025; XTRA bisa turun sewaktu-waktu (proteksi hanya 7 hari) | **SEBAGIAN COCOK — KOREKSI:** (1) jangan pakai PPh flat 5% — pakai 2,5% efektif di bracket bawah, atau hitung progresif; (2) wajib pakai **cap Rp10.000**; (3) % XTRA dicek ulang tiap minggu | Koreksi terpenting kedua setelah rasio masuk |
| Break-Even CPC = komisi bersih × CR | CR lapangan: cold direct <1% (@gregory.purba) dan 1,6% (@origin2market) — sejalan dengan CR cold 0,5–1% skill | **COCOK untuk cold direct; BELUM TERVERIFIKASI untuk deep link/Bridge 1,5–3% dan retargeting 3,5–6%+** — tidak ada satu pun postingan yang mengukur CR deep-link atau retargeting secara terpisah | Jangan klaim angka itu tervalidasi lapangan |
| Target Max CPC Profit = (BE CPC/1,11) × 0,70 | CPC <Rp100 tetap boncos bila rasio masuk 20–30% (@nur_hikam, @gregory.purba); CPC Rp150 di FB Feed lebih untung daripada CPC <Rp50 di IG Reels (@nengwulan.id) | **BERTENTANGAN / PERLU KOREKSI — koreksi terpenting:** rumus skill tidak mengandung rasio masuk. **Koreksi: Max CPC Meta = komisi bersih × CR × rasio masuk × 0,70 / 1,11.** Contoh: komisi bersih Rp5.000 × CR 1% = BE Rp50; bila rasio masuk 30%, Max CPC Meta = 50 × 0,30 × 0,70 / 1,11 ≈ **Rp9,50** — bukan Rp31,50. Inilah mengapa CPC "murah" Rp55–100 tetap boncos | Wajib ditambahkan ke skill |
| EPC vs CPC (scale ≥1,5×; breakeven 1,0–1,4×; kill <1,0×) | Tidak ada postingan Threads yang memakai istilah EPC. Lapangan memakai ROAS komisi / jumlah order / rasio klik sebagai bahasa keputusan | **BELUM TERVERIFIKASI — BARU sebagai bahasa lapangan.** Konsepnya benar secara matematis, tapi harus didefinisikan eksplisit: EPC **per klik Meta** = rasio masuk × CR × komisi bersih. Bila EPC dihitung per klik Shopee, rasionya berbeda dan ambang 1,5× menyesatkan | Definisikan eksplisit di skill |
| Break-Even ROAS komisi 1,15–1,25×; scale 1,8–2,5× | @bin_sugiyanto (Jun 2026): ROAS 1,2 di hari ke-3 ditanyakan "baiknya dimatikan?" — lapangan menganggap 1,2 sebagai zona ragu, bukan scale. Tidak ada postingan affiliate yang menunjukkan scale pada ROAS komisi 1,8–2,5×; mayoritas affiliate melaporkan ROAS komisi <1 (boncos) | **COCOK arahnya, ambang scale BELUM TERVERIFIKASI untuk affiliate.** ROAS 4–16× yang muncul di Threads adalah **ROAS GMV brand/e-commerce, bukan ROAS komisi** — jangan dicampur | Pisahkan ROAS GMV dari ROAS komisi di semua contoh |
| LPV 75–85% | Lapangan: 10% (@origin2market: 61/600+), 20–30% (@nur_hikam), ±30% (bocor 70%, @bennysoehardi), hanya FB Feed yang mencapai 95–98% masuk (@nengwulan.id) | **BERTENTANGAN sebagai target universal — KOREKSI:** jadikan LPV/rasio masuk sebagai **gate per placement**, bukan satu angka. Direct link IG Reels di bawah 50% adalah normal-buruk di lapangan, bukan anomali. Target 75–85% hanya realistis di placement FB Feed | Turunkan klaim universal |
| Rasio klik masuk ≥80% (biasa 80–90%); CR normal 2–3%; CR >5% → gas budget | @indrapgun, 27 Agu 2026 | **COCOK.** 80% berada di dalam rentang skill. CR >5% sebagai sinyal scale lebih agresif — gabungkan: CR >5% saja tidak cukup, harus disertai EPC ≥1,5× CPC | — |
| 7 hari berturut-turut tidak bocor → gas | @dreaminahome.studio, 26 Agu 2026 | **COCOK arahnya, lebih ketat.** Untuk budget kecil, pakai 3 hari untuk sinyal awal, 7 hari untuk scale besar | — |
| 3× harga produk belum ada hasil = matikan | @r.aditya.w, 1 Nov 2026 (komentator, bukan penulis utas) — **tidak ditemukan ulang di korpus riset 3 tahun** | **BERTENTANGAN — jangan dipakai untuk affiliate.** Aturan ini masuk akal untuk seller (margin = harga − COGS), tapi untuk affiliate komisi hanya sebagian kecil dari harga. Contoh: produk Rp135rb, komisi bersih Rp15.795 → 3× harga = Rp405rb spend sebelum kill, padahal 1× komisi saja sudah Rp15.795. Untuk affiliate, denominator yang benar adalah **komisi**, bukan harga produk. 3× harga produk pada komisi 1,5%+XTRA = ±200× komisi | Jangan pakai |
| CPC harus <Rp20, ideal Rp5 | @rudiiife, 23 Sep 2026; klaim CPC Rp19 muncul di komentar (@awalnur36); CPC Rp55 (@nableeee) — keduanya tanpa dashboard dan tanpa order | **BERTENTANGAN — jangan dipakai sebagai patokan universal.** CPC harus diturunkan dari komisi × CR × rasio masuk, bukan angka absolut. CPC Rp19–55 adalah sinyal traffic murah berkualitas rendah, bukan sinyal profit | Ambang salah terkonfirmasi |
| Hook Rate ≥25%; Outbound CTR ≥1,5% (target 2,5%) | CTR >5% tetap boncos (@gregory.purba) — CTR tinggi tidak memprediksi profit bila kliknya bocor / tidak niat beli | **SEBAGIAN COCOK — CTR adalah syarat perlu, bukan cukup.** Tidak ada angka Hook Rate di korpus ini (tidak terverifikasi). Kill/scale tidak boleh memakai CTR saja | — |
| Frequency <2,5 | Tidak ada satu pun postingan/komentar yang menyebut frequency | **TIDAK ADA BUKTI — netral.** Pertahankan sebagai hipotesis, bukan ambang tervalidasi | — |
| Auto-Kill: spend ≥Rp20rb AND Outbound CTR <1,0% | Keputusan kill lapangan lebih sering berbasis rasio masuk / 0 order setelah ±Rp80rb (@gregory.purba: ±Rp80rb, 2 hari) atau rasio 20–30% (@nur_hikam) | **COCOK arahnya, TAPI sampel terlalu kecil:** Rp20rb pada CPC Rp150 = ±133 klik Meta → ±40 klik Shopee → ekspektasi order <0,5 pada CR 1%. Kill pada Rp20rb berisiko membunuh iklan yang belum sempat dapat sinyal. **Naikkan ambang spend kill ke ≥Rp50rb atau ≥100 klik Shopee**, kecuali CTR <1% DAN rasio masuk <30% | Koreksi ambang |
| Auto-Kill: spend ≥Rp25rb AND CPC > Max CPC +15% | CPC murah di placement salah (IG Reels <Rp50) lebih buruk daripada CPC mahal di FB (Rp150) | **BERTENTANGAN bila dipakai mentah — KOREKSI:** kill berbasis CPC harus memakai **CPC efektif per klik Shopee** (CPC ÷ rasio masuk), bukan CPC Meta mentah | Koreksi |
| Budget testing Rp35–50rb/hari; test 3 hari | Rp30–50rb/hari adalah norma lapangan (@firmanalexramadani Rp30rb, @kosankuu Rp40rb, @bukankoding Rp50rb); @bin_sugiyanto testing ABO ±seminggu | **COCOK.** Catatan: 3 hari × Rp30rb = Rp90rb → pada CPC Rp150 dan rasio 30% hanya ±180 klik Shopee → ±2 order pada CR 1%. Sinyal tipis; 3 hari adalah minimum, bukan jaminan | — |
| Scale +20% tiap 24–48 jam | @rahmatmajeed (Agu 2026): CBO 1 campaign 1 produk, KPI < target → scale 20%, KPI > target → turun 20%. @hudayat_h (Okt 2026): scale-up membuat performa langsung turun | **COCOK — ambang paling konsisten bertahan di lapangan 2026.** Satu-satunya angka scale yang muncul berulang dan tidak dibantah | — |
| Overspend Meta sampai 175% | Tidak ada postingan/komentar yang menyebut angka 175% atau overspend harian vs budget di korpus Threads ini | **TIDAK ADA BUKTI di korpus Threads ini.** Yang ada: pacing cepat (@bukankoding: budget Rp50rb/hari tersedot dalam 19 menit) — itu soal pacing/placement, bukan overspend 175%. [RESMI: dokumen Meta memang menulis maks 175%/hari] | Pertahankan sebagai fakta resmi, bukan bukti lapangan |
| Biaya per order vs untung kotor per order; ad set yang lewat batas itu yang bocor | @a__gee, 31 Okt 2026 | **COCOK, dan lebih tajam dari ROAS.** Ini versi lapangan dari rumus skill — pakai sebagai aturan kill utama | Tegaskan sebagai aturan pertama di Step 5 |

**Tren angka 2023–2026 (sintesis):** bukan "makin murah atau makin mahal" secara tunggal.
**Harga lelang Meta naik konsisten sejak akhir 2023 [RESMI], sementara komisi Shopee
menyusut dan makin bersyarat [RESMI 2024–2025].** Di lapangan affiliate, CPC terlihat
murah (Rp50–300) karena traffic berkualitas rendah — dan justru di situlah boncos
terjadi: CPC murah + rasio masuk rendah + CR <1% + cap komisi Rp10.000 = EPC runtuh.
Kenaikan biaya Q4 (11.11) memperparah, tapi bukan penyebab utama. Data sekunder
(bukan resmi Meta): CPM Indonesia ~US$2,80 dan CPC ~US$0,18 (±Rp2.800) (AdAmigo/AdMakeAI
2026); CPC umum Indonesia Rp500–Rp3.500; CPM mingguan Indonesia ±Rp19.500 awal Apr 2026
→ **Rp37.363 pada minggu 26 Okt–1 Nov 2026** (pra-11.11) — hampir 2× dalam 7 bulan,
tapi ini **musiman Q4**, bukan tren struktural. CPC affiliate Rp19–287 di Threads jauh
di bawah benchmark umum karena objektif traffic + placement Reels, bukan karena pasar
murah secara umum.
Angka lapangan affiliate 2026 [ANEKDOT]: CPC Rp19–Rp55 (klaim komentar), <Rp100
(@gregory.purba, Mei), Rp150 (@nur_hikam, dinilai "bagus" karena rasio masuknya tinggi),
Rp287 (@firmanalexramadani, Nov: Rp30rb/hari → 111 klik), >Rp150 semua adset
(@grosir_hemat77, Nov, mengeluh). Rasio masuk: ±10% (@origin2market), 20–30%
(@nur_hikam), ±54% (angka yang ditanyakan di komentar @gregory.purba, belum
terkonfirmasi), bocor 70% alias masuk ±30% (@bennysoehardi), 95–98% masuk hanya di FB
Feed (@nengwulan.id). CR (dari klik Shopee): <1% (@gregory.purba), 1 order dari 61 klik
= 1,6% (@origin2market).

**Kesalahan boncos yang berulang tiap tahun** (pola yang sama antara Apr 2024 → Mei–Nov
2026; untuk 2023 dan 2025 tidak terverifikasi dari Threads):
1. Menyamakan CPC murah dengan profit — Mei 2026 @gregory.purba → Okt 2026 @agilgilang08
   (kejar CPC <Rp100, 50% klik bot luar negeri / click-and-bounce) → Nov 2026 komentar
   @firmanalexramadani (CPC Rp19–55 dibanggakan, dikoreksi: klik Shopee paling separuhnya,
   0 order).
2. Tidak pernah membandingkan klik Meta vs klik Shopee (tidak cek rasio masuk/LPV) —
   Mei 2026 @origin2market (600+ vs 61) dan @gregory.purba → Okt 2026 @nur_hikam →
   Nov 2026 @bennysoehardi (bocor 70%).
3. Menilai terlalu cepat (hari ke-1–2) ATAU sebaliknya menahan boncos berbulan-bulan
   tanpa kill rule — Mei 2026 @gregory.purba → Jul 2026 @denmas.mr (hari ke-8 masih
   boncos) → Sep 2026 komentar di @iqrmmm_: "4 bulan ngiklan, cuma 1× winning,
   kesininya boncos terus".
4. Modal kecil, ekspektasi besar; top-up Rp100rb habis tanpa rencana — Sep 2026
   @bukankoding → Nov 2026 @nengwulan.id.
5. Tidak menghitung pajak & cap komisi — akar [RESMI]: skema Okt 2024 (komisi jadi Rp0
   untuk produk non-XTRA) → Sep 2025 (cap Rp10.000). [ANEKDOT] Nov 2026 @melanikus_7:
   "pajak Shopee Affiliate melebihi komisi setiap hari" (tanpa bukti angka; kemungkinan
   salah paham akumulasi PPh/NPWP).
6. Memilih produk tanpa Komisi XTRA / komisi kecil / elektronik 0,5% — di lapangan 2026,
   tidak ada postingan yang menunjukkan afiliator menghitung % XTRA sebelum beriklan;
   produk dipilih dari "yang lagi rame", bukan dari komisi.
7. Placement serampangan (semua placement / IG Reels) lalu heran klik bocor — dua klaim
   placement yang **bertentangan**; pelajarannya: placement harus diuji per akun, bukan
   ditiru mentah.
8. Scale dengan menaikkan budget besar sekaligus → performa drop — Jun 2026
   @bin_sugiyanto → Agu 2026 @rahmatmajeed (scale 20%) → Okt 2026 @hudayat_h ("setiap
   kali scale up, performa langsung turun").
9. Percaya screenshot ROAS / kelas yang menjual "cuan instan" — Mei 2026 komentar
   @einryuukie di @gregory.purba: yang share thread cuan kebanyakan gimmick jualan
   kelas; modal tidak sebanding, klik Meta vs Shopee beda jauh. Pola "CARA INSTAN KAYA /
   DM OM" juga diejek oleh @babanatabumi (Nov 2026).
10. Tracking tidak sinkron (pixel/CPAS/EMQ) lalu menyalahkan algoritma — Okt 2026
    komentar @timkerjaai.id di @origin2market (gap 600 vs 61 = tracking/pixel tidak
    sync, cek EMQ) dan @scalewithmirza. Juga komentar @cerita.audi: mempertanyakan
    apakah "Meta Ads × Shopee Affiliate" adalah program resmi — **[fakta resmi, perlu
    koreksi narasi lapangan]:** bukan program kemitraan resmi Meta–Shopee; ini strategi
    traffic biasa (kampanye traffic ke link affiliate).

## 9. Launch — lindungi budget dari pacing Meta, dan higiene akun

- **Overspend harian:** @bukankoding, 23 Sep 2026 — top-up Rp100rb, budget Rp50rb/hari,
  iklan jalan 14.00 dan 14.19 saldo sudah banyak terpakai.
  https://www.threads.com/@bukankoding/post/DdoZAZaAZ3M
  @donylimm / @samuelaripin / @gustiaditpratama (23–24 Sep): daily budget bisa tersedot
  sampai 175% dalam sehari (maksimum Meta); normalnya 10–20% di atas target, rata-rata
  mingguan tetap sesuai. Mitigasi: pakai **lifetime budget** atau **account spending
  limit** (hard cap). @diditrinjano: "hindari langsung running iklan kalau udah lewat
  pertengahan hari… lebih baik di-schedule tayang jam 12.01 keesokan harinya."
  @teradjana: Meta "ngejar setoran" kalau start siang.
- **Higiene akun sebelum scale:** @origin2market — akun Shopee Affiliate dulu pernah
  ditutup karena direct link + mengejar klik/indirect order dalam jumlah besar; Shopee
  curiga klik banyak tapi order kecil. @doratatiana, Nov 2026 — akun bisnis IG tidak
  bisa beriklan berbulan-bulan karena kartu kredit expired; iklan jalan 1 hari lalu
  kena stop karena data CC lama belum diganti. Pelajaran: cek metode pembayaran
  sebelum scale.
- **Kebijakan / penolakan iklan yang berulang [ANEKDOT + SEKUNDER]:** pola akun kena
  restrict: banding ditolak, CS "nggak terlalu membantu", bikin akun/BM baru pun ditolak
  (@faris_yudza, Mei 2026); masalah menggantung 1 bulan, banding ditolak (@mr.nashci,
  Agu 2026). Tidak ada solusi yang terverifikasi muncul di komentar. Taksonomi yang
  berguna (bukan resmi): penolakan iklan (ringan, per kreatif) vs restriksi (akun tidak
  bisa buat iklan baru) vs disable (akses diputus). Pemicu umum: klaim kesehatan/finansial
  tanpa disclaimer, before-after, personal attributes, landing page mismatch, pelanggaran
  kecil berulang. Meta menyatakan akun yang direstriksi >180 hari tidak bisa dipulihkan
  — klaim dari blog yang mengutip Meta, belum terverifikasi langsung. Pergeseran 2025
  ke enforcement berbasis risk-score + pembatasan data source kategori sensitif
  (kesehatan/wellness, lalu finansial/Core Setup Mar 2025) — event mid/low funnel
  (ATC, Purchase) tidak bisa dipakai optimasi. **Belum terverifikasi ke dokumen resmi
  Meta** — perlakukan sebagai laporan praktisi.

## 10. Organik vs berbayar, konten AI, dan Shopee Affiliate Singapura

**Tema dominan 3 bulan terakhir: produksi konten pakai AI.** Claude/ChatGPT untuk
naskah, Gemini/Dreamina/Kling/Google Flow untuk gambar & video, prompt AI dari POV
audiens, dan otomatisasi Threads. Bukan lagi sekadar "posting link".

- **Prompt AI dari POV audiens** — @vanthenextlevel, 22–24 Okt: klaim komisi
  Rp26.056.889 semuanya dari media sosial, pakai AI gratisan — Claude + ChatGPT
  bergantian kalau token habis; gambar & video pakai Gemini, Dreamina, Kling, Google
  Flow; format video dan teks untuk Threads; bahas dari sisi emosional. Prompt lengkapnya
  diarahkan ke ebook berbayar — dan ada pembeli yang mengeluh di komentar ebooknya
  tidak masuk.
- **Tutorial Google Flow** — @rijalaufaar, 5 Nov: tutorial membuat video affiliate
  pakai Google Flow — 3.563 likes, 739 repost, 139 balasan. Isi tutorialnya ada di video,
  tidak terbaca dari teks. Dari komentar: Flow reset harian, video bisa diperpanjang
  (penulis janji buatkan tutorial lanjutan), aktifkan label "konten AI" saat upload,
  penulis mengaku punya 5 akun.
- **AI video (Google Flow/Veo) [FAKTA]:** Veo 3 tersedia global termasuk Indonesia sejak
  Juli 2025 untuk pelanggan AI Pro (159 negara); Flow memakai sistem kredit harian yang
  reset tiap hari; 2026 ada Veo 3.1 dan Flow digabung dengan Whisk/ImageFX (Feb 2026).
  Kendala berulang: kredit gratis cepat habis, output sering diawali freeze-frame foto
  upload (VO terpotong saat di-cut), konsistensi wajah/produk antar render tidak stabil
  — solusinya prompt lock wajah/gerakan + referensi tiap scene.
- **Threads organik pakai AI** — @_anhalim, 12 Nov: Day 1 nyoba AI untuk affiliate
  Threads x Shopee. Dari komentar terungkap yang dipakai adalah dashboard/tool
  auto-affiliate custom ("buzzer-pro") — **bukan produk resmi Shopee/Threads**,
  menurut balasan Meta AI. Saran Meta AI di situ: siapkan link Shopee Affiliate dulu,
  koneksikan Threads via Threads API + AI untuk generate utas jualan dari link produk,
  buat scheduler + dashboard, jaga rasio **1 jualan : 3 utas biasa** supaya tidak
  ke-detect spam, dan tambahkan tracking komisi harian. Peringatan dari komentator:
  spam link produk di Threads, sekali kena report spam akun bisa langsung melayang.
- **Content planning TOFU → MOFU → BOFU** (@aklifsainie, 28 Apr — di luar 3 bulan,
  tapi muncul di Top): satu SKILLS.md untuk Claude.ai, content plan 1 produk selama
  1 minggu, 2 posting Threads per hari, total 14 konten.
- **Format yang bertahan di kedua jalur (organik & berbayar):** video vertikal pendek +
  angle problem-solution; produk komisi besar lebih diutamakan daripada produk murah
  bervolume; riset produk berbasis data sebelum produksi konten. **Video vertikal UGC
  problem–solution, 10 detik, VO Bahasa Indonesia** — format dominan. Prompt Flow yang
  berulang: `/ugcproblemsolution /ugcaffiliate /ugchookproduk`, durasi 10s
  (@haryono_pro, Okt 2026); storyboard dibuat dulu via ChatGPT.
- **Native soft-sell organik:** video masak/daily life, link affiliate ditaruh di
  **reply/komentar**, bukan di caption utama (@ehkepakeaja, 23 Nov 2026 — video panci
  listrik + reply berisi link `s.shopee.co.id` dengan `affiliate_id`).
- **Dapat sampel:** tawaran sampel terbuka di kolom komentar, contohnya produk Dewi Sri
  Spa Whitening Premium Scrub, SOW 1 VT + keranjang kuning, niche Beauty/BodyCare/Face
  Review (bukan Product Only), **tanpa minimal followers dan tanpa minimal views**,
  via DM. Polanya: seller cari affiliator kecil, bukan cuma yang besar.
- **Banjir pemula:** tab Recent didominasi akun baru yang minta ditutorin dan postingan
  yang isinya cuma link affiliate mentah tanpa konteks (spam).

**Organik vs iklan berbayar, menurut postingan di sana:**

- **Organik (Shopee Video, Threads, IG Reels, TikTok):** tanpa biaya iklan, komisi jadi
  laba bersih dikurangi waktu. Kuncinya volume + konsistensi konten, dibantu AI untuk
  skala (naskah, video, scheduling). Jalur sampel gratis cocok untuk pemula tanpa
  followers. Risikonya: lambat, dan spam link bisa membuat akun hilang. Veteran yang
  muncul di riset sebelumnya mengklaim Shopee Video masih paling kuat untuk komisi
  tinggi — di pencarian ini tidak ada postingan baru yang membantah atau mengonfirmasi
  klaim itu secara langsung.
- **Berbayar (Meta Ads):** trafik cepat, tapi hanya objektif Traffic yang realistis
  untuk affiliate, Meta sulit mendorong sampai closing, dan klik bocor adalah pajaknya.
  Butuh riset produk + setting anti-bocor (LPV, mobile only, Reels/Story) + batas kill
  yang jelas. Tanpa itu, CPC murah sekalipun tetap boncos.
- **Jalur hibrida yang muncul di sini:** post organik dulu, video yang engagement-nya
  bagus baru diiklankan — disebut di beberapa thread sebagai cara paling hemat untuk
  memilih kreatif yang layak dibayar.
- **Shopee Affiliate Singapura sebagai varian ketiga:** bukan organik vs iklan, tapi
  pasar baru — affiliator lebih sedikit (klaim @inspirasiinside90, 11 Nov), tapi
  pendaftaran berliku — daftar via web lalu download aplikasinya; set lokasi Google
  Play/App Store ke Singapura; nomor HP Indonesia bisa dipakai; saat isi company
  name/partner type, pilih **Enterprise, bukan Individual**; target audiensnya Singapura.
  Persetujuan tidak mudah: ada yang ditolak berkali-kali padahal sudah upload video
  produk di beberapa sosmed. Penulisnya di hari ke-6 sedang mencoba apply pembayaran
  ke akun sendiri (@wanridwanarif, 25 Okt 2026).

**Kesalahan umum / jebakan di jalur organik:**

- **Spam link = akun melayang.** Sekali kena report spam karena spam link produk di
  Threads, akun bisa langsung hilang.
- **Jangan pakai share sesi/cookie ke tool orang lain.** Daftar Shopee Affiliate dulu
  supaya dapat API/link komisi resmi, jangan serahkan sesi ke tool pihak ketiga.
- **Ebook / prompt / strategi di balik paywall.** @vanthenextlevel (prompt AI),
  @ifralaryanto (strategi sinkron klik), @babanatabumi ("ANU") — semuanya mengarahkan
  ke DM/ebook. Ada pembeli yang mengeluh ebook tidak masuk setelah bayar.
- **Konten AI yang kentara.** Komentator @ziq7i: kalau sudah pakai [auto-reply/AI]
  kentara banget, ia pernah pakai lalu berhenti. Otomatisasi penuh tanpa sentuhan
  manusia berisiko terasa robotik dan dilaporkan spam.
- **Re-upload video China mentah:** pernah kena pelanggaran (PL) karena upload video
  anak kecil; akun sempat terdampak lalu pulih; kreator lain menyebut "aman asal tidak
  tampil screenshot, gerakan dinamis, ada model" — klaim tanpa dasar kebijakan
  [ANEKDOT — risiko tidak terkuantifikasi].
- **Konten AI tanpa label:** kreator mengonfirmasi konten AI **ditandai** platform;
  klaim "aman upload TikTok" hanya anekdot.
- **Jual kredit Flow murah** (tawaran "Flow AI 1000 kredit 18 bulan Rp50rb" di komentar)
  — pola jual-beli akun/kredit, risiko penipuan/pemblokiran.
- **Ternak akun / multi-akun** (@rijalaufaar: "punya 5 akun"; @lailahomedecor: "ternak
  akun") masih dipraktikkan sebagai mitigasi banned, bukan sebagai format kreatif.

**Angka lapangan (Shopee Affiliate umum) — semuanya anekdot:**

- Komisi Rp26.056.889 — @vanthenextlevel, 22 dan 24 Okt (dua postingan, angka yang
  sama). 3.267 likes di postingan 24 Okt, 679 repost. Tidak ada periode, GMV, jumlah
  order, atau spend di teks. **Klaim sepihak.**
- "Kekumpul 5jt cuma ajak teman belanja doang tanpa repot buat konten" — komentar
  @egoobyindonesia. Anekdot komentar, tanpa bukti.
- 740k views di postingan pertama — @hanifmuh_, 4 Feb (di luar 3 bulan): workflow
  Manus (wide research) → Claude (nulis post, setelah ditrain writing style) →
  Buffer (scheduling). Workflow-nya konkret, tapi usianya jauh di luar jendela.
- Tidak ada angka konsensus untuk CR / EPC organik di postingan 3 bulan terakhir ini —
  orang lebih banyak bicara views, likes, dan komisi total daripada rasio konversi.

## 11. Klaim angka besar — anekdot tanpa bukti, jangan jadikan patokan

Semua di bawah ini **[ANEKDOT tanpa bukti]** kecuali dinyatakan lain. Tidak ada satu pun
yang menyertakan dashboard Shopee (komisi tervalidasi) + dashboard Meta dalam satu bukti
yang bisa diverifikasi dari teks/angka yang terambil. Pola klaim: angka ekstrem selalu
muncul **tanpa denominator** (tanpa spend total, tanpa komisi tervalidasi, tanpa periode
ulang) dan sering berdekatan dengan penawaran kelas/jasa.

| Klaim | Sumber & tanggal | Status |
|---|---|---|
| ROAS 45× (leads) | @naffa.ard, 29 Okt 2026 | Tanpa bukti. Tanpa spend, tanpa nilai leads, tanpa konversi jadi penjualan |
| ROAS 16×, spend Rp947 jt, purchase value Rp15,4 M (1 Jan–4 Nov 2026) | @rizqriska, 4 Nov 2026 | Angka internal konsisten tapi tanpa bukti terverifikasi. **Bukan affiliate:** brand campaign e-commerce (ROAS GMV) |
| ROAS 100× dari spend Rp300rb-an | @angrheptro, 5 Okt 2026 | Tanpa bukti, sampel kecil |
| ROAS 102x CPAS 10.10 (spend Rp2,6 jt, purchase value Rp269 jt) | @rizqriska, Okt 2026 | Tanpa bukti, konteksnya brand CPAS, bukan affiliate |
| ROAS 11×/hari, "ads 600rb masuk 7 juta" | @salmasyneroa, 22 Nov 2026 | Tanpa bukti; ada konflik kepentingan — postingan menawarkan jasa handling Meta Ads |
| ROAS 4,49×, spend RM72.445, sales RM324.940, 7.576 purchases/bulan | @rusydi.rahman, 21 Sep 2026 (Malaysia) | Angka internal konsisten tapi tanpa bukti; fashion client Malaysia, ROAS GMV |
| ROAS 4,85× (struktur 1-1-3, 1 creative perform) | @scalewithabu, 6 Apr 2026 | Tanpa bukti angka dasar |
| ROAS 6,18x, 41.000+ penjualan (CPAS brand beauty, Feb–Apr 2024) | Studi kasus Omnicom | [FAKTA PIHAK KETIGA] — tapi ini brand CPAS, bukan affiliate |
| Sikat gigi elektrik: bln 1 spend 2jt/omzet 26jt/ROAS 8; bln 2 spend 5jt/71jt/ROAS 12; bln 3 spend 4jt/109jt/ROAS 23 | @se.arahtuju, 17 Sep 2026 | Tanpa screenshot |
| CPL Rp10rb, ~90% qualified, rumah Rp1–2M, belum sebulan jalan | @kikicandra_, 8 Nov 2026 | Tanpa bukti; penulis sendiri mengakui data closing belum ada. Kontras: @rudiiife — qualified wajib siap harga/budget; 100 leads isi form 11 field tapi belum siap budget dianggap low qualified |
| Penjualan Rp1,5jt, komisi "segitu", klik Meta–Shopee sinkron, PayDay 25 Nov | @ifralaryanto, 17 Nov 2026 | Angka komisi tidak disebut; detail strategi di ebook berbayar |
| CPC 3 perak (Meta Ads ke Shopee Affiliate) | @babanatabumi, 23 Nov 2026 | Tanpa bukti |
| CPC Rp7–10, target Rp0,xx; "pernah lihat ada yang CPC 0,5 perak" | @rudiiife, 23 Sep 2026 | Tanpa bukti. Yang "0,5 perak" explicitly "pernah lihat di utas lain" |
| CPC 0,02 (mata uang tidak jelas — kemungkinan RM) | @zul_azrii, 30 Jun 2026 | Tanpa bukti; klaim tangan kedua ("teknik yang dishare orang lain") |
| CPC Rp19 / Rp55 | Komentar @awalnur36 / @nableeee di @firmanalexramadani, Nov 2026 | Tanpa bukti (komentar, tanpa screenshot); dikoreksi komentator lain di thread yang sama |
| Modal Rp15jt (April) → muter Rp86jt (Juni) | @iqrmmm_, 1 Jul 2026 | Tanpa bukti profit. "Muterin modal" = perputaran/omzet, bukan laba; tanpa rincian spend, komisi, dan pajak |
| 22.000 klik → komisi Rp2,6jt | @mahbub165, 15–16 Okt 2026 | Sangat meragukan. Penulisnya sendiri mengakui data dari mentee dan "mungkin overclaim/palsu" |
| Spend Rp287rb, klik 9.700, komisi Rp812rb, profit | @slowlivingaff, 10 Mei 2026 | Anekdot + di luar rentang |
| Top-up Rp30rb, balik 5x modal | @yossie.sr, 22 Nov 2026 | Tanpa screenshot |
| Kelas Shopee Rp1,5jt → Rp22jt dalam 1 bulan | @nengwulan.id, 22 Nov 2026 | Tanpa bukti. Kontras dengan pengalaman penulis sendiri bahwa kebanyakan kelas lain "bodong" |
| Spend Rp20rb dapat "210 juta..." (satuan tidak jelas) | @trikaryati_, 22 Nov 2026 | Tanpa bukti, tidak dapat diverifikasi. Penulisnya sendiri di komentar bilang masih boncos, tidak pakai pixel, tidak pakai LP. Jangan dikutip sebagai revenue |
| Klik bocor 70%, cara di atas bikin klik 1,6x | @bennysoehardi, 17 Nov 2026 | Klaim pengalaman sendiri, tanpa screenshot perbandingan. Paling sering dirujuk, tapi tetap anekdot |
| Per 2.000 klik dapat Rp500rb, biaya iklan ~Rp350rb, sisa Rp150rb | @bennycell3039 (komentar), 26 Agu 2026 | Anekdot — tapi satu-satunya contoh dengan spend dan komisi sekaligus (EPC Rp250, CPC ~Rp175), jadi masih bisa dipakai sebagai ilustrasi, bukan patokan |
| CPM Rp2 jt / CPC Rp90rb | @syauqiy.ahmad.labyb, 13 Nov 2026 | Satire/lelucon, bukan klaim — tapi mengindikasikan ada niche yang memang semahal itu (kemungkinan B2B/properti) |
| Rumus harga: CR 50%, CPR Rp50rb → harga Rp118rb, laba Rp35rb | @rnsrmind, 8 Jan 2026 | Angka ilustratif, bukan hasil riset. Komentator @timkerjaai.id mengoreksi: CR 50% adalah angka ideal, di lapangan bisa jauh lebih rendah |
| "Meta minimal 7 hari" | @andrigunawan06 (komentar) | Meragukan, tidak dikonfirmasi sumber lain. Jangan dipakai sebagai aturan |
| Klaim AI: "paksa akun naik limit jadi ratusan juta" dan "iklan reject dipaksa aktif" | @devildata (komentar, 24 Okt) | Klaim sepihak, berisiko melanggar kebijakan — jangan direkomendasikan |
| Viral 120K views dari "bikin hook doang" | @kontenhustle, 30 Okt 2025 | Tidak ada bukti kausal bahwa hook-nya saja yang menyebabkan viral |

**Yang relatif lebih kredibel:** aturan berbasis mekanisme Meta yang dikonfirmasi beberapa
orang sekaligus (overspend harian maks 175%, rata-rata mingguan tetap; learning phase
hari-1 volatil; EMQ/CAPI penting) dan praktik testing 1-1-5 / 3 hari yang diulang di lebih
dari satu utas. Angka yang paling kredibel justru yang paling "membosankan": ROAS 1,2 di
hari ke-3 (@bin_sugiyanto), CPC Rp150 dengan rasio masuk bagus (@nur_hikam), scale 20%
(@rahmatmajeed).

**Angka lapangan Meta Ads umum (anekdot):** Testing budget Rp35–50rb sudah cukup —
@hudayat_h (komentar, 31 Okt). CPL Rp10rb untuk properti harga Rp1–2 miliar, ~90%
leads qualified, dalam <1 bulan — @kikicandra_, 8 Nov 2026 (screenshot ada tapi tidak
terbaca dari teks). CPL stabil ~Rp15rb untuk properti Rp300–800jt, belasan survey,
closing 3 — @yasqirachmadhani (komentar, 9 Nov). Visit rate 20–30% dari leads —
@joenasammy (komentar, 9 Nov). Budget habis sangat cepat di awal — @bukankoding,
23 Sep 2026: topup Rp100rb, budget Rp50rb/hari, iklan jalan 14.00, pukul 14.19 sudah
kepakai banyak.

**Definisi qualified lead (properti) — bertentangan:** @kikicandra_ — yang minat dan
tanya lebih dalam itu qualified, beli atau tidak itu KPI sales; @rudiiife — qualified
wajib siap harga/budget, 100 leads isi form 11 field tapi loss karena belum siap budget
dihitung low qualified oleh sales. **Google Ads vs Meta Ads:** @masaridigital, 26 Jun
2025 — Google Ads disebut lebih gurih dan tidak "roller coaster" biaya seperti Meta;
ini satu-satunya suara pro-Google yang muncul, tanpa angka pembanding.

## 12. Taktik yang SUDAH MATI / berbahaya — jangan dipakai lagi

1. **Direct link massal kejar klik demi indirect order (klik banyak, order kecil)** —
   mati ~2025. Akun ditutup Shopee; Shopee curiga klik banyak tapi order kecil
   [ANEKDOT @origin2market].
2. **Objektif Link Clicks / Max Clicks, bangga CPC murah (terutama FB)** — mati 2026.
   CPC murah FB tidak sampai ke Shopee; >600 klik Meta vs 61 di Shopee [ANEKDOT];
   "max click kurang oke" [ANEKDOT, komentar @bennysoehardi].
3. **Advantage+ / semua placement (FB Feed murah mendominasi)** — mati 2026 sebagai
   default. Discrepancy terbesar dari placement FB; diganti manual IG-only [ANEKDOT].
   **Catatan:** ada anekdot berlawanan — @nengwulan.id klaim FB Feed+Reels discrepancy
   hanya 2–5% dengan CPC Rp150, sementara IG CPC <Rp50 tapi "bocor alus". Perdebatan
   placement belum selesai.
4. **Interest stack sempit + banyak ad set (hyper-targeting)** — mati: opsi
   dihapus/diperluas jadi suggestion; audiens kecil kehabisan reach, frekuensi meledak
   [RESMI + ANEKDOT].
5. **Lookalike standalone sebagai strategi utama** — mati perlahan: logikanya dilipat
   ke Advantage+ Audience [SEKUNDER].
6. **PPE / engagement bait sebagai jalan murah ke penjualan** — mati sebagai strategi
   performa; hanya social proof [ANEKDOT].
7. **Pixel-only tanpa CAPI** — berbahaya: kehilangan atribusi besar pasca-ATT; EMQ
   rendah = optimasi buta [RESMI/SEKUNDER].
8. **Campur image + Reels/video dalam 1 ad set CBO** — berbahaya: Meta menyerot budget
   ke format engagement tertinggi (Reels), format termurah bisa 0 spend. Pisah ad set
   per format [ANEKDOT, terdokumentasi dengan angka Rp140rb vs Rp68rb/lead].
9. **Optimasi Purchase padahal volume tidak mungkin capai 50/minggu, lalu memaksa** —
   berbahaya: terjebak Learning Limited selamanya; lapangan menurunkan ke ATC +
   retargeting terpisah [ANEKDOT].
10. **Otak-atik/edit iklan saat learning phase & scale >20% sekaligus** — berbahaya:
    me-reset learning; skala bertahap 20%/3 hari adalah norma lapangan [ANEKDOT;
    aturan 20%-reset adalah MITOS — Meta tidak pernah menerbitkannya].
11. **Mengandalkan "tombol/struktur magic"** — mati: tidak ada struktur yang
    menyelamatkan kreatif & LP yang buruk [ANEKDOT, konsensus].
12. **Bikin akun/BM baru untuk lolos dari restriksi; re-run iklan ditolak dengan edit
    minor** — berbahaya: memicu risk-score & policy score; jalur benar lewat Account
    Quality + appeal terdokumentasi [ANEKDOT + SEKUNDER].
13. **Menganggap daily budget sebagai cap harian keras** — salah kaprah: Meta resmi
    boleh 175%/hari (210% dengan budget sharing), 7x/minggu. Tanpa campaign/account
    spending limit atau lifetime budget, tidak ada hard cap harian [RESMI].
14. **Atribusi view 28-hari / 7-hari view sebagai dasar keputusan** — mati: jendela
    view tersebut dihapus 12 Jan 2026 [SEKUNDER].
15. **CPAS via form Google + tunggu 14 hari** — mati Sep 2026: diganti Collaboration
    Center / Seller Centre Iklan Eksternal ~15 menit [ANEKDOT @liemptr + komentar].
16. **Mengandalkan komisi dasar tinggi era lama (10–20%)** — mati Sep 2025: skema baru
    1,5%/0,5% cap Rp10.000 [RESMI]; elektronik makin turun Okt 2026 [ANEKDOT].
17. **Clickbait (iklan ≠ produk di link), konten curian, beli lewat link sendiri,
    spam link** — selalu dilarang; penegakan terasa 2025–2026. S&K 6.2(d)/(f), 6.3(n)
    [RESMI]; komisi tidak valid / akun dibekukan.
18. **Jual-beli/sewa akun (Shopee Partner, akun Meta/whitelist) untuk scale** — muncul
    2026, berisiko. Praktik terlihat di komentar @iqrmmm_ (WTS akun Partner, Nov 2026);
    tidak ada bukti aturan yang mengesahkannya — flag sebagai risiko, bukan taktik.
19. **Re-upload video China mentah / konten AI tanpa label / jual kredit Flow murah** —
    berisiko PL, penandaan platform, penipuan/pemblokiran [ANEKDOT].
20. **Klaim AI: "paksa akun naik limit jadi ratusan juta" dan "iklan reject dipaksa
    aktif"** — @devildata. Klaim sepihak, berisiko melanggar kebijakan.
21. **"Meta minimal 7 hari"** — @andrigunawan06. Meragukan, tidak dikonfirmasi sumber
    lain. Jangan dipakai sebagai aturan.
22. **Babanatabumi "ANU" (13 Nov 2026):** klaim "EZ, kasih ANU, setting ANU, DUAAAR" —
    251 likes, 161 balasan — tapi setting-nya tidak pernah dibuka di publik, semua
    diarahkan ke DM. Ini pola bait, bukan tutorial.
    https://www.threads.com/@babanatabumi/post/DfrbExygH2F

## 13. Rencana aksi paling efisien — budget kecil Rp20–50rb/hari (diperbarui pelajaran 3 tahun)

Prinsip: **di budget kecil, yang dibeli bukan order — yang dibeli adalah data rasio
masuk dan CR.** Order adalah efek samping.

### Hari 0 — Sebelum spend Rp1 pun (gratis)
1. Skor produk dengan Winning Product Scorecard (skill). Skor <70 → jangan iklan
   tunggal; <50 → ganti produk. Prioritas Komisi XTRA ≥10% atau komisi bersih
   ≥Rp10.000/order.
2. Hitung komisi bersih **dengan cap [RESMI Sep 2025]**: komisi = min(harga × 1,5%,
   Rp10.000) + (harga × % XTRA), lalu × (1 − 0,025) untuk PPh efektif bracket bawah.
   Tolak produk elektronik (0,5%) dan produk tanpa XTRA kecuali XTRA-nya besar.
   Cek ulang % XTRA tiap minggu.
3. Hitung 3 angka wajib dengan **rumus koreksi rasio masuk**: Max CPC Meta = komisi
   bersih × CR asumsi 1% × rasio masuk asumsi 30% × 0,70 / 1,11; Target Max CPC Profit
   dan pesanan valid untuk impas dengan simulator skill. **Bila Max CPC hasilnya
   <Rp20, produk itu tidak layak diiklan di budget kecil — cari produk lain, jangan
   paksakan CPC.** Contoh komisi Rp15.795 (vacuum mini): Break-Even CPC Rp316, Target
   Rp199 (rumus lama, tanpa rasio masuk) — dengan rasio masuk 30%, Max CPC Meta yang
   sebenarnya jauh lebih rendah; hitung ulang dengan rumus koreksi sebelum launch.
4. Riset Ads Library: cari 5 brand se-target market, catat iklan yang aktif 30–60+
   hari, ATM hook/formatnya. Jangan buat kreatif dari nol tanpa referensi ini.
5. Siapkan 5 variasi kreatif (struktur 1-1-5): 2–3 angle berbeda, video 15–25 detik
   9:16 (atau 10 detik UGC problem-solution VO Indonesia), hook 3 detik + filter harga
   di baris pertama. Validasi organik dulu kalau bisa (Fase 0 skill) — gratis.
6. Generate deep link dengan benar: browser → affiliate.shopee.co.id → Generate Link
   → centang "Buka di Aplikasi / App Deep Link" (link jadi `shopee://`); isi SubID
   lewat form Custom Link (sub_id1 produk, sub_id2 funnel+tanggal, sub_id3 ad set,
   sub_id4 kreatif — huruf+angka, tanpa spasi). Jangan bungkus dengan shortener lain.
   Uji dari HP sendiri: klik preview iklan di aplikasi FB/IG, harus langsung pindah
   ke aplikasi Shopee, bukan login di browser. Pastikan dashboard Shopee bisa
   menampilkan klik (bukan hanya klik Meta).
7. Cek higiene: metode pembayaran aktif (kartu tidak expired), Page niche (bukan FB
   Pro, bukan impersonasi Shopee), pengungkapan afiliasi sudah disiapkan.

### Hari 1 — Launch Rp35–50rb (1 campaign, 1 ad set, 5 kreatif, CBO — mengikuti
@hudayat_h; alternatif ABO 1-2-2 kalau mau pisah hook; bila hanya ada Rp20rb/hari,
jalankan 1 ad set saja, jangan pecah)
8. Setting anti-bocor: Performance goal Landing Page View, device mobile only,
   placement **FB Feed dulu** (bukti lapangan: selisih klik 2–5% vs IG Reels yang
   bocor) — uji IG Reels & Story hanya sebagai ad set terpisah, jangan dicentang semua
   sekaligus; Indonesia only, matikan Audience Network dan desktop.
9. Schedule mulai **00.01** keesokan hari (bukan siang hari). Pakai **lifetime budget
   atau account spending limit** sebagai hard cap — Meta bisa spend sampai 175%
   budget harian.
10. Pasang Automated Rules skill sebelum launch (dengan koreksi ambang kill §8):
    Auto-Kill Hook (spend ≥Rp20rb AND Outbound CTR <1,0% — kill dini saja), Auto-Kill
    CPC berbasis **CPC efektif per klik Shopee** (CPC ÷ rasio masuk) > Max CPC koreksi
    +15% setelah spend ≥Rp50rb / 100 klik Shopee, Auto-Alert Pemenang (spend ≥Rp30rb
    AND CPC ≤ Target Max CPC Profit AND Outbound CTR ≥2,5% — notifikasi saja).
11. Comment seeding segera setelah Active: 1 komentar pertama + pin, jawab cepat
    pertanyaan soal ukuran/bahan/keaslian.

### Hari 1–3 — Testing, jangan sentuh budget
12. Jangan nilai dari CPC/klik/ROAS dashboard. Hitung tiap hari: rasio klik masuk
    (klik Shopee ÷ klik keluar Meta — target ≥80% di FB Feed; IG Reels 30–50% adalah
    kenyataan lapangan), LPV Ratio, CR, EPC **per klik Meta** vs CPC.
13. Kill cepat (tanpa feeling, pakai angka): Outbound CTR <1,0% setelah spend Rp20rb
    → kill kreatif itu (kill dini); CPC efektif per klik Shopee > Max CPC koreksi +15%
    setelah spend ≥Rp50rb → kill; rasio masuk <30% setelah 100+ klik → pause,
    perbaiki deep link/placement dulu, bukan ganti kreatif; **jangan** pakai aturan
    "3× harga produk" atau "CPC harus <Rp20".
14. Jangan panik hari pertama: learning phase volatil, dashboard Meta bisa tidak
    sinkron dengan pemasukan riil — cross-check ke Laporan Performa/Komisi Shopee
    sebelum mematikan iklan yang CTR-nya tinggi dan CPC-nya murah. Tunggu validasi H+1.
15. Kalau dari 5 kreatif hanya 1–2 yang dapat spend: ada closing → lanjutkan; tidak
    ada closing → kill supaya budget pindah ke ads lain.

### Hari 4–7 — Validasi
16. Lanjutkan hanya ad set dengan rasio masuk ≥50% dan CPC efektif per klik Shopee
    di bawah Break-Even CPC. Target: minimal 100 klik Shopee terkumpul sebelum menilai CR.
17. Rekonsiliasi per sub_id (H+1/H+2): cocokkan komisi per sub_id4 dengan Amount Spent
    × 1,11 di Ad terkait. Hitung EPC = komisi tervalidasi ÷ klik keluar Meta.
18. Keputusan: EPC < CPC → **KILL** (boncos), jangan scale. EPC 1,0–1,4× CPC →
    **OPTIMASI** (perbaiki LPV/CR dulu, jangan tambah budget). EPC ≥1,5× CPC DAN Net
    ROAS ≥1,8x → **SCALE**. Kalau CR >5% tapi EPC masih <1,5× CPC, masalahnya di CPC
    — turunkan CPC atau ganti produk, bukan scale.
19. Kill bila: total spend ≥Rp150–200rb dan 0 order, atau EPC per klik Meta < CPC × 1,0
    selama 2 hari berturut-turut setelah 100 klik Shopee.
20. Kalau tidak ada satu pun kreatif yang lolos: jangan ulangi dengan produk yang sama
    dan budget lebih besar. Ganti produk (skor ulang) atau ganti angle/hook — dan cek
    lagi apakah bocornya di funnel (LPV <75% di FB Feed) atau di Shopee (CR <1,5%,
    price shock, stok/varian, ulasan toko).

### Scale — hanya kalau lolos Hari 7, dan bertahap
21. Pindahkan winner ke CBO, scale **+20% tiap 24–48 jam** (@rahmatmajeed — satu-satunya
    angka scale yang bertahan). Jangan duplikasi besar-besaran; bila performa drop saat
    scale (@hudayat_h), kembalikan ke budget sebelumnya, jangan matikan campaign.
22. Horizontal: kumpulkan 2–3 pemenang dengan Post ID yang sama ke CBO baru, budget
    awal 2–3× budget testing harian.
23. Retargeting 10–15% budget: pengunjung Bridge Page 14 hari + Video Viewers 50%
    14 hari. Syarat scale penuh: Net ROAS ≥1,8x selama 2–3 hari berturut-turut (sinyal
    awal) — untuk scale besar, tunggu 7 hari berturut-turut tidak bocor dan komisi
    tervalidasi di dashboard Shopee (bukan klik) menutup spend + PPN 11%. Ingat [RESMI]:
    komisi dihitung dari pesanan selesai dalam 7 hari setelah klik — jangan klaim profit
    sebelum jendela 7 hari tertutup.
24. Kalender: tahan budget 20–30% di tanggal tua 15–23; agresifkan di Payday 25–3 dan
    Tanggal Kembar (mulai H-2). Prioritaskan jam 07.00–09.00, 11.30–13.30, 19.00–22.30 WIB.
25. Rotasi kreatif sebelum fatigue: Frequency >2,5–3,0 atau foto/video yang sama sudah
    jalan berminggu-minggu → ganti hook/angle (variasi, tidak wajib video). Cek Ads
    Library lagi untuk angle baru.

**Checklist harian (2 menit):** rasio masuk ≥80% (FB Feed)? LPV ≥75%? EPC per klik
Meta ≥ CPC? Biaya per order ≤ untung kotor per order? Kalau ada satu yang tidak —
jangan scale, perbaiki titik bocornya dulu sesuai matriks diagnosis skill (CPM →
Broad/native; Hook <25% → ganti 3 detik awal; Outbound CTR <1,5% → perjelas CTA;
LPV <75% → matikan Audience Network/kompres halaman; CR <1,5% → harga di iklan,
deep link, audit halaman Shopee).

**Yang tidak boleh dilakukan (diulang tiap tahun):** mengejar CPC <Rp20–100 sebagai
target; menilai dari screenshot ROAS orang lain; scale karena 1 hari bagus; beriklan
produk tanpa XTRA; mengabaikan PPN 11% dan cap Rp10.000 dalam hitungan; menaikkan
budget besar sekaligus; menilai konversi Shopee secara real-time di jam pertama.

## 14. Postingan kunci gabungan

1. @bennysoehardi — 17 Nov 2026 — https://www.threads.com/@bennysoehardi/post/Df0_INpn-QD — Klik bocor 70%; LPV + mobile only + IG Reels/Story, klaim klik 1,6x. [ANEKDOT]
2. @origin2market — 13 Mei 2026 — https://www.threads.com/@origin2market/post/DYSKU9ME7ge — >600 klik Meta vs 61 klik Shopee, 1 order; akun affiliate dulu ditutup karena direct link. [ANEKDOT]
3. @hudayat_h — 31 Okt 2026 — https://www.threads.com/@hudayat_h/post/DfJXoMtEiMj — Struktur 1-1-5 era Andromeda; budget testing Rp35–50rb/hari, CBO. [ANEKDOT]
4. @haritst26 — 30 Jul 2026 — https://www.threads.com/@haritst26/post/DbaLIaGoPKu — Meta Ads dulu vs sekarang; kontras pra/pasca-Andromeda paling jernih. [ANEKDOT]
5. @adsbywhd — 16 Nov 2026 — https://www.threads.com/@adsbywhd/post/DfxTdvcEsTo — Berhenti cari struktur magic; skill yang dibutuhkan kini kreatif, landing page, baca data. [ANEKDOT]
6. @bin_sugiyanto — 28 Jun 2026 — https://www.threads.com/@bin_sugiyanto/post/DaHYpqYFs66 — Scale CBO, testing ABO; tiap ad set beda format; evaluasi 3 hari. [ANEKDOT]
7. @ejjaarf — 21 Nov 2026 — https://www.threads.com/@ejjaarf/post/Df__9lAnRXB — Learning phase: 50 konversi/minggu; keluar learning ≠ CPA stabil. [ANEKDOT; angka 50 selaras RESMI]
8. @ianfatah — 29 Okt 2026 — https://www.threads.com/@ianfatah/post/DfEKo45ARXt — Jangan gabung image dan Reels di 1 ad set (Reels Rp140rb/lead vs image Rp68rb/lead, image 0 spend). [ANEKDOT]
9. @saddamsaness — 5 Agu 2026 — https://www.threads.com/@saddamsaness/post/Dbo2ZJyk3WP — Cara menemukan produk komisi besar tanpa menebak-nebak; 90 pesanan = Rp478,4rb komisi (klaim). [ANEKDOT]
10. @rijalaufaar — 5 Nov 2026 — https://www.threads.com/@rijalaufaar/post/DfWVKfoErlm — Tutorial affiliate pakai Google Flow; 3.563 likes, 739 repost. [ANEKDOT]
11. @liemptr — 22 Sep 2026 — https://www.threads.com/@liemptr/post/DdmAGbVktuT — CPAS kini via Collaboration Center ~15 menit, tanpa form/14 hari. [ANEKDOT]
12. @gregory.purba — 11 Mei 2026 — https://www.threads.com/@gregory.purba/post/DYMkaPCE9OO — CPC <Rp100, CTR >5%, closing <1%, tetap boncos; "CPC/traffic murah ≠ profit". [ANEKDOT]
13. @dreaminahome.studio — 26 Agu 2026 — https://www.threads.com/@dreaminahome.studio/post/Dcfoj0jlJE6 — Gelombang boost-post IG Agu 2026; 1.100 klik/Rp85rb, masih boncos, berharap cookie 7 hari. [ANEKDOT]
14. @iqrmmm_ — 1 Jul 2026 — https://www.threads.com/@iqrmmm_/post/DaPhUgZGT90 — Klaim modal Rp15 jt (Apr) muter jadi Rp86 jt (Jun); nilai risetnya justru di komentar (afiliator lain 4 bulan boncos). [ANEKDOT]
15. @labibhusn_ — 30 Okt 2026 — https://www.threads.com/@labibhusn_/post/DfH95IGnTrn — Ekstensi riset produk Shopee; **koreksi: toolnya Risetika, bukan SENA**. [ANEKDOT/Fakta]
16. @tips.omcharlie — 10 Nov 2026 — https://www.threads.com/@tips.omcharlie/post/DfjqzXvHStW — Bridge Page untuk 5 platform; link mentah = spam. [ANEKDOT]
17. @para_malinda — 7 Feb 2025 — https://www.threads.com/@para_malinda/post/DFxcU0Myvmh — Satu-satunya bukti 2025: LP = halaman yang **disediakan Shopee** (Festival Kreator). [ANEKDOT]
18. @haryono_pro — 8 Okt 2026 — https://www.threads.com/@haryono_pro/post/DeN0HRqk57M — Resep prompt Google Flow untuk produk affiliate; 10 detik, VO Indonesia. [ANEKDOT]
19. @kontenhustle — 30 Okt 2025 — https://www.threads.com/@kontenhustle/post/DQbxG7uE0sj — 5 prompt ChatGPT untuk bikin hook, klaim viral 120K views. [ANEKDOT]
20. @armansatrio — 13 Sep 2026 — https://www.threads.com/@armansatrio/post/DdOkvm7gZbm — Pemutaran Video 3 Detik sebagai metrik evaluasi hook; contoh iklan 42.641 pemutaran 3 detik, CTR 5,04%, CPC Rp43. [ANEKDOT]
21. @dualipatdigital — 11 Okt 2026 — https://www.threads.com/@dualipatdigital/post/DeVjPhDAUNE — Andromeda: hook 3 detik pertama adalah salah satu dari 3 hal yang membuat iklan dibaca "beda". [ANEKDOT]
22. @rivaldiekaptr — 22 Nov 2026 — https://www.threads.com/@rivaldiekaptr/post/DgBud5KGaiN — Hook dari 26 formula + skor (instagram-agent-skill, trending GitHub). [ANEKDOT]
23. @natasyaph_ — 27 Jul 2026 — https://www.threads.com/@natasyaph_/post/DbSfEREiUQ2 — Offer vs landing page vs budget; pilih 1 level awareness dulu. [ANEKDOT]
24. @vanthenextlevel — 24 Okt 2026 — https://www.threads.com/@vanthenextlevel/post/De4GIOSkwD1 — Komisi Rp26.056.889 + bongkar prompt AI. [ANEKDOT]
25. @sudutsamar — 13 Okt 2026 — https://www.threads.com/@sudutsamar/post/Dea1b-Pk0qF — Ekstensi Chrome SENA untuk riset produk Shopee. [ANEKDOT]
26. @wanridwanarif — 25 Okt 2026 — https://www.threads.com/@wanridwanarif/post/De62KXZj2nU — Shopee Affiliate Singapura, hari ke-6, apply pembayaran. [ANEKDOT]
27. @_anhalim — 12 Nov 2026 — https://www.threads.com/@_anhalim/post/DfoQBO6E-YB — AI untuk affiliate Threads x Shopee (Day 1). [ANEKDOT]
28. @ifralaryanto — 17 Nov 2026 — https://www.threads.com/@ifralaryanto/post/Df0u12JATyC — Shopee x Meta Ads "gacor", penjualan Rp1,5jt, klik sinkron, PayDay 25 Nov. [ANEKDOT]
29. @scalewithmirza — 10 Okt 2026 — https://www.threads.com/@scalewithmirza/post/DeUKcvvmJCp — Tracking manual dengan EMQ bagus. [ANEKDOT]
30. @bukankoding — 23 Sep 2026 — https://www.threads.com/@bukankoding/post/DdoZAZaAZ3M — Top-up Rp100rb, budget Rp50rb/hari, tersedot dalam 19 menit. [ANEKDOT]
31. @kikicandra_ — 8 Nov 2026 — https://www.threads.com/@kikicandra_/post/DfecwlIGDjq — Properti: CPL Rp10rb, ~90% qualified, rumah Rp1–2M. [ANEKDOT]
32. @chandrapropertyads — 24 Okt 2026 — https://www.threads.com/@chandrapropertyads/post/De3N1AXGDTm — Cara paksa buka manual placement via Meta AI. [ANEKDOT]
33. @trikaryati_ — 22 Nov 2026 — https://www.threads.com/@trikaryati_/post/DgBsROmj8z7 — Spend Rp20rb, "210 juta..." (satuan tidak terverifikasi), penulis mengaku masih boncos. [ANEKDOT]
34. @salmasyneroa — 22 Nov 2026 — https://www.threads.com/@salmasyneroa/post/DgBwnDCEzNC — Klaim ROAS 11x, spend Rp600rb masuk Rp7jt (tawaran jasa). [ANEKDOT]
35. @babanatabumi — 13 Nov 2026 — https://www.threads.com/@babanatabumi/post/DfrbExygH2F — "Meta Ads x Shopee Affiliate? EZ" — setting "ANU" tidak pernah dibuka di publik. [ANEKDOT]
36. @armansatrio — 26 Agu 2026 — TOFU → MOFU → BOFU, funnel bertahap (detail di gambar, tidak terbaca sebagai teks). [ANEKDOT]
37. @m.albardan — 26 Okt 2026 — https://www.threads.com/@m.albardan/post/De8QAtJmUfB — B2B skincare, CTR 2% tapi qualified leads di bawah 30–50%. [ANEKDOT]
38. @muhamadarifin775 — 23 Nov 2026 — https://www.threads.com/share/BADsdqv5Q0 — Pemula gagal karena "sok tau": skip riset produk & konsistensi, mau 1 video langsung viral; klaim komisi Rp18.901.219 dari video-video sepele, bukan 1 video viral — tanpa periode/GMV/jumlah order, screenshot komisi tidak terbaca, dan postingan adalah lead magnet ke channel penulis. Komentar: masalah nyata pemula adalah distribusi, ~10 views/video; pertanyaan tak terjawab: 5 produk × banyak versi vs 50 produk × 1 video. Pelajaran valid dan sejalan dengan pendekatan skill (5 variasi hook dari 1 produk), angka jangan jadi patokan. [ANEKDOT]
39. @novitasriiiil — 24 Nov 2026 — https://www.threads.com/share/BBcJVqEEmF — "Reply marketing": datangi utas ramai yang orangnya lagi cari rekomendasi, reply dengan value dulu (pengalaman + kekurangan kecil), link hanya kalau diminta; target 6–10 reply berkualitas per sesi. Klaim 8.200 klik, 287 order, komisi Rp1 jt dalam sehari — tidak terverifikasi (CR 3,5%, ~Rp3.500/order, produk kemungkinan murah); akun kecil (309 followers, 0 likes), postingan berujung funnel ebook gratis. Jawaban atas masalah distribusi di #38: kalau utas sendiri sepi, datangi permintaan yang sudah ada. Cocok untuk produk yang sedang diincar (vacuum mini, moisturizer, sunscreen) — reply di utas yang menanyakan rekomendasi. Risiko spam kalau asal tempel link di utas orang. [ANEKDOT]
40. @umarhy.serbadigital — 25 Nov 2026 — https://www.threads.com/@umarhy.serbadigital/post/DgMFYK0j7GM — "Rahasia iklan produk keren: bukan prompt panjang, tapi kode singkat" — ChatGPT + foto produk: /commercialad /heroproduct /superrealistic /storyboard image; Google Flow + storyboard: /premiumcommercial /cinematiclighting /brandheroshot /ultraphotorealistic /talkingahead /voiceover bahasa indonesia /cta ending. 59 likes, 1 komentar ("Back kk"), tidak ada yang melaporkan hasil; carousel tidak terbaca via CLI sehingga kualitas hasil yang diklaim tidak terverifikasi. "Kode" ini BUKAN perintah resmi Flow/ChatGPT yang terverifikasi — perlakukan sebagai bahan prompt ringkas (style block): premium commercial + cinematic lighting + brand hero shot + ultra photorealistic + talking head + VO Indonesia + CTA ending, ditempel di atas prompt detail storyboard yang sudah ada (bukan penggantinya). Pelengkap #18 (@haryono_pro, resep prompt Flow 10 detik VO Indonesia). [ANEKDOT]
41. @arnoldalvaro — 26 Nov 2026 — https://www.threads.com/@arnoldalvaro/post/DgNPzLDD3eJ — Template prompt storyboard sinematik lengkap (teks penuh ada di caption + rantai komentar penulis sendiri): "CHOCOLATE LAVA CAKE — VOLCANIC ERUPTION", 9:16, 15 dtk, 8 scene. Yang bisa ditiru: (1) layout sheet — satu lembar vertikal 2×4, background hitam, nomor scene merah, judul putih, timecode persis, keyframe fotorealistik, shotlist teknis ringkas, sketsa gerak grayscale + panah arah; (2) mechanic build-up and release — ketegangan naik (collision → meltdown → vortex → chamber → pressure rising → fault line) lalu lepas (eruption → aftermath); (3) continuity lock — progresi state ketat (solid → fragments → melted → batter → baked → opened → flowing → hero), jaga geometri produk & properti, tanpa reset state; (4) negative prompt eksplisit — tanpa manusia/tangan/dialog, tanpa duplikasi produk, tanpa panel ekstra; (5) sound cue per scene (ASMR, perkusi naik, bass impact, near silence). Dibuat dengan Dreamina AI (tag #dreaminaCPP — konten kemitraan, promosional). Catatan: hanya 10 likes dari 74.190 followers, tidak ada yang melaporkan hasil, sheet hasil di carousel tidak terbaca via CLI sehingga kualitas output tidak terverifikasi; contohnya makanan, bukan skincare — perlu adaptasi progresi state (mis. Renew: cleanser → serum → moisturizer → glowing, atau 7 produk dirakit jadi set). [ANEKDOT]

## 15. Yang belum terverifikasi — jangan klaim sebagai fakta

- CR deep-link / Bridge Page 1,5–3% dan CR retargeting / payday 3,5–6%+ — tidak ada
  satu pun postingan yang mengukur CR deep-link atau retargeting secara terpisah.
- Hook Rate ≥25% (sebagai ambang skill) — cocok dengan baseline web Billo/AdLibrary,
  tapi tidak muncul di korpus Threads 2024–2026 ini.
- Frequency <2,5 — tidak ada satu pun postingan/komentar yang menyebut frequency.
- Ambang scale ROAS komisi 1,8–2,5× — belum terverifikasi untuk affiliate.
- Sweet spot harga Scorecard Rp45–250rb — tidak dikonfirmasi maupun dibantah.
- Landing pre-sell per-section / Clarity / message match — tidak ada bukti Threads.
- Stack CAPI terbaik untuk CTWA/LPWA Indonesia — belum terjawab di Threads.
- Deep link langkah-demi-langkah dan UTM template — sumbernya jawaban AI @meta.ai;
  perlu verifikasi ke Help Center Shopee sebelum dijadikan instruksi resmi.
- Bila butuh bukti kontemporer 2023–2025, perlu sumber lain (arsip blog/YouTube/grup
  FB lama), bukan Threads search.
