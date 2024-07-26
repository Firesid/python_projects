import qrcode
import image
qr = qrcode.QRCode(
    version = 15, #15 is the version of the qr code, higher the number bigger the code image and complicated picture
    box_size = 10, #size of the box where qr code will be displayed
    border = 5 # it is the white part of the image -- border in all 4 sides with white color
)
data ="https://www.google.com" #qr code website

qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill = "black", back_color = "white")
img.save("test.png")