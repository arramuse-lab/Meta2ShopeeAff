"""Hitung titik impas iklan afiliasi pada satu skenario anggaran kreator.

Rumus yang dipakai (lihat SKILL.md Step 1 dan
references/threads-field-notes.md §8, koreksi 23 Nov 2026):

- Komisi bersih per pesanan valid =
  (min(harga x % komisi dasar, cap Komisi Shopee) + harga x % XTRA)
  x (1 - % PPh efektif). Skema 15 Sep 2025: komisi dasar Affiliate 1,5%
  non-elektronik / 0,5% elektronik, cap Rp10.000/pesanan; PPh efektif
  bracket bawah 2,5% (DPP 50% x tarif 5%), bukan 5% flat.
- EPC per klik Meta = komisi bersih x CR x rasio masuk,
  dengan CR = pesanan dibuat per klik Shopee, dan rasio masuk =
  klik Shopee / klik keluar Meta. Tanpa rasio masuk, CPC "murah"
  terlihat untung padahal boncos.
- Max CPC Meta (dashboard, margin 30%) =
  (EPC per klik Meta / 1,11) x 0,70. Bila hasilnya < Rp20, produk
  tidak layak diiklan di budget kecil.
- CPC efektif per klik Shopee = CPC Meta / rasio masuk.

Kompatibilitas mundur: pemakaian lama (--komisi + --pesanan-per-100-klik
per klik keluar Meta, tanpa --rasio-masuk-persen) tetap menghasilkan
angka yang sama seperti sebelumnya.
"""

import argparse
from decimal import Decimal, InvalidOperation, ROUND_CEILING

PPN_META = Decimal("1.11")
MARGIN = Decimal("0.70")


def angka_nonnegatif(teks):
    try:
        nilai = Decimal(teks)
    except InvalidOperation as exc:
        raise argparse.ArgumentTypeError("Masukkan angka tanpa pemisah ribuan.") from exc
    if not nilai.is_finite() or nilai < 0:
        raise argparse.ArgumentTypeError("Nilai harus berupa angka nol atau positif.")
    return nilai


def persen(teks):
    nilai = angka_nonnegatif(teks)
    if nilai > 100:
        raise argparse.ArgumentTypeError("Persentase maksimal 100.")
    return nilai


