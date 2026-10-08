suhu = float(input("Masukkan suhu reaktor (Celcius): "))
tekanan = float(input("Masukkan tekanan gas (Bar): "))

print("Suhu    :", suhu, "Celcius")
print("Tekanan :", tekanan, "Bar")

if suhu > 1000:
    if tekanan > 50:
        status = "MELTDOWN! SEGERA EVAKUASI!"
    else:
        status = "Bahaya Suhu: Segera Turunkan Daya!"
elif suhu > 500:
    if tekanan > 30:
        status = "Peringatan: Tekanan Tidak Stabil"
    else:
        status = "Operasi Reaktor Normal"
else:
    status = "Reaktor Belum Cukup Panas"

print("Status bahaya:", status)

pompa = "Pompa Maksimal" if suhu > 800 else "Pompa Normal"
print("Status pompa :", pompa)