from PIL import Image, ImageFilter

before = Image.open("image.jpeg")
after = before.filter(ImageFilter.FIND_EDGES)
after.save("out2.jpeg")