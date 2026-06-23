# SR — Claude Design Prompt — Erafone Activity Report (Mei–Jun 2026)

> **Tujuan file ini:** prompt siap-pakai untuk **Claude Design** buat generate presentasi visual (HTML deck) aktivitas Saramonic di Erafone sejak Mei 2026.
> **Audience deck:** Partner Erajaya / Erafone → tone partnership, hasil + komitmen.
> **Bahasa deck:** Bahasa Indonesia. **Scope:** Erafone-only. **Format:** visual deck 16:9.
> **Versi:** ringkas — 1 topik = 1 slide.
>
> **Cara pakai:** (1) lengkapi placeholder `{{...}}` di BAGIAN 2 · (2) copy BAGIAN 3 → paste ke Claude Design · (3) pasang foto · (4) review & revisi.
>
> *Dibuat: 2026-06-23. Data: Todoist (project Saramonic) + input Kenny.*

---

## BAGIAN 1 — Struktur Deck (9 slide)

| # | Slide | Isi |
|---|-------|-----|
| 1 | Cover | Judul, periode, logo Saramonic × Erafone |
| 2 | Executive Summary | Metrik besar: 4 training · 4 toko branding · 6 KOL · 21 peserta |
| 3 | Erafone Training | Brief (4 toko) / Output / Challenges |
| 4 | Visual Branding | Brief (4 toko) / Output / Challenges |
| 5 | Dealer Program | Brief (special price & discount Erafone) / Output / Challenges |
| 6 | Special Purchase Program & Voucher | Brief (bundling Blink900 + voucher Indomaret) / Output / Challenges |
| 7 | Marketing Activity | Brief (PWP, Cross Brand Workshop, KOL, dll.) / Output / Challenges |
| 8 | Content & Collaboration | Brief (Podcast R5) / Output / Challenges |
| 9 | Key Learnings & Next Step | Ringkasan + rekomendasi Phase 2 |

> Tiap slide topik pakai 3 blok tetap: **Brief** · **Output** · **Challenges**. Sub-item disebut singkat di dalam slide, bukan dipecah jadi slide sendiri.

---

## BAGIAN 2 — THE PROMPT (copy-paste ke Claude Design)
---

Buatkan **presentasi visual (HTML deck, rasio 16:9, navigasi keyboard kiri/kanan, satu file mandiri tanpa dependency eksternal)** berisi laporan aktivitas **Saramonic × Erafone periode Mei–Juni 2026**, untuk dipresentasikan ke **partner Erajaya/Erafone**. Tone profesional, partnership, fokus hasil & komitmen. Semua teks **Bahasa Indonesia**.

**Design direction:**
- Tema gelap/charcoal premium, aksen oranye Saramonic. Pro-audio look: bersih, tegas, banyak ruang kosong.
- Tipografi sans-serif modern, hierarki kuat (angka besar untuk metrik).
- Tiap slide topik pakai layout 3 blok konsisten berlabel **BRIEF**, **OUTPUT**, **CHALLENGES** (CHALLENGES beri warna aksen berbeda).
- Slot gambar placeholder ("Foto: [nama]") di slide yang butuh foto — saya ganti nanti.
- Header tiap slide: logo Saramonic kiri, "× Erafone" kanan, nomor + total slide.

**Susunan slide (9):**

1. **Cover** — "Saramonic × Erafone — Activity Report" · subjudul "Periode Mei–Juni 2026" · ruang logo Saramonic & Erafone.

2. **Executive Summary** — 4 metrik besar: **4** sesi training · **4** toko di-branding · **6** KOL aktivasi · **21** peserta dilatih. Tambah 1 kalimat ringkas pencapaian. 

3. **Erafone Training**
   - BRIEF: Training & demoday produk Air, Air SE, Ultra, dan SR-C series untuk staff ERO di 4 toko Erafone — Region 1 Margonda, Region 1 Sedayu, Region 5, dan MOI (Mei–Jun 2026).
   - OUTPUT: 21 staff dilatih (Margonda 6 · Sedayu 5 · Region 5 — 5 · MOI 5); seluruh peserta memahami key selling point utama & cara menjual tiap produk.
   - CHALLENGES: Jumlah peserta per sesi relatif sedikit, sehingga transfer knowledge ke ERO lain belum optimal — perlu sesi lanjutan / materi mandiri untuk perluasan.

4. **Visual Branding 4 Toko**
   - BRIEF: Produksi & pemasangan visual branding Saramonic di 4 toko Erafone: Bintaro Xchange, Ruko Kemang, Kelapa Gading, dan Mall of Indonesia.
   - OUTPUT: Better visibility untuk Saramonic & juga demo untuk
   - CHALLENGES: {{BRANDING_CHALLENGE}}.

5. **Dealer Program**
   - BRIEF: Program harga khusus & diskon untuk Erafone — PAYDAY (25 Mei–6 Jun), Double Date 5.5, dan Payday Sharing (25 Jun–7 Jul).
   - OUTPUT: Membantu sell-out SKU Saramonic di Erafone

6. **Special Purchase Program & Voucher**
   - BRIEF: Insentif pembelian & reward sell-out untuk Erafone — (1) Bundling: beli 500 pcs Saramonic Air / Air SE gratis 20 pcs Blink900 B2TG (nilai ≈ Rp 80 juta); (2) Voucher Indomaret Rp 500.000 untuk tiap toko yang mencapai target sell-out Rp 20 juta/toko.

7. **Marketing Activity** (tampilkan sub-poin dalam 1 slide)
   - BRIEF: Inisiatif marketing pendukung di Erafone — (1) PWP Bundling: Purchase-With-Purchase Saramonic dengan pembelian OPPO/VIVO; (2) Cross Brand Workshop: {{WORKSHOP_BRIEF}}; (3) KOL Visit Program: 6 KOL kunjungi toko Erafone & buat konten (offline + online).
   - OUTPUT: PWP — {{PWP_OUTPUT}}; Workshop — {{WORKSHOP_OUTPUT}}; KOL — {{KOL_OUTPUT}}.
   - CHALLENGES: {{PWP_CHALLENGE}} / {{WORKSHOP_CHALLENGE}} / {{KOL_CHALLENGE}}.

8. **Content & Collaboration**
   - BRIEF: Podcast & Live Session kolaborasi dengan Erafone Region 5 (terjadwal 25 Jun 2026).
   - OUTPUT (target): {{PODCAST_TARGET}}.
   - CHALLENGES / catatan: {{PODCAST_CHALLENGE}}.

9. **Key Learnings & Next Step** — 3–4 poin pembelajaran utama dari aktivitas Mei–Jun + rekomendasi Phase 2 (sesi training lanjutan untuk perluasan ERO, scale visual branding, perluas KOL & cross-brand). Tutup dengan kalimat komitmen partnership Saramonic × Erafone.


