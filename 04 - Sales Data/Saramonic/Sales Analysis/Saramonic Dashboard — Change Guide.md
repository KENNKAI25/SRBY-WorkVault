# Saramonic Sales Dashboard — Change Guide

> **Untuk Claude:** Baca file ini **wajib** sebelum mengubah apa pun di Saramonic Sales Dashboard. Tujuannya: tiap perubahan yang Kenny minta dieksekusi lengkap, tanpa ada langkah/efek samping yang kelewat.
>
> *Last updated: 26 Jun 2026*

---

## 0. TL;DR — aturan emas (baca ini dulu)

1. **JANGAN PERNAH edit file `Saramonic Sales Dashboard.html` langsung.** File itu **hasil generate** — akan ditimpa otomatis tiap pagi 08:03 oleh scheduled task. Semua perubahan ditiban besok pagi.
2. **Semua perubahan ada di 2 file di folder `.dashboard_build/`:**
   - `template.html` → layout, CSS, teks, chart, tabel, logika tampilan (JS).
   - `build_dashboard.py` → cara baca data + bentuk data yang dikirim ke template.
3. Setelah edit, **WAJIB jalankan 5 langkah finalisasi** (lihat §6). Kalau salah satu kelewat, perubahan gak akan kelihatan di salah satu tempat (artifact / file / Netlify).
4. **Perubahan paling berisiko = ganti rentang bulan** (mis. masuk Juli). Itu menyentuh banyak titik hardcoded. Lihat §7 — kerjakan dengan checklist khusus.

---

## 1. Apa itu dashboard ini

Dashboard HTML statis 1 file (self-contained, cuma load Chart.js dari CDN) yang menampilkan performa **sell-in** Saramonic: tren revenue, breakdown per dealer, per SKU, dan "Flags" (dealer yang perlu perhatian). Data sumbernya lokal (markdown), bukan database.

Dashboard ini muncul di **3 tempat** (penting — sering jadi sumber "kok belum berubah?"):

| Tempat | Apa | Kapan ter-update |
|---|---|---|
| **File HTML** | `Sales Analysis/Saramonic Sales Dashboard.html` | tiap build |
| **Cowork artifact** | id `saramonic-sales-dashboard` (yang tampil di app Cowork) | saat `update_artifact` dipanggil |
| **Netlify (publik)** | https://saramonic-salesdashboard.netlify.app | saat deploy dari Mac Kenny (lihat `.deploy-tools/`) |

---

## 2. Peta file (path lengkap)

Semua di bawah: `04 - Sales Data/Saramonic/`

```
Saramonic/
├── SR Sales Data/                       ← SUMBER DATA (input)
│   ├── Sales by SKU (Value).md          ← revenue per SKU per bulan
│   ├── Sales by SKU (QTY).md            ← unit per SKU per bulan
│   ├── Sales by Dealer (Value).md       ← revenue per dealer per bulan
│   └── Sales by Dealer (QTY).md         ← unit per dealer per SKU per bulan
├── Saramonic Stock Data.md              ← stok gudang (untuk kolom Stok/Cover)
└── Sales Analysis/
    ├── Saramonic Sales Dashboard.html   ← OUTPUT (JANGAN diedit langsung)
    ├── Saramonic Dashboard — Change Guide.md   ← file ini
    ├── .dashboard_build/                ← MESIN BUILD (edit di sini)
    │   ├── build_dashboard.py           ← baca data → JSON → inject ke template
    │   └── template.html                ← HTML/CSS/JS + placeholder __DATA__
    ├── _deploy/
    │   └── index.html                   ← copy dashboard untuk Netlify
    └── .deploy-tools/                   ← script deploy Netlify (lihat README di dalamnya)
```

**Cara kerja build (1 kalimat):** `build_dashboard.py` baca 5 file sumber → susun jadi 1 objek JSON → tempel ke `template.html` di posisi `__DATA__` → tulis hasilnya jadi `Saramonic Sales Dashboard.html`.

---

## 3. Kontrak data — format file sumber (jangan dilanggar)

Build script mem-parsing tabel markdown baris per baris (`|`-delimited). **Kalau format tabel berubah, build bisa error atau salah baca diam-diam.**

### Rentang bulan = **terkunci 9 kolom**: `2025-10` s/d `2026-06`
Didefinisikan di `build_dashboard.py` baris `MONTHS = [...]`. Semua file sumber **harus** punya 9 kolom bulan ini + kolom `Total`, dengan urutan sama.

