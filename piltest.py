from PIL import Image
im = Image.open("hopper.bmp")

print(im.format, im.size, im.mode)

#im.show()

newimg = Image.new('RGB', (220, 440), color=(45, 203, 45))

newimg.show()