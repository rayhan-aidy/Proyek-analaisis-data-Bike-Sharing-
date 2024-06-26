# Dicoding Proyek Analisis Data

Proyek ini merupakan implementasi dari analisis data menggunakan Streamlit. Proyek ini bertujuan untuk memberikan wawasan mengenai pola penggunaan berbagi sepeda berdasarkan berbagai faktor seperti musim, cuaca, waktu, dan jenis pengguna.

## Persyaratan

- Python 3.x
- Pip (Python package installer)
- Virtual environment (opsional tetapi direkomendasikan)

## Langkah-langkah Instalasi

### 1. Clone Repository

Clone repository ini ke dalam direktori lokal Anda:

```sh
git clone https://github.com/username/repo.git
cd repo
```

### 2. Buat dan Aktifkan Virtual Environment

Disarankan untuk menggunakan virtual environment agar dependensi proyek terisolasi dari sistem Anda. Buat dan aktifkan virtual environment dengan perintah berikut:

#### Untuk Windows:

```sh
python -m venv nama_venv
.\nama_venv\Scripts\activate
```

#### Untuk macOS/Linux:

```sh
python3 -m venv nama_venv
source nama_venv/bin/activate
```

### 3. Instal Dependensi

Instal semua dependensi yang diperlukan menggunakan `requirements.txt`. Jika Anda belum memiliki file `requirements.txt`, Anda bisa membuatnya dengan `pipreqs` atau menambahkannya secara manual.

Jika Anda sudah memiliki file `requirements.txt`, jalankan perintah berikut:

```sh
pip install -r requirements.txt
```

Jika belum memiliki file `requirements.txt`, buat file tersebut dengan menggunakan `pipreqs`:

```sh
pip install pipreqs
pipreqs /path/to/your/project
```

### 4. Jalankan Aplikasi Streamlit

Setelah semua dependensi terinstal, jalankan aplikasi Streamlit dengan perintah berikut:

```sh
cd dashboard
streamlit run app.py
```

## Struktur Direktori

Berikut adalah struktur direktori proyek ini:

```
repo/
├── nama_venv/
├── app.py
├── requirements.txt
└── README.md
```

## Penjelasan Kode

Aplikasi Streamlit ini memiliki dua halaman utama: Home dan Another Page. Pada halaman Home, ditampilkan gambar dan beberapa informasi terkait pola penggunaan berbagi sepeda. Halaman ini menggunakan pustaka PIL untuk memanipulasi gambar.

### Contoh Kode `app.py`

```python
import streamlit as st
from PIL import Image
import requests
from io import BytesIO

# URL unduhan langsung Google Drive
url = 'https://drive.google.com/uc?export=download&id=1iK0iM1KvdDS7O-IiV8xEgDvJZt_X5wss'

# Mengunduh gambar
response = requests.get(url)
response.raise_for_status()  # Memastikan permintaan berhasil

# Simpan gambar ke disk
image_path = 'downloaded_image.jpg'
with open(image_path, 'wb') as f:
    f.write(response.content)

# Streamlit App
page = st.sidebar.selectbox('Select a page:', ['Home', 'Another Page'])

if page == 'Home':
    st.header('Welcome to the Bike Sharing Dashboard!')
    
    # Buka gambar yang sudah diunduh
    image = Image.open(image_path)
    
    # Tampilkan gambar di Streamlit
    st.image(image, caption='Bike Sharing', use_column_width=True)
    
    st.write('This dashboard provides insights into bike sharing usage patterns based on various factors such as season, weather, time of day, and user type.')
else:
    st.header('Another Page')
    st.write('Content for another page goes here.')
```

Dengan mengikuti langkah-langkah di atas, Anda akan dapat menjalankan aplikasi Streamlit ini dan menjelajahi pola penggunaan berbagi sepeda berdasarkan berbagai faktor.



Dengan README ini, pengguna dapat dengan mudah menyiapkan lingkungan pengembangan dan menjalankan aplikasi Streamlit.
