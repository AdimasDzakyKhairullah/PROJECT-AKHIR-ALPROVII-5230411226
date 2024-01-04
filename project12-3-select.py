import sqlite3

conn = sqlite3.connect('HEWAN.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM HEWAN")
tabel_hewan = cursor.fetchall()

print("Data Nama Hewan:")
print("==============================================================================================================")
print("{:<5} {:<20} {:<20} {:<20} {:<10} {:<5}".format(
    "ID", "Nama Hewan","Jenis","Asal", "jumlah sekarang","tahun ditemukan"))
print("--------------------------------------------------------------------------------------------------------------")
for row in tabel_hewan:
    print("{:<5} {:<20} {:<20} {:<20} {:<10} {:<5}".format(
        row[0], row[1], row[2], row[3], row[4],row[5]))

conn.close()

