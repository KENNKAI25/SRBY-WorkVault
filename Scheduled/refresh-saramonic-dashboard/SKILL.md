---
name: refresh-saramonic-dashboard
description: Auto-refresh Saramonic Sales Dashboard artifact dari data lokal SR Sales Data setiap pagi.
---

Tugas: refresh "Saramonic Sales Dashboard" dari data sales lokal terbaru. Balas dalam Bahasa Indonesia, ringkas.

LANGKAH:
1. Jalankan build script via tool bash (mcp__workspace__bash):
   python3 "$(ls /sessions/*/mnt/SRBY-WorkVault/04*/Saramonic/Sales*/.dashboard_build/build_dashboard.py | head -1)"
   Script ini otomatis membaca 4 file di "04 - Sales Data/Saramonic/SR Sales Data/" (Sales by SKU & Dealer, QTY & Value) + "Saramonic Stock Data.md", lalu me-regenerate file dashboard HTML. Di stdout dia akan print satu baris ringkasan (diawali "OK ...") dan satu baris "OUTPUT_HTML=<path>".

2. Kalau script ERROR (mis. file hilang / format tabel berubah / "placeholder not replaced"): JANGAN update artifact. Laporkan errornya ke user dengan jelas + saran cek format file. Stop di sini.

3. Kalau sukses: ambil path setelah "OUTPUT_HTML=" dari stdout, lalu panggil tool mcp__cowork__update_artifact dengan:
   - id: "saramonic-sales-dashboard"
   - html_path: <path OUTPUT_HTML tadi>
   - update_summary: "Auto-refresh data sales terbaru"

4. Siapkan file untuk publish Netlify: copy HTML hasil regenerate ke folder deploy sebagai index.html via bash:
   cp "<path OUTPUT_HTML tadi>" "$(dirname "<path OUTPUT_HTML tadi>")/_deploy/index.html"
   (Folder _deploy ini yang dibaca oleh deploy script di Mac Kenny. Tujuannya: folder deploy selalu berisi versi dashboard terbaru.)

5. Setelah update artifact berhasil, balas singkat: konfirmasi dashboard sudah di-refresh + tanggal/grand total dari baris "OK" tadi. Jangan tampilkan angka dealer/SKU detail di chat (data confidential).

CATATAN DEPLOY NETLIFY:
- Sandbox Cowork TIDAK bisa push ke Netlify (network ke api.netlify.com / netlify-mcp.netlify.app diblokir — sudah dites, hasilnya fetch failed). Jadi task ini HANYA menyiapkan _deploy/index.html terbaru. JANGAN coba jalankan deploy/npx netlify di sandbox — pasti gagal.
- Push ke https://saramonic-salesdashboard.netlify.app dilakukan OTOMATIS dari Mac Kenny oleh launchd job "com.kenny.saramonic-deploy" tiap hari 08:20 (17 menit setelah refresh ini), yang menjalankan ".deploy-tools/deploy.command". Task ini cukup pastikan _deploy/index.html sudah ter-update; deploy bukan tanggung jawab task ini.

PENTING:
- Data sales = confidential. Task ini regenerate + update artifact + refresh _deploy/index.html lokal. Jangan kirim/ekspor ke channel lain.
- Jangan edit file sumber di SR Sales Data. Script hanya MEMBACA file sumber dan MENULIS file dashboard HTML output.
- Jangan ubah build_dashboard.py atau template.html kecuali user minta eksplisit.