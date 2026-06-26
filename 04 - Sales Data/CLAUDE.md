# CLAUDE.md (Local) — Sales Data

> Instruksi lokal khusus folder `04 - Sales Data/`. Berlaku **tambahan** di atas instruksi global di root `CLAUDE.md` (jangan menimpa — aturan global tetap berlaku, terutama Hard Rules §5 soal delete/send/publish/overwrite).

*Last updated: 12 Mei 2026 — Tambah section sales analysis, stock forecasting, sales performance.*

---

## 1. Kapan File Ini Berlaku

Claude wajib baca file ini + semua file relevan di `04 - Sales Data/` **sebelum jawab atau eksekusi task** kalau topiknya:

### 1.A Pricing & Quotation

- 💰 **Harga / pricing** — retail price, distributor price, dealer price, margin, MAP, MSRP
- 🧾 **Quotation / penawaran** — bikin atau review penawaran ke retailer/dealer/end user
- 📦 **Bundling & promo** — paket harga, diskon, subsidi, payday/seasonal promo
- 🤝 **Negosiasi dealer / retail** — terms, payment, term agreement
- 📊 **Sell-in / sell-out program** — tier program, target, insentif
- 🛒 **Marketplace pricing** — harga di Tokopedia/Shopee/TikTok Shop, mapping antar channel
- 📈 **Pricing strategy / repricing** — kapan naik/turun, kompetitor positioning
- 📑 **Sales collateral** — price sheet, dealer card, proposal, sales deck pricing slide

### 1.A.1 Saramonic Sales Dashboard (PENTING)

- 🖥️ Kalau task menyentuh **Saramonic Sales Dashboard** (ubah tampilan, chart, tabel, flag, data, atau deploy ke Netlify) → **WAJIB baca dulu** `Saramonic/Sales Analysis/Saramonic Dashboard — Change Guide.md` sebelum eksekusi. File itu memetakan build pipeline, titik hardcoded, dan 5 langkah finalisasi supaya tidak ada yang kelewat.
- ❗ Jangan pernah edit `Saramonic Sales Dashboard.html` langsung — itu file generate (ditimpa tiap pagi). Edit di `.dashboard_build/template.html` + `build_dashboard.py`.

### 1.B Sales Analysis, Forecasting & Performance

- 📊 **Sales analysis** — performance per SKU, per dealer, per dealer type, trend bulanan/quarterly/yearly
- 📉 **Sales performance review** — sell-in performance, growth rate, MoM/YoY comparison, kontribusi per channel
- 📦 **Stock forecasting / demand planning** — proyeksi sales, restock recommendation, fast/slow mover identification
- 🏆 **Top performer / bottom performer** — SKU mana yang jalan, SKU mana yang stuck, dealer mana yang growth
- 🎯 **Target setting** — target sales per dealer, per SKU, per dealer type
- 📈 **Dealer health check** — performance dealer aktif, dealer dormant, kontribusi per dealer
- 🧮 **Sales reporting** — bikin report sales (weekly/monthly/quarterly) untuk internal atau principal
- 🔁 **Channel mix analysis** — proporsi sales per dealer type (Camera Stores, CE, Audio Stores, System Integrators, dll.)

Kalau task **bukan** salah satu di atas (misal content brief, social caption, brand identity, KOL outreach) — pakai instruksi global aja, **nggak perlu** baca folder ini.

---

## 2. Wajib Baca Sebelum Jawab

### 2.A Pricing Tasks

#### Saramonic
- `04 - Sales Data/Saramonic/Saramonic Price List.md` — master price list resmi Saramonic Indonesia. **Sumber kebenaran** untuk semua angka harga produk Saramonic.

#### BOYA
- `04 - Sales Data/BOYA/BOYA Price List.md` — master price list resmi BOYA Indonesia. **Sumber kebenaran** untuk semua angka harga produk BOYA.

### 2.B Sales Analysis / Forecasting / Performance Tasks

#### Saramonic — folder `04 - Sales Data/Saramonic/SR Sales Data/`

