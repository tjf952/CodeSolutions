
import time
import concurrent.futures
from PIL import Image, ImageFilter

img_names = [
    "photo10.png",
    "photo11.png",
    "photo12.png",
    "photo13.png",
    "photo14.png",
    "photo15.png",
    "photo1.png",
    "photo2.png",
    "photo3.png",
    "photo4.png",
    "photo5.png",
    "photo6.png",
    "photo7.png",
    "photo8.png",
    "photo9.png",
]

t1 = time.perf_counter()

size = (1200, 1200)


def process_image(img_name):
    img = Image.open(f"images/{img_name}")
    img = img.filter(ImageFilter.GaussianBlur(15))
    img.thumbnail(size)
    img.save(f'processed/{img_name}')
    print(f'{img_name} was processed...')


with concurrent.futures.ProcessPoolExecutor() as executor:
    executor.map(process_image, img_names)


t2 = time.perf_counter()

print(f'Finished in {t2-t1} seconds')
