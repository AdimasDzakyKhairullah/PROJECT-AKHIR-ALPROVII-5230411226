import sqlite3
conn = sqlite3.connect('HEWAN.db')
cursor = conn.cursor()
cursor.execute(
    f"UPDATE HEWAN SET nama_hewan = 'Komodo', Asal = 'Nusa Tenggara Timur' WHERE Id_hewan= 3")
conn.commit()
if cursor.rowcount > 0:
    print(f"Data Komodo berhasil diupdate.")
else:
    print(f"Tidak ada data Komodo.")

conn.close()
