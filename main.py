from auth import login
from menu import show_product, add_product, edit_product, delete_product

from transaksi import beli_produk

def main():
    role = None

    # ini login
    while role is None:
        role = login()


    while True:
        print("=== TOKO MAINAN PYTHON ===")

        if role == "admin":
            print("1. Lihat Produk")
            print("2. Tambah Produk")
            print("3. Edit Produk")
            print("4. Hapus Produk")
            print("5. Beli Produk")
            print("6. Keluar")

            pilihan = input("Pilih menu: ")
            
            if pilihan == "1":
                show_product()
            elif pilihan =="2":
                add_product()
            elif pilihan =="3":
                edit_product()
            elif pilihan =="4":
                delete_product()
            elif pilihan =="5":
                beli_produk()
            elif pilihan =="6":
                print("Terimakasih telah menggunakan program ini")
                break
            else:
                print("pilihan tidak valid!\n")
        #   sampe sini kerjakkan ulang 
        elif role == "user":
            print("1. Lihat Produk")
            print("2. Beli Produk")
            print("3. Keluar")

            pilihan = input("Pilih menu: ")

            if pilihan == "1":
                show_product()
            elif pilihan == "2":
                beli_produk()
            elif pilihan == "3":
                print("Terima kasih telah menggunakan aplikasi!")
                break
            else:
                print("Pilihan tidak valid!\n")
    



if __name__ == "__main__":
    main()