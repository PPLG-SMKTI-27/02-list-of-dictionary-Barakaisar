# List of dictionary
items = [
    {"barang": "Pensil", "stok": 100, "harga": 2000},
    {"barang": "Buku Tulis", "stok": 50, "harga": 15000},
    {"barang": "Penghapus", "stok": 75, "harga": 5000},
    {"barang": "Rautan", "stok": 30, "harga": 3000},
    {"barang": "Spidol", "stok": 20, "harga": 10000}
]

# Fungsi untuk menambahkan item ke list of dictionary
def create(barang, stok, harga):
    new_item = {"barang": barang, "stok": stok, "harga": harga}
    items.append(new_item)

# Menampilkan isi dari list of dictionary
for item in items:
    print(f"Nama: {item['barang']}, Stok: {item['stok']}, Harga: {item['harga']}")
# Contoh menambahkan item baru
create("Kertas", 200, 5000)

# Menampilkan isi setelah penambahan
print("\nSetelah penambahan item:")
for item in items:
  print(f"Nama: {item['barang']}, Stok: {item['stok']}, Harga: {item['harga']}")