### Per file:
- **Sales by SKU (Value).md** — kolom: `SKU Type | SKU Name | [9 bulan] | Total`. `SKU Type` cuma diisi di baris pertama tiap grup (sisanya kosong = lanjut grup di atasnya). Baris `Total` & baris kosong di-skip. → ini sumber **kategori SKU**.
- **Sales by SKU (QTY).md** — kolom: `SKU Name | [9 bulan] | Total`. (tanpa kolom Type.)
- **Sales by Dealer (Value).md** — kolom: `Client Location | Client | [9 bulan] | Total`. `Client Location` cuma diisi di baris pertama tiap lokasi.
- **Sales by Dealer (QTY).md** — kolom: `Client | SKU Name | [9 bulan] | Total`. `Client` cuma diisi di baris pertama tiap dealer. → ini sumber **SKU apa yang dibeli tiap dealer**.
- **Saramonic Stock Data.md** — kolom: `SKU Name(kode) | Title | Warehouse | Area | Shelf | Available`. Yang dipakai: kolom **Title** (dicocokkan ke nama SKU) + kolom **Available** (dijumlah per Title).

### Aturan angka
- Angka boleh pakai pemisah ribuan koma (`229,948,000`) — script otomatis bersihkan.
- Sel kosong = 0 (atau "tidak ada order" untuk logika flag/last-order).

### Pencocokan stok ↔ SKU (sering meleset)
Script mencocokkan `Title` di Stock Data ke `SKU Name` di Sales pakai fungsi `norm()`: lowercase → buang semua selain huruf/angka → buang kata "saramonic". Kalau penamaan beda jauh, kolom **Stok** jadi `n/a` dan **Cover** jadi `—`. Kalau Kenny bilang "stok SKU X kok n/a", cek kecocokan nama di sini dulu.

---

## 4. Isi dashboard — peta section ↔ lokasi di template

Pakai ini untuk tahu **di mana** mengubah sesuatu. (Nomor baris bisa bergeser; pakai sebagai petunjuk, cari berdasarkan teks/`id`.)

| Yang tampil | Lokasi HTML (template.html) | Logika JS (template.html) | Butuh data dari build |
|---|---|---|---|
| Judul, subtitle, tanggal data | `<header class="top">` | `gendate`, `period-range` | `generated`, `months` |
| Catatan "bulan berjalan parsial" | `#partial-note` | blok `partial-note` | — |
| KPI utama (Bulan/Quarter/Tahun ini) | `#kpis-primary` | blok `render KPIs` + `pctVal` | `monthlyTotal` |
| KPI sekunder (Total/Dealer aktif/SKU aktif/Flags) | `#kpis-secondary` | sda | `dealers`, `skus` |
| Tab nav (Performance/Dealer/SKU/Flags) | `.tabs` | blok `tabs` | — |
| **Performance:** Tren Revenue (bar, toggle bln/quarter/tahun) | `#panel-perf` → `#trendChart` | `drawTrend`, array `Q`, `YEARS` | `monthlyTotal` |
| Quarterly Breakdown (tabel) | `#qtable` | IIFE quarter table | `monthlyTotal` |
| Kontribusi per Kategori (doughnut) | `#catChart` | IIFE category chart | `skus[].type,totalValue` |
| **Dealer:** Top 12 Dealer (bar) | `#dealerBars` | `barList` | `dealers[].totalValue` |
| Revenue per Lokasi (bar horizontal) | `#locChart` | IIFE | `dealers[].location` |
| Tabel "Semua Dealer" (Ringkasan/Value Bulanan/Quarter) | `#dealerTable` dll | `renderDealerTable`, `renderValMatrix` | `dealers[].value` |
| Detail SKU per Dealer (qty bulanan) | `#dealerSkuTable` | IIFE dealer→SKU | `dealers[].skuMonthly` |
| **SKU:** Top 12 SKU Value & Qty | `#skuBars`, `#skuQtyBars` | IIFE | `skus[].totalValue/totalQty` |
| Tabel "Semua SKU" (Ringkasan/Qty/Value) | `#skuTable` dll | `renderSkuTable` dll | `skus[]` (+`stock`) |
| **Flags:** dealer prioritas | `#flagsList` | **FLAG ENGINE** (lihat §5) | `dealers[]` |
| Footer | `.foot` | — | — |

