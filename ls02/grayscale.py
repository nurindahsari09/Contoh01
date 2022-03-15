from PIL import Image
CITRA = Image.open('re0205.jpg')
PIXEL = CITRA.load()
CITRA_GRAYSCALE = Image.open('re0205.jpg').convert('L')
CITRA_GRAYSCALE.save('gray0205.jpg')
