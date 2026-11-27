# AutoMeta

Skill fokus untuk mengelola Meta Ads Shopee Affiliate secara otomatis: monitoring berkala, diagnosis EPC vs CPC, auto-kill stop-loss, alert pemenang, dan scaling.

## Asal

Disarikan dari `meta-ads-shopee-affiliate-pro` (Step 5 dan Template Automated Rules) dan spesifikasi loop monitor live `g2g-renew-monitor-30m` untuk campaign Glad2Glow Super Renew (26-28 Nov 2026). Bukan pengganti skill induk; ini versi fokusnya, khusus otomatisasi.

## Isi paket

- `SKILL.md`: alur kerja 6 langkah (siapkan angka dasar, pasang Automated Rules, loop monitor, vonis kill/scale, laporan dan jam malam, evaluasi H+1/H+2).
- `references/automated-rules.md`: template 4 Automated Rules siap pasang di Ads Manager (Auto-Kill Hook, Auto-Kill CPC, Auto-Kill Final, Auto-Alert Pemenang).
- `references/monitor-loop.md`: spesifikasi loop monitor tiap 30 menit, termasuk yang boleh dan dilarang diubah.
- `references/rumus-ringkas.md`: rumus komisi bersih, Max CPC, EPC, dan CPC efektif.

## Cara install

Salin folder `autometa` ke folder skill Muse (contoh: `~/workspace/custom-skills/`), lalu verifikasi lewat pencarian skill. Cara pakai: pasang dulu Automated Rules di Ads Manager sebelum launch, lalu jalankan loop monitor selama campaign aktif.

## Catatan penting

- Muse read-only di akun iklan (Ads MCP write dinonaktifkan Meta). Pause dilakukan lewat browser. Yang mematikan iklan secara native dan otomatis adalah Automated Rules Meta sendiri.
- Jangan menyatakan profit hanya dari metrik Meta. Komisi Shopee lag H+1.
