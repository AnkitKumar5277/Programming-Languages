import qrcode as qr
img = qr.make("https://sites.google.com/view/softwarextm/home")
img.save("save.png")
