import qrcode
data=input("Siteyi Giriniz")
img = qrcode.make(data)
img.save('My.png')