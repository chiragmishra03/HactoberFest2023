#To create a QR code from text in Python, you can use a library called qrcode. First, you need to install this library if you haven't already. You can install it using pip:
pip install qrcode
pip install Pillow


import qrcode

# Text you want to convert to a QR code
text = "Hello, this is a QR code!"

# Generate a QR code
qr = qrcode.QRCode(
    version=1,  
    error_correction=qrcode.constants.ERROR_CORRECT_L, 
    box_size=10,  
    border=4, 
)
qr.add_data(text)
qr.make(fit=True)


img = qr.make_image(fill_color="black", back_color="white")


img.save("qr_code.png")

img.show()
