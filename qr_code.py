import qrcode

FILL_COLOR = "black"
BACK_COLOR = "white"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_M,
    box_size=10,
    border=4,
)
data = "00020101021238560010A0000007270138000697042201120402040206940208QRIBFTTA5303704540410005802VN5913DAU VAN GIANG62080804TEST63047949"
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color=FILL_COLOR, back_color=BACK_COLOR)
img.show()