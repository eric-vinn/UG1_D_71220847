print("-----Nilai Ke 1-----")
x = int(input("Nilai Harian : "))
y = int(input("Nilai UTS : "))
z = int(input("Nilai UAS : "))

print("-----Nilai Ke 2-----")
a = int(input("Nilai Harian : "))
b = int(input("Nilai UTS : "))
c = int(input("Nilai UAS : "))

print("-----Total Nilai-----")
def nilai():
    harian = ((x + a)/2)*30/100
    UTS = ((y + b)/2)*30/100
    UAS = ((z + c)/2)*40/100
    total = harian + UTS + UAS
    print("Total nilai yang didapat : ", total)
    if total >= 70:
        print("Total Nilai Dalam Huruf : B")
    else:
        print("Total Nilai Dalam Huruf : C")

nilai()