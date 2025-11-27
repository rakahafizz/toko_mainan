from database import load_data, save_data

def format_angka(promt):
    return int("".join(filter(str.isdigit,input(promt))))

def format_rupiah(angka):
    return f"Rp {angka:,}".replace(",",".")

def show_product():
    data = load_data()
    if not data:
        print("\nBelum ada produk!\n")
        return

    print("\n=== DAFTAR PRODUK ===")
    for i, item in enumerate(data, start=1):
        print(f"{i}. {item['nama']} - {format_rupiah(item['harga'])} (stok: {item['stok']})")
    print()

def add_product():
    nama = input("Nama mainan: ")
    harga =format_angka("Harga: ")
    stok = int(input("Stok: "))

    data = load_data()
    data.append({"nama": nama, "harga": harga, "stok": stok})
    save_data(data)

    print("\nProduk berhasil ditambahkan!\n")

def edit_product():
    data = load_data()
    show_product()

    index = int(input("Pilih nomor produk yang mau di-edit: ")) - 1

    if index < 0 or index >= len(data):
        print("Nomor tidak valid!")
        return

    print("\nKosongkan jika tidak ingin mengubah.")
    nama = input(f"Nama baru ({data[index]['nama']}): ") or data[index]["nama"]
    harga = input(f"Harga baru ({data[index]['harga']}): ")
    stok = input(f"Stok baru ({data[index]['stok']}): ")

    data[index]["nama"] = nama
    if harga:
        data[index]["harga"] = int(harga)
    if stok:
        data[index]["stok"] = int(stok)

    save_data(data)
    print("\nProduk berhasil diperbarui!\n")

def delete_product():
    data = load_data()
    show_product()

    index = int(input("Pilih nomor produk yang mau dihapus: ")) - 1
    if index < 0 or index >= len(data):
        print("Nomor tidak valid!")
        return

    deleted = data.pop(index)
    save_data(data)
    print(f"\nProduk '{deleted['nama']}' berhasil dihapus!\n")
