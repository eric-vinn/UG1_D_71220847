print("===== KASIR =====")

while True:
    x = int(input("Harga Barang : "))
    y = input("Apakah anda membeli barang lagi? [yes/no] : ")
    x += x
    if y == "no":
        print("TOTAL BELANJA : ", x)
        break
    elif y == "yes":
        continue
    else:
        print("INVALID")
        break