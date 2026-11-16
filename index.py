jenis1 = ""
jenis2 = ""
print("===Program Kasir Swalayan Maju Sejahtera===")
nama = input("Masukkan Nama Customer: ")
tgl = input("Tanggal Pembelian: ")
print("Nama Customer: ", nama)
print("Tanggal Pembelian: ", tgl)
print("")
print("Produk Pakaian")


def pilihan(i):
    switcher = {
        1: '----Kemeja = Rp.130.000----',
        2: '----Kaos Oblong= Rp.50.000----',
        3: '----Sweater = Rp.250.000----',
        4: '----Baju Muslim = Rp.150.000----',
    }
    return switcher.get(i, "Masukkan Pilihan Yang Benar!")


print("1. Kemeja")
print("2. Kaos Oblong")
print("3. Sweater")
print("4. Baju Muslim")
nomor = int(input("Masukkan Pilihan: "))
c = pilihan(nomor)
print(c)
jumlah1 = int(input("Banyak item yang dibeli: "))
if nomor == 1:
    a = jumlah1 * 130000
    print("Sub-Total= Rp. ", a)
    jenis1 = ("Kemeja")
if nomor == 2:
    a = jumlah1 * 50000
    print("Sub-Total= Rp. ", a)
    jenis1 = ("Kaos")
if nomor == 3:
    a = jumlah1 * 250000
    print("Sub-Total= Rp. ", a)
    jenis1 = ("Jaket")
if nomor == 4:
    a = jumlah1 * 150000
    print("Sub-Total= Rp. ", a)
    jenis1 = ("Baju Muslim")


def pilihan(i):
    switcher = {
        1: '----celana Panjang = Rp.100.000----',
        2: '----Celana Chino = Rp.75.000----',
        3: '----Celana Jeans = Rp.350.000----',
        4: '----Celana Kulot = Rp.100.000----',
    }
    return switcher.get(i, "Masukkan Pilihan Yang Sesuai!")


print("Produk Celana")
print("1. Celana Panjang")
print("2. Celana Chino")
print("3. Celana Jeans")
print("4. Celana Kulot")
nomor = int(input("Masukkan Pilihan: "))
c = pilihan(nomor)
print(c)
jumlah2 = int(input("Banyak item yang dibeli: "))
if nomor == 1:
    b = jumlah2 * 100000
    print("Sub-Total= Rp. ", b)
    jenis2 = ("Celana Panjang")
if nomor == 2:
    b = jumlah2 * 75000
    print("Sub-Total= Rp. ", b)
    jenis2 = ("Celana Chino")
if nomor == 3:
    b = jumlah2 * 350000
    print("Sub-Total= Rp. ", b)
    jenis2 = ("Celana Jeans")
if nomor == 4:
    b = jumlah2 * 100000
    print("Sub-Total= Rp. ", b)
    jenis2 = ("Celana Kulot")

print("total Belanja= Rp.", a + b)
uang = int(input("Uang Tunai: Rp."))
akhir = int(uang - (a + b))

print("================================================")
print("============== STRUK PEMBAYARAN ===============")
print("================================================")
print("=== Nama :", nama)
print("=== Tanggal :", tgl)
print("=== Beli :", jumlah1, jenis1)
print("=== ", jumlah2, jenis2)
print("=== Tagihan :Rp.", a + b)
print("=== Bayar :Rp.", uang)
print("=== Kembalian :Rp.", akhir)
print("==================TERIMA KASIH==================")
print("=sudah berbelanja di Swalayan Maju Sejahtera=")
print("================================================")
