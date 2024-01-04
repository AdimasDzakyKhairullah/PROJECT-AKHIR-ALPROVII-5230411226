import sqlite3


koneksi = sqlite3.connect('HEWAN.db')
kursor = koneksi.cursor()


kursor.execute("SELECT * FROM HEWAN ORDER BY nama_hewan ASC")  # ASC|DESC
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
