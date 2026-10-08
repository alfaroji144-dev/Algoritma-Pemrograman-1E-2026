total = int(input("Masukkan total belanja (Rp): "))

if total % 100000 == 0:
    total_bayar = 0
elif total % 50000 == 0:
    total_bayar = total - (total * 50 / 100)
elif total % 10000 == 0:
    total_bayar = total - (total * 20 / 100)
elif total >= 200000:
    total_bayar = total - (total * 10 / 100)
else:
    total_bayar = total

status_poin = "Poin Bertambah" if total_bayar > 0 else "Tidak Ada Poin"

print("Total belanja awal :", total)
print("Total harus dibayar:", total_bayar)
print("Status poin        :", status_poin)