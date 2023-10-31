Soal = int(input('''Silahkan pilih diantara soal berikut?
             1. Menghitung luas persegi
             2. Menghitung luas lingkaran
             3. Menghitung luas persegi
             ...'''))
match Soal:
    case 1:
        print("Kamu memilih luas persegi")
        sisi = int(input("sisi ="))
        print("untuk luas persegi dengan sisi", sisi, "adalah", sisi*sisi)
    case 2:
        print("Kamu memilih luas lingkaran")
        r = int(input("jari jari ="))
        luaslingkaran = 3.14 * r*r
        print("untuk luas lingkaran dengan jari jari", r, "adalah", luaslingkaran)
    case 3:
        print("Kamu memilih luas segitiga")
        alas = int(input("alas ="))
        tinggi = int(input("tinggi ="))
        luas = 0.5*alas*tinggi
        print("untuk luas segitiga","dengan alas",alas, "dengan tinggi", tinggi, "adalah")
    case _:
        print("pilihanmu salah! silahkan coba lagi")
        