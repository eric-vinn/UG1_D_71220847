print("===== KASIR =====")

x = int(input("Harga Barang : "))
y = input("Apakah anda membeli barang lagi? [yes/no] : ")

while y == ("yes"):
    int(input("Harga Barang : "))
    input("Apakah anda membeli barang lagi? [yes/no] : ")

if y == ("no"):
    print("invalid")