| File                                            | Isi                                                              | Kapan dipakai                                                          |
| ----------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `Categorized Sales Data (By Dealer Type).md`    | Sales revenue + proporsi per dealer type (Camera Stores, CE, Audio Stores, System Integrators, Phone & Accessories, Computer Stores, Modern Channels, Multimedia Rentals, Intercom Rentals, Government, Churches, Hotels, dll.) per bulan + total 2025/2026 | Channel mix analysis, kontribusi per dealer type, performance per kategori dealer |
| `Sales by SKU (QTY).md`                         | Quantity sold per SKU per bulan                                  | Stock forecasting, fast/slow mover identification, demand planning     |
| `Sales by SKU (Value).md`                       | Revenue per SKU per bulan (rupiah)                               | Revenue contribution per SKU, top-performing SKU, pricing impact       |
| `Sales by Dealer (QTY).md`                      | Quantity sold per dealer per bulan                               | Dealer performance per volume, dealer engagement, restock per dealer   |
| `Sales by Dealer (Value).md`                    | Revenue per dealer per bulan (rupiah)                            | Dealer health check, kontribusi per dealer, target setting per dealer  |

#### Saramonic — file stok di `04 - Sales Data/Saramonic/`

| File                                            | Isi                                                              | Kapan dipakai                                                          |
| ----------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `Saramonic Stock Data.md`                       | Snapshot stok aktual per SKU per gudang (PIK2, office, Pinisi, DDS) dalam satuan unit. Berisi SKU name, EP code, lokasi gudang, dan QTY per baris. | Stock analysis, fast/slow mover, dead stock identification, restock planning, cross-check velocity vs stok tersedia. **Wajib dibaca** tiap task yang melibatkan stok, restock recommendation, atau stock-to-sales ratio analysis. |

#### Saramonic — folder `04 - Sales Data/Saramonic/Claim (Sell-out) Data/`
- `Claim Cashback (Sell-out).md` — data klaim cashback (sell-out indicator)
- `Credit Note Usage Data.md` — penggunaan credit note (proxy aktivitas dealer)

#### BOYA — folder `04 - Sales Data/BOYA/BY Sales Data/`

| File                                            | Isi                                                              | Kapan dipakai                                                          |
| ----------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `Categorized Sales Data (By Dealer Type).md`    | Sales revenue + proporsi per dealer type per bulan + total       | Channel mix analysis, kontribusi per dealer type BOYA                  |
| `Sales by SKU (QTY).md`                         | Quantity sold per SKU per bulan                                  | Stock forecasting, fast/slow mover BOYA                                |
| `Sales by SKU (Value).md`                       | Revenue per SKU per bulan (rupiah)                               | Revenue contribution per SKU BOYA                                      |
| `Sales by Dealer (QTY).md`                      | Quantity sold per dealer per bulan                               | Dealer performance per volume BOYA                                     |
| `Sales by Dealer (Value).md`                    | Revenue per dealer per bulan (rupiah)                            | Dealer health check BOYA                                               |

### 2.C Aturan Pilih File yang Tepat

Tergantung pertanyaan yang masuk, pilih kombinasi file yang relevan:

| Pertanyaan / Task                                       | File yang harus dibaca                                                                  |
| ------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| "SKU apa yang paling laku bulan ini di Saramonic?"     | `04 - Sales Data/Saramonic/SR Sales Data/Sales by SKU (QTY).md` + `Sales by SKU (Value).md`                       |
| "Kontribusi Camera Stores berapa % di Saramonic?"      | `04 - Sales Data/Saramonic/SR Sales Data/Categorized Sales Data (By Dealer Type).md`                              |
| "Dealer mana yang paling growth di BOYA?"              | `04 - Sales Data/BOYA/BY Sales Data/Sales by Dealer (Value).md` + `Sales by Dealer (QTY).md`                 |
| "Forecast stock SKU X untuk 3 bulan ke depan"          | `Sales by SKU (QTY).md` brand terkait + `04 - Sales Data/Saramonic/Saramonic Stock Data.md`             |
| "SKU mana yang slow mover?"                            | `Sales by SKU (QTY).md` + `Sales by SKU (Value).md` + `04 - Sales Data/Saramonic/Saramonic Stock Data.md` |
| "Total revenue Q1 2026 Saramonic vs BOYA"              | `Categorized Sales Data (By Dealer Type).md` kedua brand                                |
| "Dealer Camera Store yang paling besar kontribusinya"  | `Sales by Dealer (Value).md` + cross-check dealer type di `Categorized Sales Data`      |
| "Sell-out vs sell-in gap untuk Saramonic"              | `04 - Sales Data/Saramonic/SR Sales Data/Sales by SKU (Value).md` + `Claim (Sell-out) Data/` keduanya             |
| "Berapa stok SKU X sekarang?"                          | `04 - Sales Data/Saramonic/Saramonic Stock Data.md`                                                     |
| "SKU mana yang hampir habis / perlu restock?"          | `04 - Sales Data/Saramonic/Saramonic Stock Data.md` + `04 - Sales Data/Saramonic/SR Sales Data/Sales by SKU (QTY).md`             |
| "Dead stock Saramonic apa saja?"                       | `04 - Sales Data/Saramonic/Saramonic Stock Data.md` + `04 - Sales Data/Saramonic/SR Sales Data/Sales by SKU (QTY).md`             |

