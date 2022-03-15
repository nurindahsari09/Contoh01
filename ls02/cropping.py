from PIL import Image
def crop(image_path, coords, saved_location):
    image_obj = Image.open("0205.jpeg")
    cropped_image = image_obj.crop(coords)
    cropped_image.save(saved_location)
   

if __name__ == '__main__':
    image = "0205.jpeg"
    crop(image, (0, 0, 800, 800 ), 're0205.jpg')
