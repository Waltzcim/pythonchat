import socket
import time

host_ismi = "localhost"
port = 7777

internet_soketi = socket.socket()
internet_soketi.connect((host_ismi,port))

print("bağlantı sağlandı{}:{}".format(host_ismi , port))

mesaj = input("----:")
print("server bekleniyor hacı")

while mesaj != "cikis":
    internet_soketi.send(mesaj.encode())
    gelen_veri = internet_soketi.recv(1024).decode()

    print("SUNUCU:"+gelen_veri)

    mesaj = input("----")
    print("sunucu bekleniyor...")

internet_soketi.close()