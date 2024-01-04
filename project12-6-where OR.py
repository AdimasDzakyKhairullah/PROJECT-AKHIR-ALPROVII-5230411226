import sqlite3


koneksi = sqlite3.connect('HEWAN.db')
kursor = koneksi.cursor()

kursor.execute(
    f"SELECT * FROM HEWAN WHERE asal= 'Sumatera' OR  jmlh_sekarang>= '500'")
baris_table = kursor.fetchall()

print("Data Pegawai:")
print("==============================================================")
print("{:<5} {:<20} {:<20} {:<20} {:<10} {:<10}".format(
    "ID", "Nama Hewan", "Jenis", "Asal", "jumlah sekarang", "tahun ditemukan"))
print("--------------------------------------------------------------")
for baris in baris_table:
    print("{:<5} {:<20} {:<20} {:<20} {:<10} {:<10}".format(
        baris[0], baris[1], baris[2], baris[3], baris[4],baris[5]))

koneksi.close()
