from PIL import Image

def crop(image_path, coords, saved_location):
    image_obj = Image.open("03055.jpeg")
    cropped_image = image_obj.crop(coords)
    cropped_image.save(saved_location)
   

if __name__ == '__main__':
    image = "03055.jpeg"
    crop(image, (0, 0, 800, 800 ), 're03055.jpg')
