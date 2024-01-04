import sqlite3

conn = sqlite3.connect('HEWAN.db')
cursor = conn.cursor()

Jenis = 'Mamalia'
cursor.execute(f"DELETE FROM HEWAN WHERE Jenis = ?", (Jenis,))
conn.commit()

if cursor.rowcount > 0:
    print(f"Data HEWAN dengan Jenis_hewan {Jenis} berhasil dihapus.")
else:
    print(f"Tidak ada data hewan dengan Jenis_hewan {Jenis}.")

# Menutup koneksi
conn.close()
