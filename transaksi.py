import json
from datetime import datetime
from database import load_data, save_data

TRANSAKSI_FILE = "transaksi.json"


def load_transaksi():
    try:
        with open(TRANSAKSI_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_transaksi(data):
    with open(TRANSAKSI_FILE, "w") as file:
        json.dump(data, file, indent=4)


def beli_produk():
    data = load_data()

    # Tampilkan produk
    print("\n=== DAFTAR PRODUK ===")
    for i, item in enumerate(data, start=1):
        print(f"{i}. {item['nama']} - Rp{item['harga']} (stok: {item['stok']})")

    # Pilih produk
    pilihan = int(input("\nPilih nomor produk yang ingin dibeli: ")) - 1

    if pilihan < 0 or pilihan >= len(data):
        print("Nomor produk tidak valid!")
        return

    produk = data[pilihan]

    # Input jumlah
    jumlah = int(input("Jumlah yang dibeli: "))

    if jumlah > produk["stok"]:
        print("Stok tidak mencukupi!")
        return

    total = produk["harga"] * jumlah

    # Kurangi stok
    produk["stok"] -= jumlah
    save_data(data)

    # Buat struk transaksi
    transaksi = load_transaksi()
    transaksi.append({
        "nama_produk": produk["nama"],
        "jumlah": jumlah,
        "harga_satuan": produk["harga"],
        "total": total,
        "waktu": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    save_transaksi(transaksi)

    # Tampilkan struk
    print("\n===== STRUK PEMBELIAN =====")
    print(f"Nama Produk  : {produk['nama']}")
    print(f"Jumlah       : {jumlah}")
    print(f"Harga Satuan : Rp{produk['harga']}")
    print(f"Total Harga  : Rp{total}")
    print(f"Waktu        : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=============================\n")

    print("Pembelian berhasil dicatat!\n")
