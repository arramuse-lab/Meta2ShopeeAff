# Loop Monitor Berkala (30 Menit)

Spesifikasi loop monitor yang menjaga campaign tetap aman saat pengguna tidak memantau layar. Disarikan dari cron live `g2g-renew-monitor-30m` untuk campaign Glad2Glow Super Renew (26-28 Nov 2026, akun iklan 83704961, 2 ad set FB Feed, masing-masing $15 per hari, Traffic/LPV). Ganti nilai campaign di bawah dengan campaign sendiri saat memakai ulang.

## Jadwal dan laporan

- Interval: tiap 30 menit selama campaign aktif.
- Laporan singkat tiap run (maks sekitar 5 baris): jam cek, total spend sejauh ini (mata uang dashboard + kira-kira Rupiah), angka per ad set (spend, CPC, CTR), dan vonis AMAN / WASPADA / KILL + tindakan yang diambil.
- Jam malam (contoh 21:30-06:30): tetap cek dan catat, tapi kirim pesan hanya bila ada edit (pause) atau error kritis (akun kena flag, iklan rejected). Selebihnya diam dan gabungkan angka malam ke laporan pagi.
- Akhir campaign: pada run pertama setelah campaign berakhir, kirim ringkasan akhir (total spend, total per ad set, vonis, dan apa yang harus dicek di laporan Shopee H+1/H+2), lalu nonaktifkan loopnya sendiri.

## Tiap run

1. Baca metrik via API/CLI bila tersedia (level campaign/ad set + tren performa): spend, impressions, outbound clicks, CPC, outbound CTR, LPV ratio per ad set. Jangan pakai browser hanya untuk membaca; pakai browser hanya bila perlu edit atau bila pembacaan API gagal.
2. Hitung biaya riil = spend x 1,11 (PPN). Patokan CPC yardstick contoh Rp150; Max CPC koreksi tergantung XTRA produk (contoh Super Renew: Rp211 bila XTRA 10%, Rp119 bila XTRA 5%). Persen XTRA wajib diketahui dari dashboard affiliate; bila belum diketahui, jangan pernah menyatakan profit hanya dari metrik Meta.
3. Terapkan kill rule skill:
   - Kill dini kreatif bila Outbound CTR < 1,0% setelah spend >= Rp20rb.
   - Kill bila CPC efektif per klik Shopee (CPC dibagi rasio masuk) melebihi Max CPC + 15% setelah spend >= Rp50rb.
   - Kill final bila total spend >= Rp150-200rb dan 0 order, atau EPC < CPC selama 2 hari berturut-turut setelah 100 klik Shopee.
4. Edit yang diizinkan: pause (matikan switch) ad set yang kena kill rule, lalu verifikasi perubahannya.
5. Dilarang: menaikkan budget, mengubah kreatif/targeting/URL/tanggal, menghapus apa pun, membuat campaign baru.
6. Bila angka berada di batas ambang, verifikasi dulu di Ads Manager via browser sebelum pause.
7. Catat setiap run (jam, angka per ad set, keputusan) dengan append ke file log.

## Bila pembacaan metrik gagal

- Bila pembacaan API/CLI gagal (consent atau rate limit), coba sekali via browser.
- Bila itu juga gagal, laporkan singkat kegagalannya dan loop tetap jalan di run berikutnya. Jangan klaim run tidak jalan hanya dari satu kegagalan.

## Bila campaign belum delivering

- Bila campaign belum Active/delivering di run-run awal (masih In review atau Scheduled), laporkan singkat begitu dan terus cek. Jangan edit apa pun.
