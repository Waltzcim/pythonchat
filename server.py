import socket
import time

host_ismi = "localhost"
port = 7777

internet_soketi = socket.socket()
internet_soketi.bind((host_ismi,port))

internet_soketi.listen(1)

baglanti, adres = internet_soketi.accept()

print(str(adres)+" baglanti sağlandı")

while True:
    while True:
        try:
            gelen_veri = str(baglanti.recv(1024).decode())
            print("client şunu yolladı :"+gelen_veri)
            break
        except ConnectionResetError:
            time.sleep(2)
            baglanti, adres = internet_soketi.accept()
            print(str(adres)+"baglantı Başarılı ")
    if gelen_veri == "cikis":
        break
    else:
        mesaj = input ("----::")
        print("client bekleniyor ")
        baglanti.send(mesaj.encode())

baglanti.close()
