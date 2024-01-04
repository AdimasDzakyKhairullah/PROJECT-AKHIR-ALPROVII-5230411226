import sqlite3
conn = sqlite3.connect('HEWAN.db')
cursor = conn.cursor()
cursor.execute(f"UPDATE HEWAN SET nama_hewan = 'Orangutan', jmlh_sekarang='900' WHERE Id_hewan= 1")
conn.commit()
if cursor.rowcount > 0:
    print(f"Data Orangutan berhasil diupdate.")
else:
    print(f"Tidak ada data Orangutan.")

conn.close()