### 2.D Aturan Cross-File

- Tiap kali ada pertanyaan harga / pricing → **baca file price list brand yang relevan dulu**.
- Tiap kali ada pertanyaan sales / forecasting / performance → **baca file sales data brand yang relevan dulu**. Jangan jawab dari memori atau dari `Brand Context.md`.
- Kalau produk/dealer/data nggak ada di file → bilang *"data X belum ada di Sales Data, tolong konfirmasi atau update file"* — jangan ngarang.
- Kalau ada inkonsistensi antar file → laporkan ke Kenny, jangan asumsi mana yang benar.
- Kalau task spec lebih kompleks (perlu join antar file, multiple SKU, multiple dealer) → bilang asumsi yang dipakai sebelum jalan.

---

## 3. Hard Rules Khusus Sales & Pricing

Selain hard rules global (`CLAUDE.md` §5), aturan tambahan khusus folder ini:

- 🔒 **Confidential by default.** Semua isi `Sales Data/` = data internal. Harga distributor, margin, dealer terms, tier program, **angka sales actual, nama dealer, dealer breakdown** — **jangan pernah** dimasukkan ke output publik (caption, post, ad, copy, deck untuk eksternal) tanpa konfirmasi Kenny.
- 🔒 **Harga retail vs distributor** — harga retail (yang dilihat consumer) boleh ditulis di output publik. Harga distributor / dealer / margin **tidak boleh** keluar dari folder ini tanpa izin.
- 🔒 **Sales actual & dealer names** — angka sales actual dan nama dealer = strictly internal. Kalau bikin deck untuk principal/external, default-nya pakai % atau index, bukan nominal rupiah, kecuali Kenny approve.
- ⚠️ **Sebelum kirim quotation / penawaran** — Claude wajib tunjukin draft ke Kenny dulu untuk review, **jangan langsung jadi final**.
- ⚠️ **Sebelum update price list atau sales data file** — flag ke Kenny dulu, simpan versi lama dengan suffix `_YYYY-MM-DD` atau `_v2` (bukan overwrite).
- ⚠️ **Stock forecast / restock recommendation** — selalu kasih asumsi yang dipakai (window data, growth rate, seasonality). Jangan kasih angka final tanpa context — Kenny butuh ngerti basis kalkulasinya.
- ❌ **Jangan share file `.md` price list / sales data** ke pihak luar (dealer, retailer, partner, principal). Kalau perlu, export ke format lain (`.pdf`, `.xlsx`) yang sudah Kenny approve.

---

## 4. Format Output Default

### 4.A Pricing Tasks

| Task                                  | Output                                                                                |
| ------------------------------------- | ------------------------------------------------------------------------------------- |
| Quotation singkat (1–3 produk)        | Inline di chat, tabel markdown                                                        |
| Quotation formal ke dealer/retailer   | `.docx` atau `.pdf` letterhead-ready, save di `outputs/` dulu sebelum dikirim ke Kenny |
| Price list update                     | Edit langsung di file `.md` masing-masing brand, versi lama di-backup                  |
| Sales deck pricing slide              | `.pptx` — referensi spec produk dari `Brand Context.md`, harga dari Sales Data         |
| Bundling/promo plan                   | `.md` atau `.xlsx` — kasih breakdown SKU + harga + diskon + margin impact              |
| Comparison harga (vs kompetitor)      | `.md` atau `.xlsx` — sebut sumber harga kompetitor (link/tanggal akses)                |

### 4.B Sales Analysis / Forecasting / Performance Tasks

| Task                                              | Output                                                                                       |
| ------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| Quick lookup (1 SKU / 1 dealer / 1 bulan)         | Inline di chat, tabel markdown                                                               |
| Sales performance report (weekly/monthly)         | `.md` atau `.xlsx` — KPI ringkas + table breakdown + insight 3–5 poin                        |
| Stock forecast / demand planning                  | `.xlsx` — proyeksi per SKU + asumsi + restock recommendation                                 |
| Top/bottom performer analysis                     | `.md` atau `.xlsx` — ranking + delta vs periode sebelumnya + insight                         |
| Channel mix / dealer type analysis                | `.md` atau `.xlsx` + bisa pakai chart kalau diminta (`.png` atau embed di `.pptx`)           |
| Sales deck untuk principal / internal review     | `.pptx` — KPI cards + chart trend + insight                                                  |
| Cross-brand comparison (SR vs BY)                 | `.xlsx` atau `.md` — sandingkan metric apple-to-apple, sebut basis pembanding                |