def rupiah(nilai):
    angka = f"{abs(nilai):,.2f}".translate(str.maketrans(".,", ",."))
    awalan = "-Rp" if nilai < 0 else "Rp"
    return awalan + angka.removesuffix(",00")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--anggaran", type=angka_nonnegatif, required=True,
                        help="Anggaran iklan kreator yang diasumsikan habis, dalam rupiah "
                             "(total biaya yang ditanggung kreator, sudah termasuk PPN).")
    parser.add_argument("--komisi", type=angka_nonnegatif,
                        help="Komisi BERSIH rupiah per pesanan valid teratribusi. "
                             "Isi ini, atau isi --harga beserta persentase komisi.")
    parser.add_argument("--biaya-lain", type=angka_nonnegatif,
                        help="Biaya tetap lain untuk periode yang sama, dalam rupiah.")
    parser.add_argument("--pesanan-per-100-klik", type=angka_nonnegatif,
                        help="Pesanan dibuat per 100 klik keluar Meta (mode lama). "
                             "Jangan dipakai bersama --cr-persen.")
    parser.add_argument("--validasi-persen", type=persen,
                        help="Persentase pesanan dibuat yang akhirnya valid, dari 0 sampai 100.")
    parser.add_argument("--cpc", type=angka_nonnegatif,
                        help="Asumsi biaya per klik keluar Meta (dashboard) untuk proyeksi, dalam rupiah.")
    # --- Koreksi 23 Nov 2026: rasio masuk ---
    parser.add_argument("--rasio-masuk-persen", type=persen,
                        help="Rasio masuk: klik Shopee per 100 klik keluar Meta. "
                             "Default 100 (dianggap semua klik sampai). "
                             "Lapangan: FB Feed 95-98%%, IG Reels 30-50%%, bocor 70%% = 30%%.")
    parser.add_argument("--cr-persen", type=persen,
                        help="Conversion rate: pesanan dibuat per 100 klik SHOPEE. "
                             "Pakai ini bersama --rasio-masuk-persen; jangan dipakai "
                             "bersama --pesanan-per-100-klik.")
    # --- Koreksi 23 Nov 2026: komisi bersih dari harga ---
    parser.add_argument("--harga", type=angka_nonnegatif,
                        help="Harga jual produk, dalam rupiah. Dipakai untuk menghitung "
                             "komisi bersih bila --komisi tidak diisi.")
    parser.add_argument("--komisi-dasar-persen", type=angka_nonnegatif, default=Decimal("1.5"),
                        help="Persentase komisi dasar Shopee (default 1.5 non-elektronik; "
                             "isi 0.5 untuk elektronik).")
    parser.add_argument("--xtra-persen", type=angka_nonnegatif, default=Decimal("0"),
                        help="Persentase Komisi XTRA penjual (default 0).")
    parser.add_argument("--cap-komisi", type=angka_nonnegatif, default=Decimal("10000"),
                        help="Cap Komisi Shopee per pesanan (default Rp10.000, skema 15 Sep 2025).")
    parser.add_argument("--pph-persen", type=angka_nonnegatif, default=Decimal("2.5"),
                        help="PPh efektif atas komisi dalam persen (default 2.5, "
                             "DPP 50%% x tarif 5%% bracket bawah).")
    args = parser.parse_args()

    if args.anggaran == 0:
        parser.error("Simulasi belanja kreator memerlukan anggaran lebih besar dari nol.")
    if args.cpc == 0:
        parser.error("CPC untuk simulasi harus lebih besar dari nol.")
    if args.pesanan_per_100_klik is not None and args.cr_persen is not None:
        parser.error("Pilih salah satu: --pesanan-per-100-klik (per klik Meta) "
                     "atau --cr-persen (per klik Shopee), jangan keduanya.")
    if args.komisi is not None and args.harga is not None:
        parser.error("Pilih salah satu: --komisi (komisi bersih langsung) "
                     "atau --harga (hitung komisi bersih dari harga), jangan keduanya.")
    if args.komisi is None and args.harga is None:
        parser.error("Isi --komisi (komisi bersih per pesanan valid) atau --harga.")

    # --- Komisi bersih ---
    if args.komisi is not None:
        komisi = args.komisi
    else:
        dasar = min(args.harga * args.komisi_dasar_persen / 100, args.cap_komisi)
        xtra = args.harga * args.xtra_persen / 100
        kotor = dasar + xtra
        komisi = kotor * (1 - args.pph_persen / 100)
        print(f"Harga produk = {rupiah(args.harga)}")
        print(f"Komisi dasar (min {args.komisi_dasar_persen}% x harga, cap "
              f"{rupiah(args.cap_komisi)}) = {rupiah(dasar)}")
        print(f"Komisi XTRA ({args.xtra_persen}%) = {rupiah(xtra)}")
        print(f"Komisi kotor = {rupiah(kotor)}; PPh {args.pph_persen}% -> "
              f"komisi bersih per pesanan valid = {rupiah(komisi)}")

    total_biaya = args.anggaran + (args.biaya_lain or Decimal(0))
    cakupan = "biaya iklan saja" if args.biaya_lain is None else "iklan dan biaya tetap yang diisi"
    print(f"Biaya simulasi ({cakupan}) = {rupiah(total_biaya)}")
    if komisi == 0:
        print("Dengan komisi Rp0 per pesanan, komisi tidak dapat menutup biaya simulasi.")
        return

    pesanan_impas = (total_biaya / komisi).to_integral_value(rounding=ROUND_CEILING)
    print(f"Pesanan valid minimum untuk impas = {pesanan_impas}")
    if args.pesanan_per_100_klik is None and args.cr_persen is None:
        print("Untuk menghitung EPC dan CPC impas, isi --pesanan-per-100-klik "
              "(per klik Meta) atau --cr-persen (per klik Shopee) beserta "
              "--validasi-persen dan --rasio-masuk-persen bila diketahui.")
        return
    if args.validasi_persen is None:
        print("Untuk menghitung EPC dan CPC impas, isi --validasi-persen.")
        return

    rasio = (args.rasio_masuk_persen if args.rasio_masuk_persen is not None
             else Decimal("100")) / 100
    validasi = args.validasi_persen / 100

    if args.cr_persen is not None:
        # Mode baru: CR diukur per klik Shopee, EPC Meta = komisi x CR x rasio masuk.
        cr = args.cr_persen / 100
        epc_shopee = komisi * cr * validasi
        epc = epc_shopee * rasio
        print(f"CR per klik Shopee = {args.cr_persen}%")
        print(f"Rasio masuk (klik Shopee / klik Meta) = {rasio * 100}%")
        print(f"Estimasi komisi per klik Shopee = {rupiah(epc_shopee)}")
    else:
        # Mode lama: pesanan per 100 klik keluar Meta; EPC Shopee diturunkan bila rasio diketahui.
        tingkat_pesanan_valid = (args.pesanan_per_100_klik / 100) * validasi
        epc = komisi * tingkat_pesanan_valid
        print(f"Rasio masuk (klik Shopee / klik Meta) = {rasio * 100}%")
        if rasio < 1:
            print(f"Estimasi komisi per klik Shopee = {rupiah(epc / rasio)}")

    print(f"Estimasi komisi per klik keluar Meta (EPC) = {rupiah(epc)}")
    cpc_impas = epc * args.anggaran / total_biaya
    print(f"CPC impas untuk biaya simulasi ≈ {rupiah(cpc_impas)}")

    # Max CPC Meta (dashboard) dengan margin 30% — rumus koreksi 23 Nov 2026.
    max_cpc = (epc / PPN_META) * MARGIN
    print(f"Max CPC Meta (dashboard, margin 30%) = {rupiah(max_cpc)}")
    if max_cpc < 20:
        print("KEPUTUSAN: Max CPC di bawah Rp20 — produk TIDAK LAYAK diiklan "
              "di budget kecil. Cari produk lain, jangan paksakan CPC.")
    elif max_cpc < 150:
        print("PERINGATAN: Max CPC di bawah Rp150 — margin sangat tipis; "
              "pertimbangkan bundling/koleksi atau ganti produk sebelum membakar budget.")

    if args.cpc is not None:
        estimasi_komisi = (args.anggaran / args.cpc) * epc
        print(f"Estimasi komisi pada CPC asumsi {rupiah(args.cpc)} = {rupiah(estimasi_komisi)}")
        print(f"Estimasi hasil setelah biaya simulasi = {rupiah(estimasi_komisi - total_biaya)}")
        if rasio < 1:
            cpc_efektif = args.cpc / rasio
            print(f"CPC efektif per klik Shopee = {rupiah(cpc_efektif)}")
            if args.cr_persen is not None:
                be_shopee = epc_shopee
                print(f"CPC impas per klik Shopee = {rupiah(be_shopee)}")
                print("Keputusan EPC vs CPC (per klik Shopee): "
                      f"{'PROFIT / SCALE' if be_shopee >= cpc_efektif * Decimal('1.5') else 'BREAKEVEN / OPTIMASI' if be_shopee >= cpc_efektif else 'BONCOS / KILL'}")
        print("Keputusan EPC vs CPC (per klik Meta): "
              f"{'PROFIT / SCALE' if epc >= args.cpc * Decimal('1.5') else 'BREAKEVEN / OPTIMASI' if epc >= args.cpc else 'BONCOS / KILL'}")


if __name__ == "__main__":
    main()
