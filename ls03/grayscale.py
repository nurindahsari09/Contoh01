from PIL import Image
CITRA = Image.open('re0303.jpg')
PIXEL = CITRA.load()
CITRA_GRAYSCALE = Image.open('re0303.jpg').convert('L')
CITRA_GRAYSCALE.save('gray0303.jpg')
