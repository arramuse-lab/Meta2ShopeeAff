# Template Automated Rules (Stop-Loss Anti-Boncos)

Pasang aturan otomatis berikut di Meta Ads Manager (menu Automated Rules) pada level Ad atau Ad Set, agar budget tidak habis saat pengguna tidak memantau layar. Disarikan dari `meta-ads-shopee-affiliate-pro`, `references/unit-economics-and-diagnostics.md` bagian 4, termasuk koreksi 23 Nov 2026.

Isi dulu nilai `[Max CPC Aman Koreksi]` dan `[Target Max CPC Profit]` dari `rumus-ringkas.md` sebelum memasang aturan. Tanpa nilai itu, aturan tidak bisa jalan dengan benar.

## Rule 1: Auto-Kill Kreatif Gagal Hook (Cut Loss Dini)

- Apply to: All Active Ads (Campaign Testing)
- Action: Turn off ads
- Conditions:
  - `Amount Spent` >= Rp20.000 (atau 0.8x Net Commission)
  - AND `Outbound CTR` < 1,0%
- Time Range: Today (atau Lifetime saat hari pertama testing)
- Schedule: Runs continuously (setiap 30 menit)
- Catatan koreksi 23 Nov 2026: rule ini hanya kill dini berbasis CTR; jangan jadikan kill final. Spend Rp20rb terlalu kecil untuk menilai order.

## Rule 2: Auto-Kill CPC Kemahalan (Pelindung Margin)

- Apply to: All Active Ads
- Action: Turn off ads
- Conditions:
  - `Amount Spent` >= Rp50.000 (koreksi 23 Nov 2026: ambang lama Rp25.000 terlalu kecil. Rp20rb pada CPC Rp150 = sekitar 133 klik Meta, sekitar 40 klik Shopee, ekspektasi order di bawah 0,5 pada CR 1%)
  - AND `Cost per Outbound Click` > `[Max CPC Aman Koreksi + 15%]`. Hitung CPC efektif per klik Shopee (CPC dibagi rasio masuk) bila rasio masuk diketahui.
- Time Range: Today
- Schedule: Runs continuously

## Rule 2b: Auto-Kill Final (Spend Besar, 0 Order)

Baru, koreksi 23 Nov 2026.

- Apply to: All Active Ad Sets
- Action: Turn off ad sets
- Conditions:
  - `Amount Spent` >= Rp150.000 hingga Rp200.000 (total, lifetime)
  - AND 0 pesanan valid (cek laporan Shopee H+1/H+2 per sub_id)
  - ATAU EPC per klik Meta < CPC x 1,0 selama 2 hari berturut-turut setelah 100 klik Shopee atau lebih
- Time Range: Lifetime

## Rule 3: Auto-Alert Pemenang (Notifikasi Scale)

- Apply to: All Active Ad Sets
- Action: Send notification only (jangan auto-increase drastis tanpa cek komisi Shopee H+1)
- Conditions:
  - `Amount Spent` >= Rp30.000
  - AND `Cost per Outbound Click` <= `[Target Max CPC Profit]`
  - AND `Outbound CTR` >= 2,5%
- Time Range: Yesterday / Last 2 Days
