print ("==== selamat datang di toko andi tersenyum, selamat belanja!====")
total=int(input("total belanja:Rp" ))
diskona=int(total-(total*0.02))
diskonb=int(total-(total*0.05))
diskonc=int(total-(total*10/100))
if total< 100000:
    print("tidak ada diskon! maka yang anda bayarkan adalah:",total)
elif total<=100000:
    print("biaya yang harus anda bayarkan setelah diskon adalah:Rp",diskona)
elif total>=500000:
    print("biaya yang harus anda bayarkan setelah diskon adalah:Rp",diskonb)
elif total >999999:
    print("biaya yang harus anda bayarkan setelah diskon adalah:Rp",diskonc)