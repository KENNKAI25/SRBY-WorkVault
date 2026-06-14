---
name: daily-digest
description: Daily digest — Todoist tasks Saramonic & BOYA + highlight hari ini
---

Kamu sedang menjalankan Daily Digest otomatis untuk Kenny (KENNKAI), Brand Manager Saramonic Indonesia dan BOYA Indonesia.

TUJUAN: Tarik data task hari ini dari Todoist dan sajikan sebagai daily digest yang ringkas dan actionable.

LANGKAH:
1. Query Todoist via MCP — ambil semua task yang due hari ini untuk semua project Saramonic dan BOYA.
2. Cek juga task yang overdue (belum selesai, due date sudah lewat).
3. Cek task prioritas tinggi (p1/p2) yang due dalam 3 hari ke depan.

FORMAT OUTPUT (Bahasa Indonesia):
---
**📅 Daily Digest — [Tanggal hari ini, format: DD MMM YYYY]**

**🔴 Overdue**
[List task yang melewati due date — nama task, project/brand, due date asli]
Kalau kosong: "(Tidak ada)"

**📌 Due Hari Ini**
Saramonic:
- [task 1]
- [task 2]

BOYA:
- [task 1]
Kalau kosong: "(Tidak ada)"

**⚡ High Priority (3 Hari ke Depan)**
[Task p1/p2 yang due dalam 3 hari, belum selesai]
Kalau kosong: "(Tidak ada)"

**💡 Focus Hari Ini**
[2–3 poin actionable berdasarkan data di atas — singkat, langsung ke poin]
---

ATURAN:
- Bahasa Indonesia, direct, no fluff
- Jangan sertakan task yang sudah completed
- Kalau Todoist MCP tidak tersedia, tulis eksplisit: "⚠️ Todoist tidak bisa diakses. Cek langsung di Todoist."
- Timezone: WIB (UTC+7)

OUTPUT FILE:
Setelah konten digest selesai dibuat, simpan sebagai file .md ke:
  /Users/ken/Documents/KEN Work Stack/SRBY-WorkVault/05 - Digest/Daily Digest/[YYYY-MM-DD].md
  (gunakan tanggal hari ini sebagai nama file, contoh: 2026-06-09.md)
Buat folder jika belum ada. Tulis konten digest lengkap ke file tersebut.