from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import random
# from PIL import ImageEnhance
max_height = 200
max_weight = 200
base_rgb = (0, 0, 0)
img = Image.new("RGB", (max_height, max_weight), base_rgb)
pix = img.load()
draw = ImageDraw.Draw(img)
image_list = []

grid_x = [*range(0, max_weight, 20)]
grid_y = [*range(0, max_height, 10)]
print(grid_x, grid_y)

text_options = {
    'fill': (255, 255, 255)
}
size_list = [10, 20, 40]
size_list.sort(reverse=True)
print(size_list)
weight = 0
height = 0
coordinates = []
text_content = "Text"

for i in size_list:
    draw = ImageDraw.Draw(img)

    font = ImageFont.truetype("arial.ttf", i)
    w, h = draw.textsize(text_content, font=font)
    print(w, h)
    image_list.append(Image.new("RGB", (w, h), "blue"))

for i in range(len(image_list)):

    draw = ImageDraw.Draw(image_list[i])
    font = ImageFont.truetype("arial.ttf", size_list[i])
    w, h = draw.textsize(text_content, font=font)
    # image_list[i] = image_list[i].resize((w, h), Image.ADAPTIVE)

    # print(w, h)
    random_h = random.randint(0, max_height - w)
    random_w = random.randint(0, max_weight - h)

    draw.text((0, 0), text_content, **text_options, font=font)
    image_list[i].show()
    image_list[i].rotate(50)
    if pix[random_h, random_w] == (0, 0, 0) and pix[random_h + w, random_w] == (0, 0, 0):
        img.paste(image_list[i], (random_h, random_w))
    pix = img.load()

    coordinates.append([w, h])
    weight += w
    height += h
# print(coordinates)
img.show()




