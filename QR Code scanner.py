import qrcode

data = "Dont forget to subscribe"

img = qrcode.make(data)

qr = qrcode.QRCode(version = 1, box_size=10, border = 5)

qr.make(fit=True)
img = qr.make_image(full_colour = "black" , back_colour = "White")


img.save("C:/Users/thega/Documents/Coding projects/Html & CSS/QR Codeqrcode.png")

