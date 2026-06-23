# SR — Claude Design Prompt — Erafone Activity Report (Mei–Jun 2026)

> **Tujuan file ini:** prompt siap-pakai untuk **Claude Design** buat generate presentasi visual (HTML deck) yang nunjukin aktivitas Saramonic di Erafone sejak Mei 2026.
> **Audience deck:** Partner Erajaya / Erafone → tone partnership, hasil + komitmen.
> **Bahasa deck:** Bahasa Indonesia. **Scope:** Erafone-only. **Format:** visual deck 16:9.
>
> **Cara pakai (ringkas):**
> 1. Isi dulu semua placeholder `{{...}}` di BAGIAN 2 (Material) — angka, foto, challenge.
> 2. Copy seluruh BAGIAN 3 (THE PROMPT) → paste ke Claude Design.
> 3. Lampirin/seret foto sesuai instruksi di prompt.
> 4. Review hasil → revisi via follow-up prompt.
>
> *Dibuat: 2026-06-23. Data aktivitas: Todoist (project Saramonic). Status placeholder = WAJIB diisi Kenny sebelum run.*

---

## BAGIAN 1 — Struktur Deck (peta isi)

| # | Slide | Isi |
|---|-------|-----|
| 1 | Cover | Judul, periode, logo Saramonic × Erafone |
| 2 | Executive Summary | Angka besar: total training, toko, KOL, promo periode |
| 3 | Divider: Training & Demoday | — |
| 4–7 | 4× Training (Margonda, Sedayu, R5, MOI) | Brief / Output / Challenges |
| 8 | Divider: Merchandising & Branding | — |
| 9 | POP Material Air & Air SE | Brief / Output / Challenges |
| 10 | Visual Branding 4 Toko | Brief / Output / Challenges |
| 11 | Divider: Dealer Program & Promo | — |
| 12 | Promo (PAYDAY, Double Date, Payday Sharing) | Brief / Output / Challenges |
| 13 | KOL Visit Program ke Erafone | Brief / Output / Challenges |
| 14 | PWP Bundling (OPPO/VIVO) | Brief / Output / Challenges |
| 15 | Divider: Content & Collab | — |
| 16 | Podcast & Live Session Erafone R5 | Brief / Output / Challenges (upcoming) |
| 17 | Key Learnings & Next Step (Phase 2) | Ringkasan + rekomendasi |

> Tiap slide aktivitas pakai **template 3 blok tetap**: **Brief** (apa aktivitasnya) · **Output** (hasil terukur) · **Challenges** (kendala + cara diatasi).

---

## BAGIAN 2 — Material Checklist (ISI DULU SEBELUM RUN)

> Yang dari Todoist sudah saya isiin. Yang `{{...}}` = cuma kamu yang tahu, wajib diisi. Kalau belum ada angka, tulis `n/a` atau kira-kira + tandai `(estimasi)`.

### Global
- Periode laporan: **Mei – Juni 2026**
- Logo Saramonic: Saramonic Logo
- Logo Erafone/Erajaya: `{{PATH_LOGO_ERAFONE}}`
- Warna aksen deck: hitam/charcoal + aksen oranye Saramonic (ganti kalau ada hex resmi: `{{HEX_AKSEN}}`)

### Executive Summary (angka besar)
- Total sesi training Erafone: **4** (Margonda, Sedayu, R5, MOI)
- Total toko di-branding: **4** (Bintaro Xchange, Ruko Kemang, Kelapa Gading, MOI)
- Total KOL approved visit Erafone: **6**
- Total peserta training (semua sesi): `{{TOTAL_PESERTA}}`
- Sell-in / sell-out highlight (opsional): `{{SALES_HIGHLIGHT}}`

### A. Training (per sesi — isi yang sama buat tiap toko)
**A1. Erafone Region 1 — Margonda** (selesai 2 Jun 2026)
- Produk: Air, Air SE, Ultra, SR-C series
- Jumlah peserta: 6
- Output: `{{MARGONDA_OUTPUT}}` (mis. X staff paham demo Air, Y unit demo terpasang)
- Challenges: `{{MARGONDA_CHALLENGE}}`
- Foto: `{{MARGONDA_FOTO}}`

