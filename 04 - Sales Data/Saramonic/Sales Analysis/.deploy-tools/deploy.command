#!/bin/bash
# ============================================================
# Deploy Saramonic Sales Dashboard -> Netlify
# Pakai curl + shasum bawaan macOS. TIDAK butuh Node / Netlify CLI.
# Dipanggil manual (double-click) atau otomatis via launchd.
# ============================================================
set -euo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
DEPLOY_DIR="$HERE/../_deploy"
SITE_ID="10c95e90-47ad-48b4-a200-9c43579ccf67"
TOKEN_FILE="$HERE/.netlify-token"

if [ ! -f "$TOKEN_FILE" ]; then
  echo "ERROR: file token belum ada: $TOKEN_FILE"
  echo "Buat Personal Access Token di Netlify, lalu paste ke file itu."
  exit 1
fi
TOKEN="$(tr -d ' \t\r\n' < "$TOKEN_FILE")"

if [ ! -f "$DEPLOY_DIR/index.html" ]; then
  echo "ERROR: $DEPLOY_DIR/index.html tidak ditemukan. Jalankan refresh dashboard dulu."
  exit 1
fi

cd "$DEPLOY_DIR"
SHA=$(shasum index.html | awk '{print $1}')

echo "[1/2] Membuat deploy baru di Netlify..."
CREATE=$(curl -s -X POST \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d "{\"files\":{\"/index.html\":\"$SHA\"}}" \
  "https://api.netlify.com/api/v1/sites/$SITE_ID/deploys")

DEPLOY_ID=$(printf '%s' "$CREATE" | grep -o '"id":"[^"]*"' | head -1 | cut -d'"' -f4)

if [ -z "$DEPLOY_ID" ]; then
  echo "ERROR: gagal membuat deploy. Cek token / koneksi. Respons Netlify:"
  echo "$CREATE"
  exit 1
fi

echo "[2/2] Upload index.html (deploy $DEPLOY_ID)..."
curl -s -X PUT \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/octet-stream" \
  --data-binary @index.html \
  "https://api.netlify.com/api/v1/deploys/$DEPLOY_ID/files/index.html" > /dev/null

STAMP=$(date "+%Y-%m-%d %H:%M:%S")
echo "OK [$STAMP] Dashboard live -> https://saramonic-salesdashboard.netlify.app"
