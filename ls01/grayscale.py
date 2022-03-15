from PIL import Image
CITRA = Image.open('re05.jpg')
PIXEL = CITRA.load()
CITRA_GRAYSCALE = Image.open('re05.jpg').convert('L')
CITRA_GRAYSCALE.save('gray05.jpg')