### Bentuk objek `DATA` yang dikirim build → template
```
DATA = {
  months: ["2025-10", … "2026-06"],
  monthlyTotal: [9 angka],                       // total revenue semua SKU per bulan
  generated: "YYYY-MM-DD",
  skus: [ {name, type, value[9], qty[9], totalValue, totalQty, stock|null} ],
  dealers: [ {name, location, value[9], qty[9], totalValue,
              topSkus:[[sku,val]…5], skuMonthly:[{name, m[9], t}] } ]
}
```

---

## 5. Logika bisnis yang hardcoded (HARUS diingat saat ubah angka/aturan)

Ini titik-titik yang gampang bikin hasil "kelihatan jalan tapi salah". Kalau perubahan menyentuh ini, sebut eksplisit.

- **Quarter mapping** (template `Q`, `QH`, `qOf`, `YEARS`): Q4'25=Okt–Des (idx 0-2), Q1'26=Jan–Mar (idx 3-5), Q2'26=Apr–Jun (idx 6-8, *berjalan*). **Hardcoded** ke 9 bulan / 3 quarter.
- **Bulan penuh terakhir** = `LASTFULL = M.length-2`. Artinya **bulan terakhir selalu dianggap parsial/berjalan**, bulan sebelumnya dianggap penuh. Dipakai untuk MoM, kolom tabel dealer, flag.
- **Velocity** = rata-rata unit 3 bulan: `qty[5]+qty[6]+qty[7]` = **Mar+Apr+Mei** (hardcoded idx 5,6,7). Dipakai di kolom SKU "Vel/bln" & "Cover".
- **Cover** = stok ÷ velocity. Pill: `<1` merah, `<2` kuning, `≥2` hijau, tanpa stok = `—`, velocity 0 tapi ada stok = `∞`.
- **Flag engine** (3 kondisi, hasil dedupe per dealer & ambil top 10 by score):
  1. **Drop ≥20%** — turun ≥20% MoM **dan** ≥20% QoQ, dealer masih aktif, basis quarter ≥ Rp 5 jt. (`md`/`qd`, bandingkan Mar-Mei vs Des-Feb)
  2. **One-time** — 1 order ≥ Rp 25 jt yang ≥80% total dealer & ≤2 bulan pernah order.
  3. **Dormant** — pernah order, tapi tidak order ≥1 bulan penuh terakhir.
  - Ambang (20%, Rp 5jt, Rp 25jt, 80%, top 10) semua hardcoded di blok `FLAG ENGINE`. Kalau Kenny mau ubah sensitivitas flag, ubah di sini.
- **Format Rupiah**: `rp()` ringkas (M = miliar, jt, rb); `rpFull()` lengkap. Locale `id-ID`.
- **Label bulan Indonesia**: `fmtMonthLbl` (Jan…Des, "Mei" bukan "May").

---

## 6. Workflow eksekusi perubahan — 5 langkah finalisasi (WAJIB lengkap)

Setelah edit `template.html` dan/atau `build_dashboard.py`:

1. **Rebuild** — jalankan via bash:
   ```
   python3 "$(ls /sessions/*/mnt/SRBY-WorkVault/04*/Saramonic/Sales*/.dashboard_build/build_dashboard.py | head -1)"
   ```
   Sukses = ada baris `OK SKUs=.. Dealers=.. Grand=.. Gen=..` dan `OUTPUT_HTML=..`. Kalau `ERROR` → **stop**, perbaiki, jangan lanjut.
2. **Verifikasi** — buka/baca output HTML, pastikan perubahan benar & gak ada section yang pecah (cek angka KPI masuk akal vs baris `OK`). Untuk perubahan besar, cek di browser.
3. **Update Cowork artifact** — panggil `mcp__cowork__update_artifact` dengan id `saramonic-sales-dashboard`, `html_path` = OUTPUT_HTML, summary singkat.
4. **Refresh file deploy** — copy output ke folder deploy:
   ```
   cp "<OUTPUT_HTML>" "$(dirname "<OUTPUT_HTML>")/_deploy/index.html"
   ```
5. **Deploy ke Netlify** — **tidak bisa dari sini** (sandbox diblokir). Beri tahu Kenny untuk double-click `.deploy-tools/deploy.command` di Mac (atau tunggu auto-deploy harian kalau launchd aktif). Catat ini di balasan supaya gak terlupa.

