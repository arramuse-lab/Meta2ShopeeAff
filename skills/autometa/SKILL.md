---
name: autometa
description: Kelola Meta Ads otomatis untuk Shopee Affiliate: monitoring berkala, diagnosis EPC vs CPC, auto-kill stop-loss (Automated Rules di Ads Manager ditambah loop monitor), alert pemenang, dan scaling. Pakai saat user minta iklan dijaga otomatis supaya tidak boncos, dipantau tiap 30 menit, atau dimatikan sendiri saat lewat batas spend tanpa order.
---

# AutoMeta

Skill ini menjaga campaign Meta Ads Shopee Affiliate supaya tidak boncos tanpa harus menatap layar terus. Dua lapis pengaman: Automated Rules di Ads Manager yang mematikan iklan secara native, dan loop monitor berkala yang membaca metrik, memberi vonis, dan pause ad set yang kena kill rule.

Skill ini disarikan dari `meta-ads-shopee-affiliate-pro` Step 5 dan Template Automated Rules, ditambah spesifikasi loop monitor yang sudah jalan live untuk campaign Glad2Glow Super Renew (26-28 Nov 2026). Bukan skill baru yang terpisah dari logika itu; ini versi fokusnya, khusus otomatisasi.

## Batasan yang harus dipegang

- Akun iklan Muse bersifat read-only (Ads MCP write dinonaktifkan Meta). Muse tidak bisa pause atau edit iklan lewat API. Pause dilakukan lewat browser di Ads Manager. Yang mematikan iklan secara native dan otomatis adalah Automated Rules Meta sendiri, bukan Muse.
- Jangan pernah menyatakan profit hanya dari metrik Meta. Komisi Shopee lag H+1. Nilai dini hanya dari metrik hulu (spend, CPC, CTR, rasio masuk).
- Yang boleh diubah otomatis: pause (matikan switch) ad set yang kena kill rule, lalu verifikasi perubahannya.
- Yang dilarang: menaikkan budget, mengubah kreatif, targeting, URL, atau tanggal, menghapus apa pun, membuat campaign baru.

## Alur kerja

### Langkah 0: Siapkan angka dasar sebelum launch

Hitung dulu dari harga produk, persen komisi dasar, persen XTRA, dan PPh. Rumus lengkap ada di `references/rumus-ringkas.md`. Yang wajib ada sebelum iklan jalan:

- Komisi bersih per order.
- Max CPC aman (Target Max CPC Profit) dan Max CPC koreksi (batas kill).
- Rasio masuk (klik Shopee dibagi klik keluar Meta) per placement. Patokan lapangan: FB Feed 95-98 persen, IG Reels 30-50 persen.
- Persen XTRA wajib dicek di dashboard affiliate sebelum launch dan dicek ulang tiap minggu (proteksi penurunan hanya 7 hari).

Tanpa angka ini, semua aturan otomatis di bawah tidak bisa dipasang dengan benar.

### Langkah 1: Pasang Automated Rules di Ads Manager

Pasang empat aturan dari `references/automated-rules.md` sebelum launch, di level Ad atau Ad Set:

1. Auto-Kill Kreatif Gagal Hook (cut loss dini, berbasis CTR).
2. Auto-Kill CPC Kemahalan (pelindung margin, berbasis CPC efektif).
3. Auto-Kill Final (spend besar, 0 order).
4. Auto-Alert Pemenang (notifikasi saja, jangan auto-increase).

Jangan pasang auto-increase budget tanpa cek komisi Shopee H+1.

### Langkah 2: Loop monitor berkala

Jalankan loop tiap 30 menit selama campaign aktif. Spesifikasi lengkap ada di `references/monitor-loop.md`. Tiap run:

1. Baca metrik per ad set: spend, impressions, outbound clicks, CPC, outbound CTR, LPV ratio. Pakai pembacaan API/CLI bila tersedia; browser hanya bila perlu edit atau bila pembacaan API gagal.
2. Hitung biaya riil = spend x 1,11 (PPN). Hitung CPC efektif per klik Shopee = CPC dibagi rasio masuk.
3. Terapkan kill rule dan beri vonis AMAN, WASPADA, atau KILL.
4. Bila kena kill rule, pause ad set itu dan verifikasi perubahannya.
5. Catat tiap run (jam, angka per ad set, keputusan) ke file log.
6. Kirim laporan singkat tiap run (maks sekitar 5 baris): jam cek, total spend sejauh ini, angka per ad set, vonis, dan tindakan yang diambil.

Bila campaign belum Active atau delivering di run-run awal (masih In review atau Scheduled), laporkan singkat begitu dan terus cek; jangan edit.

### Langkah 3: Vonis kill atau scale

Pakai ambang yang sama di kedua basis (per klik Meta dan per klik Shopee):

- PROFIT / SCALE: EPC >= CPC aktual x 1,5.
- BREAKEVEN / OPTIMASI: EPC = CPC aktual x 1,0 sampai 1,4.
- BONCOS / KILL: EPC < CPC aktual (setelah memperhitungkan jeda pelaporan H+1).

Kill rule rinci:

- Kill dini kreatif bila Outbound CTR < 1,0 persen setelah spend >= Rp20rb. Ini kill dini saja, bukan kill final.
- Kill bila CPC efektif per klik Shopee melebihi Max CPC + 15 persen setelah spend >= Rp50rb.
- Kill final bila total spend >= Rp150-200rb dan 0 order, atau EPC < CPC selama 2 hari berturut-turut setelah 100 klik Shopee.

Bila angka berada tepat di batas ambang, verifikasi dulu di Ads Manager sebelum pause.

### Langkah 4: Laporan dan jam malam

- Jam laporan normal (contoh: 06:30-21:30 WIB): laporan singkat tiap run.
- Jam malam: tetap cek dan catat, tapi kirim pesan hanya bila ada edit (pause) atau error kritis (akun kena flag, iklan rejected). Selebihnya diam dan gabungkan angka malam ke laporan pagi.

### Langkah 5: Evaluasi H+1/H+2 dan penutup

- Bandingkan komisi Shopee tervalidasi vs spend x 1,11 per sub_id, di H+1 dan H+2. Pisahkan ROAS GMV dari ROAS komisi; GMV bukan komisi.
- Saat campaign berakhir, kirim ringkasan akhir (total spend, total per ad set, vonis, dan apa yang harus dicek di laporan Shopee H+1/H+2), lalu nonaktifkan loop monitornya sendiri.

## File referensi

- `references/automated-rules.md`: template empat Automated Rules siap pasang di Ads Manager.
- `references/monitor-loop.md`: spesifikasi loop monitor 30 menit, termasuk yang boleh dan dilarang diubah.
- `references/rumus-ringkas.md`: rumus komisi bersih, Max CPC, EPC, dan CPC efektif.
