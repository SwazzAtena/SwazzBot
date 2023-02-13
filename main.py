import pywhatkit as kit
import pyttsx3
from pyfiglet import Figlet
import webbrowser
import qrcode
import os

while True:
    f = Figlet(font='standard')
    print(f.renderText('SwazzAtena#1889'))
    os.system("pip install pyttsx3")
    print("""
1)QR CODE MAKE
2)Tiktok Bot Basma
3)Metini Sese Çevirme
4)Çıkış
      """)

    islemno = input("İstediğiniz Nedir: ")
    if islemno=="1":
        data=input("Qrccode siteyi giriniz: ")
        img = qrcode.make(data)
        qrcode.make("data")
        imgg= input("Kaydedilecek dosya adı : ")
        img.save(imgg+".png")
    if islemno=="2":
        webbrowser.open("freer.in")
    if islemno=="3":
        Metin = input("Konuşturulacak Metni Seçiniz: ")
        engine = pyttsx3.init()
        engine.say(Metin)
        engine.runAndWait()
    if islemno=="4":
        f = Figlet(font='standard')
        print(f.renderText('By Swazz'))
        break
