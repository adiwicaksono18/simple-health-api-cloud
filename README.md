# Simple Health API - Praktikum Docker, Docker Compose, dan CI/CD

Proyek ini dibuat untuk memenuhi tugas praktikum terintegrasi materi Docker, orkestrasi sederhana menggunakan Docker Compose, dan CI/CD menggunakan GitHub Actions.

## Deskripsi Aplikasi

Aplikasi ini adalah REST API sederhana menggunakan Python Flask. Aplikasi memiliki endpoint utama, endpoint kesehatan, dan endpoint sapaan.

Endpoint:

- `GET /` menampilkan informasi aplikasi.
- `GET /health` menampilkan status aplikasi.
- `GET /api/hello/<nama>` menampilkan pesan sapaan.

## Struktur Folder

```text
cloud_docker_cicd_project/
├── app.py
├── requirements.txt
├── tests/
│   └── test_app.py
├── Dockerfile
├── docker-compose.yml
├── README.md
└── .github/
    └── workflows/
        └── ci.yml
```

## Menjalankan Aplikasi Secara Lokal

```bash
pip install -r requirements.txt
python app.py
```

Akses aplikasi:

```text
http://localhost:5000
http://localhost:5000/health
```

## Menjalankan Automated Test

```bash
pytest -v
```

## Verifikasi Docker

```bash
docker --version
docker compose version
docker run hello-world
```

## Build Docker Image

```bash
docker build -t simple-health-api:v1 .
docker images
```

## Menjalankan Container

```bash
docker run -d --name simple-health-api -p 8080:5000 simple-health-api:v1
docker ps
```

Akses aplikasi melalui browser:

```text
http://localhost:8080
http://localhost:8080/health
```

Menghentikan container:

```bash
docker stop simple-health-api
docker rm simple-health-api
```

## Menjalankan Docker Compose

```bash
docker compose up -d
docker compose ps
```

Akses aplikasi:

```text
http://localhost:8080
http://localhost:8080/health
```

Menghentikan service:

```bash
docker compose down
```

## GitHub Actions

Workflow CI berada di:

```text
.github/workflows/ci.yml
```

Pipeline menjalankan tiga proses utama:

1. Checkout source code.
2. Install dependency dan menjalankan automated test.
3. Build Docker image.

## Simulasi Pipeline Gagal

Untuk membuat pipeline gagal secara terkontrol, ubah file `tests/test_app.py`, misalnya pada bagian:

```python
assert response.get_json() == {"status": "healthy"}
```

menjadi:

```python
assert response.get_json() == {"status": "error"}
```

Kemudian lakukan commit dan push:

```bash
git add .
git commit -m "Simulasi pipeline gagal"
git push origin main
```

GitHub Actions akan gagal karena hasil endpoint `/health` tidak sesuai dengan expected output.

## Memperbaiki Pipeline

Kembalikan test menjadi:

```python
assert response.get_json() == {"status": "healthy"}
```

Lalu commit dan push kembali:

```bash
git add .
git commit -m "Memperbaiki automated test"
git push origin main
```

GitHub Actions akan berhasil setelah test dan Docker build berjalan tanpa error.
