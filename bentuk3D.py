def balok():
    "Fungsi Menghitung Volume Balok"
    panjang = int(input("Masukkan panjang balok : "))
    lebar = int(input("Masukkan lebar balok : "))
    tinggi = int(input("Masukkan tinggi balok : "))
    volume_balok = panjang*lebar*tinggi
    print("Panjang balok : ",panjang)
    print("Lebar balok : ",lebar)
    print("Tinggi balok : ",tinggi)
    print("Volume balok : ",volume_balok)

def kubus() :
    "Fungsi Menghitung Volume Kubus"
    sisi = int(input("Masukan sisi kubus : "))
    volume_kubus = sisi * sisi * sisi
    print("Sisi kubus = ",sisi)
    print("Volume kubus = ",volume_kubus)

def tabung() :
    "Fungsi Menghitung Volume Tabung"
    phi = 3.14
    jari_jari = int(input("Masukkan Jari-Jari Alas Tabung : "))
    tinggi_tabung = int(input("Masukkan Tinggi Tabung : "))
    volume_tabung = phi * jari_jari * jari_jari * tinggi_tabung
    print("Jari-jari alas tabung = ",jari_jari)
    print("Volume Tabung = ",volume_tabung)