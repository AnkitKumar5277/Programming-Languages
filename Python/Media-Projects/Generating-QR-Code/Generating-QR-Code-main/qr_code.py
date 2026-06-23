import qrcode

# Create QRCode instance
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=10,
)

# Add data to QRCode
qr.add_data("https://sites.google.com/view/softwarextm/home")
qr.make(fit=True)

img = qr.make_image(fill_color="green", back_color="white")

img.save("save.png")

print("QR Code generated")
