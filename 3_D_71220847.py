x = int(input("Masukkan Angka : "))

for a in range(x):
    print(' '*(x-a-1) + '* '*(a+1))
for b in range(x):
    print(' '*(b+1) + '* '*(x-b-1))