from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
# from PIL import ImageEnhance

img = Image.new("RGB", (512, 512), "red")
draw = ImageDraw.Draw(img)
image_list = []

text_options = {
    'fill': (255, 255, 255)
}
size_list = [10, 20, 50, 70, 90]
weight = 0
height = 0
coordinates = []

for i in size_list:

    image_list.append(Image.new("RGB", (200, 200), "blue"))

for i in range(len(image_list)):

    draw = ImageDraw.Draw(image_list[i])
    text_content = "Text"
    font = ImageFont.truetype("arial.ttf", size_list[i])
    w, h = draw.textsize(text_content, font=font)
    image_list[i] = image_list[i].resize((w, h), Image.ADAPTIVE)

    print(w, h)
    draw.text((0, 0), text_content, **text_options, font=ImageFont.truetype("arial.ttf", int(size_list[i])))
    image_list[i].show()
    image_list[i].rotate(0)
    img.paste(image_list[i], (weight, height))

    coordinates.append([w, h])
    weight += w
    height += h
print(coordinates)
img.show()




