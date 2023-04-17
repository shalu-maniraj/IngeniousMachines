import qrcode

sr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_L,
                   box_size=20,
                   border=0)

sr.add_data("https://www.bing.com/")
sr.make(fit=True)

img = sr.make_image(fill_color="blue", back_color="yellow")
img.save("myimage.png")