**A2. Erafone Region 1 — Sedayu** (selesai awal Jun 2026)
- Produk: Air, Air SE, Ultra, SR-C series
- Peserta: 5 orang · Output: Pembelajaran key selling point utama & cara jualan · Challenges: Orang terlalu sedikit dan transfer knowledge ke ERO lain kurang optimal  · Foto: `{{SEDAYU_FOTO}}`

**A3. Erafone Region 5** (selesai ~6 Jun 2026)
- Produk: Air, Air SE, Ultra, SR-C series
- Peserta: `{{R5_PESERTA}}` · Output: `{{R5_OUTPUT}}` · Challenges: `{{R5_CHALLENGE}}` · Foto: `{{R5_FOTO}}`

**A4. Erafone MOI (Mall of Indonesia)** (selesai 15 Jun 2026)
- Produk: Air, Air SE, Ultra, SR-C series
- Peserta: `{{MOI_PESERTA}}` · Output: `{{MOI_OUTPUT}}` · Challenges: `{{MOI_CHALLENGE}}` · Foto: `{{MOI_FOTO}}`

### B. Merchandising & Branding
**B1. POP Material Air & Air SE** (selesai 10–13 Jun 2026)
- Brief: desain POP material hero product (Air & Air SE) + versi informatif harga, untuk display Erafone
- Output: `{{POP_OUTPUT}}` (mis. X desain final, didistribusi ke Y toko)
- Challenges: `{{POP_CHALLENGE}}` · Foto: `{{POP_FOTO}}`

**B2. Visual Branding 4 Toko** (ongoing, target 26 Jun 2026)
- Toko & ukuran: Bintaro Xchange (96×62), Ruko Kemang (96×58), Kelapa Gading (108,5×59), MOI (92×56)
- Output: `{{BRANDING_OUTPUT}}` (mis. status print/pasang per toko)
- Challenges: `{{BRANDING_CHALLENGE}}` · Foto: `{{BRANDING_FOTO}}`

### C. Dealer Program & Promo
**C1. Promo Periode** (PAYDAY 25 Mei–6 Jun · Double Date 5.5 · Payday Sharing 25 Jun–7 Jul)
- Brief: aktivasi promo harga di channel Erafone
- Output: `{{PROMO_OUTPUT}}` (mis. uplift sell-out %, SKU terlaris)
- Challenges: `{{PROMO_CHALLENGE}}`

**C2. KOL Visit Program ke Erafone** (on-progress — 6 KOL approved)
- KOL: rizalhamzahnasution, technoboy.10, Akkang Heyhe, endrilost (offline) + rhyndutech, Priscilia Tanbayong (online)
- Output: `{{KOL_OUTPUT}}` (mis. jumlah konten tayang, reach)
- Challenges: `{{KOL_CHALLENGE}}` · Foto/link konten: `{{KOL_FOTO}}`

**C3. PWP Bundling (OPPO/VIVO)** (draft/on-progress)
- Brief: setup Purchase-With-Purchase, connect Saramonic ke pembelian OPPO/VIVO di Erafone
- Output/status: `{{PWP_OUTPUT}}` · Challenges: `{{PWP_CHALLENGE}}`

### D. Content & Collab
**D1. Podcast & Live Session Erafone R5** (upcoming — 25 Jun 2026)
- Brief: sesi podcast + live bareng Erafone Region 5
- Target output: `{{PODCAST_TARGET}}` · Catatan/risiko: `{{PODCAST_CHALLENGE}}`

---

## BAGIAN 3 — THE PROMPT (copy-paste ke Claude Design)

> Setelah placeholder di atas diisi, replace `{{...}}` di blok ini dengan angka aslinya, lalu copy semua dari garis bawah ini.

---