> Catatan: kalau perubahan cuma data (Kenny update file di SR Sales Data), scheduled task pagi otomatis lakukan langkah 1, 3, 4. Tinggal langkah 5 (deploy) yang manual dari Mac. Tapi kalau Kenny mau lihat **sekarang**, jalankan 5 langkah manual.

---

## 7. ⚠️ Operasi berisiko tinggi: menambah/menggeser bulan (mis. masuk Juli 2026)

Ini paling sering bikin dashboard "setengah jalan". Kalau rentang bulan berubah, **semua titik ini wajib diupdate bareng**:

1. **File sumber** (5 file di SR Sales Data + Stock): tambahkan kolom bulan baru pada SEMUA tabel, urutan konsisten.
2. **`build_dashboard.py`**: update array `MONTHS`. Cek semua `range(9)`, `r[2+i]`, `len(r)<12/<11` — angka 9/11/12 bergantung jumlah bulan. (9 bulan → value SKU 12 kolom, qty SKU 11 kolom, dealer 12 kolom.)
3. **`template.html`** — update yang hardcoded ke 9 bulan/3 quarter:
   - `Q` array + `QH` + `qOf()` (definisi & label quarter)
   - `YEARS` array
   - Velocity index `qty[5]+qty[6]+qty[7]` & flag index `v[5]+v[6]+v[7]`, `v[2]+v[3]+v[4]` — apakah masih "3 bulan terakhir penuh" yang benar?
   - Cek asumsi `LASTFULL` (bulan baru penuh atau parsial?)
4. Jalankan **5 langkah finalisasi** (§6).

**Kalau Kenny minta tambah bulan, konfirmasi dulu**: apakah ingin tetap menampilkan 9 bulan (geser window, buang Okt'25) atau menambah jadi 10+ bulan? Jawabannya mengubah banyak hal di atas.

---

## 8. Jenis perubahan → file mana yang disentuh (panduan cepat)

| Permintaan Kenny | Edit di | Catatan |
|---|---|---|
| Ubah warna/font/spacing/teks label | `template.html` (CSS / HTML) | langsung |
| Tambah/ubah/hapus chart atau tabel | `template.html` (HTML + JS) | pastikan data tersedia di `DATA`; kalau belum, tambah di build script |
| Ubah ambang/aturan Flags | `template.html` (FLAG ENGINE) | lihat §5 |
| Ubah cara hitung velocity/cover/quarter | `template.html` | lihat §5 — hardcoded |
| Tambah metrik baru dari data yang sudah ada | `template.html` | data sudah di `DATA` |
| Tambah metrik dari data yang BELUM diparse | `build_dashboard.py` **lalu** `template.html` | dua file |
| Ubah sumber data / tambah kolom | `build_dashboard.py` + file sumber | lihat §3 |
| Tambah/geser bulan | semua (lihat §7) | berisiko tinggi |
| Ganti judul/branding | `template.html` | header & `<title>` & footer |

---

## 9. Template permintaan perubahan (isi ini biar gak ada yang kelewat)

> Kenny: copy blok ini saat minta perubahan. Makin lengkap, makin kecil kemungkinan salah.

```
PERUBAHAN DASHBOARD SARAMONIC
1. Apa yang mau diubah: (section/elemen mana — pakai nama di §4)
2. Jadi seperti apa: (deskripsi hasil yang diinginkan)
3. Kenapa / konteksnya: (opsional, bantu ambil keputusan desain)
4. Data baru dibutuhkan?: (ya/tidak — kalau ya, dari file/kolom mana)
5. Mendesak lihat sekarang, atau cukup ikut refresh besok pagi?
6. Setelah jadi: perlu langsung deploy ke Netlify publik?
```

Setelah Kenny isi, Claude: baca guide ini → edit file build yang tepat → jalankan §6 (5 langkah) → laporkan ringkas + ingatkan langkah deploy Netlify kalau diminta publik.

---

## 10. Hal yang TIDAK boleh dilakukan tanpa konfirmasi Kenny (lihat juga CLAUDE.md §5)

- Mengubah `build_dashboard.py` atau `template.html` secara struktural besar tanpa diminta.
- Menghapus file sumber atau output.
- Men-deploy ke Netlify publik **data yang berubah** tanpa Kenny tahu (data confidential, URL publik).
- Mengubah rentang bulan (berdampak luas — konfirmasi dulu, lihat §7).
