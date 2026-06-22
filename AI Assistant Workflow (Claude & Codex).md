# AI Assistant Workflow — Claude & Codex

> Panduan pribadi Kenny untuk memilih AI assistant yang tepat. File ini dinamis, boleh diubah kapan pun kalau workflow berubah.

*Last updated: 2026-06-22*

---

## 1. Prinsip Utama

Gunakan assistant berdasarkan jenis kerja, bukan berdasarkan kebiasaan.

- **Claude** dipakai untuk kerja kreatif, analisis, dan bikin app lokal.
- **Codex** dipakai untuk baca/edit file, cek dokumen, OCR PDF, dan jadi opsi kedua saat Claude usage penuh.
- Kalau output akan dipakai untuk kerja brand Saramonic/BOYA, tetap ikuti instruksi di `AGENTS.md` dan folder `01 - About/`.

---

## 2. Pakai Claude Untuk

### 2.1 Image Generation untuk Social Media Content

Gunakan Claude saat butuh:

- Konsep visual untuk Instagram/TikTok.
- Background, scene, product mood, atau image generation untuk konten sosial.
- Variasi visual dari satu brief.
- Eksplorasi gaya visual sebelum masuk Figma/Canva.

Catatan:

- Untuk konten brand, tetap cek `01 - About/Brand Context.md`.
- Untuk produk fisik, pastikan ada foto referensi asli kalau output harus akurat.
- Untuk teks panjang di dalam gambar, lebih aman render manual di Figma/Canva.

### 2.2 Data Analysis

Gunakan Claude saat butuh:

- Membaca pola dari data marketing/sales.
- Membuat insight, summary, rekomendasi, dan action plan.
- Membandingkan performance campaign, dealer, channel, atau SKU.
- Menyusun report yang butuh interpretasi bisnis.

Catatan:

- Untuk data marketing activity, sumber utama tetap Todoist.
- Untuk sales/pricing, pakai file sumber resmi di workspace.
- Kalau angka berdampak ke budget atau keputusan partner, minta Claude tunjukkan asumsi dan sumber datanya.

### 2.3 Local Apps Creation

Gunakan Claude saat butuh bikin:

- Dashboard lokal.
- Matrix decision tool.
- Tracker interaktif.
- Visualisasi data.
- App internal sederhana untuk kerja marketing/sales.

Contoh:

- Dealer performance dashboard.
- Campaign priority matrix.
- KOL scoring tool.
- Sell-in / sell-out tracker.

---

## 3. Pakai Codex Untuk

### 3.1 File Reader: PDF, Excel, PPT

Gunakan Codex saat butuh:

- Baca isi PDF, Excel, PowerPoint, Word, atau file lokal lain.
- Extract tabel, slide, isi dokumen, atau struktur file.
- Edit file langsung di workspace.
- Convert atau rapikan format dokumen.

Catatan:

- Codex lebih cocok untuk kerja yang butuh akses file lokal dan perubahan file yang jelas.
- Kalau revisi dokumen besar, buat versi baru: `_v2`, `_revisi`, atau tanggal.

### 3.2 PDF OCR Check dan Matching Tools

Gunakan Codex saat butuh:

- Cek apakah PDF bisa dibaca teksnya atau perlu OCR.
- Bandingkan hasil OCR dengan file asli.
- Matching data dari PDF ke Excel/Sheet.
- Cek konsistensi angka, nama produk, SKU, harga, atau row data.

Contoh:

- Cocokkan invoice PDF dengan price list.
- Cek apakah angka di report PDF sama dengan Excel source.
- Extract tabel dari PDF scan lalu validasi ulang.

### 3.3 Second AI Assistant Saat Claude Usage Full

Gunakan Codex sebagai backup saat:

- Claude limit/usage penuh.
- Task harus tetap jalan hari itu.
- Task tidak butuh image generation Claude secara spesifik.
- Task lebih cocok dikerjakan via file lokal, dokumen, atau coding ringan.

Cara pindah:

1. Copy konteks task dari Claude.
2. Tambahkan file yang perlu dibaca.
3. Jelaskan output yang dibutuhkan.
4. Kalau ada draft Claude sebelumnya, minta Codex lanjutkan, bukan mulai dari nol.

---

## 4. Quick Decision Matrix

| Kebutuhan | Assistant Utama | Backup |
| --- | --- | --- |
| Image generation social media | Claude | Codex kalau hanya butuh prompt/brief |
| Visual concept exploration | Claude | Codex untuk struktur brief |
| Data analysis + insight bisnis | Claude | Codex kalau datanya file lokal |
| Dashboard / matrix / local app | Claude | Codex untuk debugging/edit file |
| Baca PDF/Excel/PPT | Codex | Claude kalau hanya perlu summary ringan |
| OCR PDF + cek hasil | Codex | - |
| Matching PDF ke Excel | Codex | - |
| Edit file workspace | Codex | Claude kalau edit ringan dan tidak butuh file tool |
| Claude usage full | Codex | - |

---

## 5. Switching Rule

Pindah assistant kalau salah satu kondisi ini terjadi:

- Assistant utama tidak punya tool yang dibutuhkan.
- Usage limit penuh.
- Output butuh akses file lokal yang lebih kuat.
- Task berubah dari ide kreatif menjadi eksekusi file.
- Task berubah dari edit file menjadi eksplorasi visual atau image generation.

Jangan paksakan satu assistant untuk semua kerja. Pilih yang paling cocok untuk tahap kerja saat itu.

---

## 6. Template Prompt Saat Pindah Assistant

```text
Saya pindah dari [Claude/Codex] ke sini karena [alasan].

Konteks:
- [ringkasan task]
- [brand/proyek terkait]
- [file yang perlu dibaca]

Yang sudah dikerjakan:
- [draft/hasil sebelumnya]

Yang saya butuh sekarang:
- [output final]
- [format file/output]
- [deadline/constraint]
```

---

## 7. Update Rule

Update file ini kalau:

- Ada tool baru yang lebih cocok untuk workflow tertentu.
- Claude/Codex berubah kemampuan.
- Ada workflow baru yang sering dipakai.
- Ada batasan baru, misalnya limit usage, output kurang stabil, atau format file berubah.

Format update:

- Tambah use case baru di bagian Claude atau Codex.
- Jangan hapus rule lama kecuali memang sudah tidak relevan.
- Kalau ragu, tambah catatan pendek di section terkait.
