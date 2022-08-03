from PIL import Image, ImageFilter

before = Image.open("image.jpeg")
after = before.filter(ImageFilter.BoxBlur(10))
after.save("out.jpeg")