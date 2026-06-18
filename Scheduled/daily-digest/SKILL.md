---
name: daily-digest
description: Daily digest — Todoist tasks Saramonic & BOYA + highlight hari ini
---

Kamu sedang menjalankan Daily Digest otomatis untuk Kenny (KENNKAI), Brand Manager Saramonic Indonesia dan BOYA Indonesia.

TUJUAN: Tarik data task hari ini dari Todoist dan sajikan sebagai daily digest yang ringkas dan actionable.

LANGKAH:
1. Query Todoist via MCP — gunakan find-tasks dengan filter string Todoist per project. Jalankan 4 query secara parallel:
   a. Saramonic today + overdue:       filter = "##Saramonic & (today | overdue)"
   b. BOYA today + overdue:            filter = "##BOYA & (today | overdue)"
   c. Saramonic high priority 3 hari:  filter = "##Saramonic & (p1 | p2) & 3 days & !today"
   d. BOYA high priority 3 hari:       filter = "##BOYA & (p1 | p2) & 3 days & !today"

   PENTING: Gunakan tool find-tasks (BUKAN find-tasks-by-date) dengan parameter "filter".
   JANGAN query project lain — filter ##Saramonic dan ##BOYA sudah menjamin scope-nya.

2. Dari hasil query (a) dan (b), pisahkan:
   - Task due hari ini (dueDate == tanggal hari ini)
   - Task overdue (dueDate < tanggal hari ini)

3. Hasil query (c) dan (d) = High Priority 3 hari ke depan.

4. Gabungkan semua hasil dan format sesuai template di bawah.

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
Kalau kosong per brand: "(Tidak ada)"

**⚡ High Priority (3 Hari ke Depan)**
[Task p1/p2 yang due dalam 3 hari ke depan (tidak termasuk hari ini), belum selesai — hanya dari Saramonic & BOYA]
Kalau kosong: "(Tidak ada)"

**💡 Focus Hari Ini**
[2–3 poin actionable berdasarkan data di atas — singkat, langsung ke poin]
---

ATURAN:
- Bahasa Indonesia, direct, no fluff
- Hanya tampilkan task dari project Saramonic dan BOYA — abaikan semua project lain
- Jangan sertakan task yang sudah completed
- Kalau Todoist MCP tidak tersedia, tulis eksplisit: "⚠️ Todoist tidak bisa diakses. Cek langsung di Todoist."
- Timezone: WIB (UTC+7)

OUTPUT FILE:
Setelah konten digest selesai dibuat, simpan sebagai file .md ke:
  /Users/ken/Documents/KEN Work Stack/SRBY-WorkVault/05 - Digest/Daily Digest/[YYYY-MM-DD].md
  (gunakan tanggal hari ini sebagai nama file, contoh: 2026-06-09.md)
Buat folder jika belum ada. Tulis konten digest lengkap ke file tersebut.