Buatkan **presentasi visual (HTML deck, rasio 16:9, navigasi keyboard kiri/kanan)** berisi laporan aktivitas **Saramonic × Erafone periode Mei–Juni 2026**. Deck ini untuk dipresentasikan ke **partner Erajaya/Erafone**, jadi tone-nya profesional, partnership, fokus ke hasil dan komitmen. Semua teks dalam **Bahasa Indonesia**.

**Design direction:**
- Tema gelap/charcoal premium dengan aksen oranye Saramonic. Pro-audio look (bersih, tegas, banyak ruang kosong).
- Tipografi sans-serif modern, hierarki kuat (angka besar untuk metrik).
- Tiap slide aktivitas pakai layout 3 blok konsisten berlabel: **BRIEF**, **OUTPUT**, **CHALLENGES** (CHALLENGES diberi warna aksen berbeda biar gampang dibaca).
- Sediakan slot gambar (placeholder bertuliskan "Foto: [nama aktivitas]") di tiap slide aktivitas — saya akan ganti fotonya nanti.
- Header tiap slide: logo Saramonic kiri, "× Erafone" kanan, nomor + total slide.

**Susunan slide:**

1. **Cover** — "Saramonic × Erafone — Activity Report" / subjudul "Periode Mei–Juni 2026" / ruang logo Saramonic & Erafone.

2. **Executive Summary** — tampilkan 4 metrik besar: {{TOTAL_TRAINING=4}} sesi training · {{TOTAL_TOKO=4}} toko di-branding · {{TOTAL_KOL=6}} KOL aktivasi · {{TOTAL_PESERTA}} peserta dilatih. Tambah 1 kalimat ringkas pencapaian + highlight sales: {{SALES_HIGHLIGHT}}.

3. **Divider** — "Bagian 1 · Training & Demoday".

4. **Erafone Region 1 — Margonda** (2 Jun 2026)
   - BRIEF: Training & demoday produk Air, Air SE, Ultra, dan SR-C series untuk staff toko.
   - OUTPUT: {{MARGONDA_PESERTA}} peserta — {{MARGONDA_OUTPUT}}.
   - CHALLENGES: {{MARGONDA_CHALLENGE}}.

5. **Erafone Region 1 — Sedayu** (awal Jun 2026)
   - BRIEF: Training & demoday Air, Air SE, Ultra, SR-C series.
   - OUTPUT: {{SEDAYU_PESERTA}} peserta — {{SEDAYU_OUTPUT}}.
   - CHALLENGES: {{SEDAYU_CHALLENGE}}.

6. **Erafone Region 5** (6 Jun 2026)
   - BRIEF: Training & demoday Air, Air SE, Ultra, SR-C series.
   - OUTPUT: {{R5_PESERTA}} peserta — {{R5_OUTPUT}}.
   - CHALLENGES: {{R5_CHALLENGE}}.

7. **Erafone MOI (Mall of Indonesia)** (15 Jun 2026)
   - BRIEF: Training & demoday Air, Air SE, Ultra, SR-C series.
   - OUTPUT: {{MOI_PESERTA}} peserta — {{MOI_OUTPUT}}.
   - CHALLENGES: {{MOI_CHALLENGE}}.

8. **Divider** — "Bagian 2 · Merchandising & Branding".

9. **POP Material Air & Air SE** (10–13 Jun 2026)
   - BRIEF: Desain POP material hero product Air & Air SE + versi informatif harga untuk display Erafone.
   - OUTPUT: {{POP_OUTPUT}}.
   - CHALLENGES: {{POP_CHALLENGE}}.

10. **Visual Branding 4 Toko** (target 26 Jun 2026)
    - BRIEF: Produksi & pemasangan visual branding Saramonic di 4 toko Erafone: Bintaro Xchange, Ruko Kemang, Kelapa Gading, Mall of Indonesia.
    - OUTPUT: {{BRANDING_OUTPUT}}.
    - CHALLENGES: {{BRANDING_CHALLENGE}}.

11. **Divider** — "Bagian 3 · Dealer Program & Promo".

