from PIL import Image, ImageFilter


image = Image.open('zzy.JPG')
print(image.format, image.size, image.mode)
# This should be the output ('JPEG', (500, 750), 'RGB')
image.show()



image = Image.open('morse.jpg')
rect = 80, 20, 310, 360
image.crop(rect).show()



image = Image.open('morse.jpg')
size = 128, 128
image.thumbnail(size)
image.show()



image1 = Image.open('zzy.JPG')
image2 = Image.open('morse.jpg')
rect = 80, 20, 310, 360
morse = image2.crop(rect)
width, height = morse.size
image1.paste(morse.resize((int(width / 1.5), int(height / 1.5))), (128, 140))
image1.show() # you need this to show the image!



image = Image.open('zzy.JPG')
image.rotate(90).show()

image.transpose(Image.FLIP_LEFT_RIGHT).show()



image = Image.open('zzy.JPG')
for x in range(200, 400):
    for y in range(80, 450):
        image.putpixel((x, y), (128, 128, 128))

image.show()



image = Image.open('morse.jpg')
image.filter(ImageFilter.CONTOUR).show()

print('Done') # This is good, as it allow you to know that your script actually finished.