nilai1 = float(input("masukan nilai soal 1:"))
nilai2 = float(input("masukan nilai soal 2:"))
nilai3 = float(input("masukan nilai soal 3:"))
umur =int(input("masukan umur anda:"))
#rata-rata= (nilai*0.5)+(nilai2*0.3)+(nilai3*0.2)/3
ratarata(int(nilai1+nilai2+nilai3)/3)
if ratarata<=25:
    if umur<=80:
        print("selamat anda lulus!")
    else:print("coba lagi tahun depan!")
    if ratarata>=90:
        print("selamat anda lulus")
    else:print("coba lagi tahun depan")