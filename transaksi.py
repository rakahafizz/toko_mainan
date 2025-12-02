import json
from datetime import datetime
from database import load_data, save_data

TRANSAKSI_FILE = "transaksi.json"

def output_koma(koma):
    hasil = f"Rp {koma:,}".replace(",",".")
    return hasil

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
        print(f"{i}. {item['nama']} - {output_koma(item['harga'])} (stok: {item['stok']})")

    input_pilihan = input("\nPilih nomor produk yang ingin di beli: ")
    
    if not input_pilihan.isdigit():
        print("Silahkan masukan angka dengan benar")
        return
    pilihan = int(input_pilihan) - 1
    
    if pilihan < 0 or pilihan >= len(data):
        print("Nomor produk tidak valid!")
        return
    
    produk = data[pilihan]
    
    input_jumlah = input("Jumlah yang ingin di beli: ")
    if not input_jumlah.isdigit():
        print("Input harus angka!")
        return
    
    jumlah = int(input_jumlah)
    
    if jumlah > produk["stok"]:
        print(f"Stok tidak mencukupi! Sisa stok cuma {produk['stok']}")
        return
    
    total = produk ["harga"] * jumlah
    
    print("-------------------------------")
    print(f"Total yang harus dibayar: {output_koma(total)}")
    print("-------------------------------")
    
    while True:
        try:
            input_bayar = input("Masukkan Uang Pembayaran: ")
            uang_bayar = int("".join(filter(str.isdigit, input_bayar)))
            
            if uang_bayar >= total:
                break
            else:
                kurang = total - uang_bayar
                print(f"Uang tidak cukup kurang {output_koma(kurang)}")
        except ValueError:
            print("Masukan angka dengan benar")
            
    kembalian = uang_bayar -total
    
    produk["stok"] -= jumlah 
    save_data(data)
    
    transaksi = load_transaksi()
    transaksi.append({
        "nama_produk": produk["nama"],
        "jumlah": jumlah,
        "harga_satuan": produk["harga"],
        "total": total,
        "bayar": uang_bayar,     
        "kembalian": kembalian,   
        "waktu": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    save_transaksi(transaksi)

    
    print("\n=============================")
    print("      STRUK PEMBELIAN        ")
    print("=============================")
    print(f"Barang       : {produk['nama']}")
    print(f"Jumlah       : {jumlah}")
    print(f"Harga Satuan : {output_koma(produk['harga'])}")
    print("-----------------------------")
    print(f"TOTAL TAGIHAN: {output_koma(total)}")
    print(f"TUNAI        : {output_koma(uang_bayar)}")
    print(f"KEMBALI      : {output_koma(kembalian)}")
    print("-----------------------------")
    print(f"Waktu: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=============================\n")
    print("Terima kasih, selamat belanja kembali!\n")
    
    

            
            
    
   
   