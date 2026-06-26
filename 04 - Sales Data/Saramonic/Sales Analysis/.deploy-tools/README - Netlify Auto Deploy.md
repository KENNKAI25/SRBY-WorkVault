# Auto-Deploy Saramonic Dashboard ke Netlify

**Kenapa perlu ini:** scheduled task Cowork (08:03 tiap pagi) cuma bisa *regenerate* file dashboard di Mac kamu — dia **tidak bisa** push ke Netlify (sandbox-nya diblokir dari internet Netlify). Jadi langkah upload jalan dari Mac kamu, pakai script di folder ini. Cuma butuh `curl` (sudah bawaan macOS) — **tidak perlu install Node atau Netlify CLI.**

- Site: `saramonic-salesdashboard` → https://saramonic-salesdashboard.netlify.app
- Site ID: `10c95e90-47ad-48b4-a200-9c43579ccf67`

---

## Setup sekali aja (~3 menit)

### 1. Bikin Netlify Personal Access Token
1. Buka https://app.netlify.com/user/applications#personal-access-tokens
2. Klik **New access token** → kasih nama (mis. `dashboard-deploy`) → **Generate token**
3. **Copy** token-nya (ini cuma muncul sekali).

### 2. Simpan token ke file
1. Di folder `.deploy-tools`, buat file baru bernama **`.netlify-token`** (persis, pakai titik di depan).
2. Paste token-nya ke dalam file itu, simpan. Isinya cuma 1 baris token, gak ada yang lain.

### 3. Jadikan script bisa dijalankan
Buka **Terminal**, paste baris ini, Enter:
```
chmod +x "/Users/ken/Documents/KEN Work Stack/SRBY-WorkVault/04 - Sales Data/Saramonic/Sales Analysis/.deploy-tools/deploy.command"
```

### 4. Tes
Double-click **`deploy.command`** di Finder. Kalau muncul `OK ... Dashboard live -> ...` berarti sukses. Buka URL-nya untuk cek.

> Kalau macOS bilang "cannot be opened" (developer tak dikenal): klik kanan file → **Open** → **Open**. Cukup sekali.

---

## Pilihan cara update

### Opsi A — Manual 1 klik (paling simpel)
Tiap habis refresh pagi (atau kapan pun mau update link publik), double-click **`deploy.command`**. Selesai ~10 detik.

### Opsi B — Full auto (set & lupakan)
Mac kamu otomatis deploy tiap hari jam **08:20** (15 menit setelah refresh Cowork). Setup sekali:
```
cp "/Users/ken/Documents/KEN Work Stack/SRBY-WorkVault/04 - Sales Data/Saramonic/Sales Analysis/.deploy-tools/com.kenny.saramonic-deploy.plist" ~/Library/LaunchAgents/
launchctl load ~/Library/LaunchAgents/com.kenny.saramonic-deploy.plist
```
Catatan: jam 08:20 Mac harus nyala (gak harus log-in, tapi jangan mati). Kalau lagi sleep, launchd jalan pas Mac bangun. Log hasil ada di `.deploy-tools/deploy.log`.

Mau matiin auto:
```
launchctl unload ~/Library/LaunchAgents/com.kenny.saramonic-deploy.plist
```

---

## ⚠️ Penting: data ini confidential, URL-nya publik
`saramonic-salesdashboard.netlify.app` sekarang **bisa diakses siapa pun yang punya link** — termasuk angka sales internal. Saran: aktifkan **password protection**. (Di Netlify free plan fitur ini terbatas; minta Kenny/Claude cek opsi password atau upgrade kalau perlu.) Jangan sebar URL di luar yang seharusnya.

## Keamanan token
File `.netlify-token` = kunci akses ke akun Netlify kamu. Jangan commit ke Git, jangan share. Script sengaja taruh token di luar folder `_deploy/` supaya **tidak ikut ke-upload** ke Netlify.
