import sqlite3

# Membuat koneksi ke database atau membuat database baru jika belum ada
koneksi = sqlite3.connect('HEWAN.db')
kursor = koneksi.cursor()

# Menjalankan query SELECT dengan LIKE
nama = 'B%'  # Mencari nama yang dimulai dengan 'John'
kursor.execute(f"SELECT * FROM HEWAN WHERE nama_hewan LIKE ?", (nama,))
tabel_hewan = kursor.fetchall()

print("Data Hewan:")
print("==============================================================")
print("{:<5} {:<20} {:<20} {:<20} {:<10} {:<10}".format(
    "ID", "Nama Hewan", "Jenis", "Asal", "jumlah sekarang", "tahun ditemukan"))
print("--------------------------------------------------------------")
for baris in tabel_hewan:
    print("{:<5} {:<20} {:<20} {:<20} {:<10} {:<10}".format(
        baris[0], baris[1], baris[2], baris[3], baris[4],baris[5]))

koneksi.close()