---

## 5. Workflow Pricing Task

1. **Baca dulu** — file price list brand yang relevan (jangan jawab dari memori).
2. **Cek konsistensi** — kalau ada konflik antara price list dan info lain, price list yang menang.
3. **Draft di scratchpad** (`outputs/`) — jangan langsung edit Sales Data kalau ini quotation/penawaran one-off.
4. **Tunjukin ke Kenny** sebelum jadi final atau dikirim ke pihak luar.
5. **Update Memory** — kalau ada keputusan pricing penting (misal naik harga, bikin promo baru), catat di `01 - About/Memory.md` §3 Decision Log.

## 6. Workflow Sales Analysis / Forecasting / Performance Task

1. **Identifikasi brand & scope** — Saramonic, BOYA, atau both? Periode mana? SKU/dealer/dealer type spesifik atau aggregate?
2. **Baca file yang relevan** — pilih dari §2.B/§2.C, jangan baca semua file kalau nggak perlu (waste context).
3. **Klarifikasi asumsi** — kalau ada angka kosong / data missing / bulan belum lengkap, bilang asumsi yang dipakai (misal: "April 2026 partial, hitung run-rate", "May 2026 kosong, exclude dari trend").
4. **Cross-check** — kalau jawaban tergantung 2+ file (misal: "dealer top performer di Camera Stores"), lakukan join manual + sebutkan source per angka.
5. **Output draft → review** — tunjukin draft ke Kenny sebelum jadi report final, terutama kalau output keluar dari folder ini (untuk principal/external/dealer).
6. **Sebut limitations** — kalau data trend baru 7 bulan, jangan bikin forecast confidence tinggi. Kalau dealer baru aktif 2 bulan, jangan extrapolasi growth-nya jauh.
7. **Update Memory** — kalau ada insight penting (SKU dropped, dealer churned, channel shift), catat di `01 - About/Memory.md`.

---

## 7. Yang Bisa Saya (Claude) Bantu

### Pricing
- ✅ Cari harga produk spesifik dari price list
- ✅ Bikin draft quotation/penawaran berdasarkan price list
- ✅ Hitung margin, diskon, bundling impact (kalau angka mentah ada di file)
- ✅ Compare harga antar varian produk
- ✅ Bikin tabel breakdown SKU + harga + spec untuk deck
- ✅ Saran struktur pricing tier
- ✅ Saran bundling/promo plan
- ⚠️ Compare dengan kompetitor — saya bisa bantu, tapi data kompetitor harus Kenny kasih

### Sales Analysis, Forecasting & Performance
- ✅ Ranking SKU per QTY / Value (top/bottom mover) per periode
- ✅ Ranking dealer per QTY / Value, dealer growth analysis
- ✅ Channel mix analysis (proporsi per dealer type) + trend MoM/YoY
- ✅ Sales performance report (weekly/monthly/quarterly)
- ✅ Stock forecasting — proyeksi linear / moving average / growth-adjusted (sebut metodologinya)
- ✅ Restock recommendation berdasarkan run-rate + safety stock asumsi
- ✅ Cross-brand comparison (Saramonic vs BOYA) di metric apple-to-apple
- ✅ Sell-in vs sell-out gap analysis (kalau data claim/credit note tersedia)
- ✅ Identify dormant dealer (last purchase >3 bulan) atau dealer di-risk
- ⚠️ Forecast advanced (seasonality, regression, ARIMA) — bisa, tapi flag dulu kalau dataset terbatas (<12 bulan history)
- ⚠️ Insight strategic (kenapa SKU X jeblok / dealer Y stuck) — saya bisa kasih hipotesis, tapi grounded di data; root cause kualitatif harus Kenny validasi

---

## 8. Catatan Tambahan

[Apapun yang Claude perlu tahu yang belum masuk kategori di atas — misal: pricing principle internal, kapan boleh diskon ekstra, dealer mana yang punya terms khusus, dealer mana yang strategis vs opportunistic, dll.]

---

---

## 9. Changelog

| Tanggal | Perubahan |
|---|---|
| 12 Mei 2026 | File dibuat. Tambah section sales analysis, stock forecasting, sales performance. |
| 29 Mei 2026 | Tambah `Saramonic Stock Data.md` ke §2.B (file stok Saramonic) dan update §2.C (tabel lookup queries). |

---

*Update file ini tiap ada perubahan workflow pricing/sales analysis, atau tambah file baru di `Sales Data/`.*