12. **Aktivasi Promo** (Mei–Jul 2026)
    - BRIEF: PAYDAY Promo (25 Mei–6 Jun), Double Date 5.5, dan Payday Sharing (25 Jun–7 Jul) di channel Erafone.
    - OUTPUT: {{PROMO_OUTPUT}}.
    - CHALLENGES: {{PROMO_CHALLENGE}}.

13. **KOL Visit Program ke Erafone** (on-progress)
    - BRIEF: 6 KOL aktivasi kunjungi toko Erafone & buat konten — offline (rizalhamzahnasution, technoboy.10, Akkang Heyhe, endrilost) + online (rhyndutech, Priscilia Tanbayong).
    - OUTPUT: {{KOL_OUTPUT}}.
    - CHALLENGES: {{KOL_CHALLENGE}}.

14. **PWP Bundling (OPPO/VIVO)** (on-progress)
    - BRIEF: Setup Purchase-With-Purchase — bundling Saramonic dengan pembelian OPPO/VIVO di Erafone.
    - OUTPUT: {{PWP_OUTPUT}}.
    - CHALLENGES: {{PWP_CHALLENGE}}.

15. **Divider** — "Bagian 4 · Content & Collaboration".

16. **Podcast & Live Session Erafone R5** (upcoming — 25 Jun 2026)
    - BRIEF: Sesi podcast + live session kolaborasi dengan Erafone Region 5.
    - OUTPUT (target): {{PODCAST_TARGET}}.
    - CHALLENGES / catatan: {{PODCAST_CHALLENGE}}.

17. **Key Learnings & Next Step** — 3–4 poin pembelajaran utama dari aktivitas Mei–Jun + rekomendasi Phase 2 (lanjutan training, scale branding, perluas KOL). Tutup dengan kalimat komitmen partnership Saramonic × Erafone.

Pastikan deck satu file HTML mandiri, bisa dibuka di browser, tanpa dependency eksternal. Beri tombol/indikator navigasi & nomor slide.

---

## BAGIAN 4 — Step-by-Step buat Kenny

1. **Kumpulin material** (15–20 menit): buka folder dokumentasi, isi tiap `{{...}}` di BAGIAN 2. Prioritas: angka peserta + challenge tiap aktivitas (itu inti yang diminta). Foto bisa belakangan.
2. **Tentukan angka Executive Summary**: total peserta = jumlahin 4 sesi training. Sales highlight opsional — kalau sensitif buat partner, skip aja.
3. **Replace placeholder di BAGIAN 3** dengan angka asli. Yang nggak ada datanya tulis "menyusul" atau hapus barisnya.
4. **Run di Claude Design**: paste BAGIAN 3. Tunggu deck jadi.
5. **Pasang foto**: ganti tiap placeholder "Foto: [...]" — bisa drag foto atau minta Claude Design ganti per slide.
6. **Review tone partner**: cek bagian Challenges — buat audience partner, frame challenge sebagai "kendala + solusi yang sudah/akan dijalankan", bukan keluhan. Saya bisa bantu reword kalau kamu kasih draft kasarnya.
7. **Finalize**: export/simpan. Kalau mau versi PDF buat kirim, tinggal print-to-PDF dari browser.

---

## Catatan & flag dari saya

- **Challenges = bagian paling rawan.** Untuk audience partner Erajaya, hindari nyalahin pihak Erafone. Pola aman: *"Kendala X → langkah yang kami ambil Y."* Kasih saya draft kasar challenge per aktivitas, nanti saya poles sesuai Writing Rules.
- **Sales number ke partner**: hati-hati. Sell-in/sell-out internal jangan diumbar kecuali kamu memang mau. Default saya: tampilkan capaian aktivitas (peserta, toko, konten), bukan angka revenue.
- **Dealer non-Erafone** (JPC Kemang, MegaPiksel, Wewe Ponsel) sengaja saya keluarkan karena scope Erafone-only. Bilang kalau mau dimasukin sebagai konteks Erajaya group.
- Tanggal Sedayu & R5 saya tandai "awal Jun / ~6 Jun" — konfirmasi tanggal pastinya kalau perlu akurat.
