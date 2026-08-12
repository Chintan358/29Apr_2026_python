import qrcode

# Data you want to encode
data = "https://fb.com"

# Create and save the image
img = qrcode.make(data)
img.save("my_qr_code.png")