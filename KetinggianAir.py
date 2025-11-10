import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# === 1. Baca dataset DWLR ===
data = pd.read_csv("DWLR_Dataset_2023.csv")

# Bersihkan data kosong
data = data.dropna(subset=['Water_Level_m', 'Rainfall_mm', 'Temperature_C'])

# Pastikan kolom sesuai dataset
data['Date'] = pd.to_datetime(data['Date'])
data = data.sort_values('Date')

# === 2. Ambil kolom utama ===
t = np.arange(len(data))
h = data['Water_Level_m']
rain = data['Rainfall_mm']
temp = data['Temperature_C']

# === 3. Hitung rata-rata dan simulasi dasar ===
h_avg = np.mean(h)
r = 0.001
h_sim_base = h_avg * np.exp(r * t)

# === 4. Tambahkan pengaruh curah hujan dan suhu ===
rain_effect = 0.01 * (rain - np.mean(rain))
temp_effect = -0.005 * (temp - np.mean(temp))
h_sim = h_sim_base + rain_effect + temp_effect

# === 5. Plot hasil simulasi ===
plt.figure(figsize=(12, 6))
plt.plot(data['Date'], h, label='Data Aktual (Tinggi Air)', color='blue', linewidth=2)
plt.plot(data['Date'], h_sim, label='Simulasi Dinamik (dengan Hujan & Suhu)', 
         color='orange', linestyle='--', linewidth=2)
plt.fill_between(data['Date'], h, h_sim, color='gray', alpha=0.2, label='Perbedaan Aktual vs Simulasi')
plt.axhline(h_avg, color='green', linestyle=':', linewidth=1.5, label=f'Rata-rata ({h_avg:.2f} m)')

# === 6. Format tampilan grafik ===
plt.title('Simulasi Sistem Dinamik: Pengaruh Hujan & Suhu terhadap Tinggi Muka Air (DWLR 2023)', fontsize=13)
plt.xlabel('Tanggal', fontsize=11)
plt.ylabel('Tinggi Muka Air (m)', fontsize=11)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.show()