# Panduan Upload ke GitHub

## 1. Buat Repository Baru
Buat repository baru di GitHub, misalnya:
```text
simple-health-api-cloud-praktikum
```

## 2. Inisialisasi Git Lokal
Jalankan perintah berikut di folder proyek:
```bash
git init
git add .
git commit -m "Menambahkan aplikasi awal"
git branch -M main
git remote add origin https://github.com/USERNAME/simple-health-api-cloud-praktikum.git
git push -u origin main
```

## 3. Riwayat Commit yang Disarankan
Agar sesuai tugas, lakukan commit bertahap seperti ini:
```bash
git add app.py requirements.txt README.md
git commit -m "Menambahkan aplikasi awal"

git add Dockerfile
git commit -m "Menambahkan Dockerfile"

git add docker-compose.yml
git commit -m "Menambahkan Docker Compose"

git add tests/test_app.py
git commit -m "Menambahkan automated test"

git add .github/workflows/ci.yml
git commit -m "Menambahkan workflow GitHub Actions"

git push origin main
```

## 4. Simulasi Pipeline Gagal
Ubah test pada `tests/test_app.py`:
```python
assert response.get_json() == {"status": "error"}
```

Lalu commit dan push:
```bash
git add .
git commit -m "Simulasi pipeline gagal"
git push origin main
```

## 5. Pipeline Berhasil
Kembalikan menjadi:
```python
assert response.get_json() == {"status": "healthy"}
```

Lalu commit dan push:
```bash
git add .
git commit -m "Memperbaiki automated test"
git push origin main
```
