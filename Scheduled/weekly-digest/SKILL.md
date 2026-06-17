---
name: weekly-digest
description: Weekly digest Senin — sales Saramonic + Todoist tasks Saramonic & BOYA
---

Kamu sedang menjalankan Weekly Digest otomatis untuk Kenny (KENNKAI), Brand Manager Saramonic Indonesia dan BOYA Indonesia.

TUJUAN: Sajikan ringkasan mingguan yang mencakup data sales Saramonic dan overview task Todoist kedua brand.

LANGKAH:
1. Baca konteks brand dari: /Users/ken/Documents/KEN Work Stack/SRBY-WorkVault/01 - About/Brand Context.md
2. Baca ongoing project dari: /Users/ken/Documents/KEN Work Stack/SRBY-WorkVault/01 - About/Memory.md
3. Cari data sales Saramonic minggu ini — cek folder: /Users/ken/Documents/KEN Work Stack/SRBY-WorkVault/04 - Sales Data/Saramonic/SR Sales Data Cari file terbaru dengan data sales mingguan/bulanan Saramonic.
4. Query Todoist via MCP:
   a. Task completed minggu lalu (7 hari ke belakang) — Saramonic + BOYA
   b. Task due minggu ini (7 hari ke depan) — Saramonic + BOYA
   c. Task overdue (belum selesai, due date lewat)

FORMAT OUTPUT (Bahasa Indonesia):
---
**📊 Weekly Digest — Minggu [DD MMM YYYY]**

**💰 Saramonic Sales Minggu Ini**
[Ringkasan angka sales dari file yang ditemukan: total, top SKU, vs minggu lalu jika tersedia]
Kalau data tidak ditemukan: "⚠️ Data sales tidak ditemukan di folder 04 - Sales Data. Perlu update manual."

**✅ Completed Minggu Lalu**
Saramonic:
- [task 1]
BOYA:
- [task 1]
Kalau kosong: "(Tidak ada)"

**📋 Task Minggu Ini**
Saramonic:
- [task + due date + priority]
BOYA:
- [task + due date + priority]
Kalau kosong: "(Tidak ada)"

**⚠️ Overdue**
[Task melewati due date yang belum selesai]
Kalau kosong: "(Tidak ada)"

**🎯 Weekly Focus**
[2–3 prioritas strategis minggu ini berdasarkan data di atas — singkat, actionable]
---

ATURAN:
- Bahasa Indonesia, direct, no fluff
- Jangan ngarang angka sales — kalau data tidak ada, bilang eksplisit
- Kalau Todoist MCP tidak tersedia, tulis: "⚠️ Todoist tidak bisa diakses. Cek langsung di Todoist."
- Timezone: WIB (UTC+7)
- Format tanggal: DD MMM YYYY

OUTPUT FILE:
Setelah konten digest selesai dibuat, simpan sebagai file .md ke:
  /Users/ken/Documents/KEN Work Stack/SRBY-WorkVault/05 - Digest/Weekly Digest/[YYYY-MM-DD].md
  (gunakan tanggal Senin minggu ini sebagai nama file, contoh: 2026-06-09.md)
Buat folder jika belum ada. Tulis konten digest lengkap ke file tersebut.