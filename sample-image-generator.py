from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from model import Database
from PIL import ImageEnhance
from company import Company
import math

class Text():

    MIN_FONTSIZE = 10
    img = Image.new("RGB", (5, 5), "red")
    draw = ImageDraw.Draw(img)

    def __init__(self, name, weight, color, font="steelfish rg.ttf"):
        self.name = name
        self.weight = weight
        self.color = color
        self.font_size = self.weight + self.MIN_FONTSIZE
        self.font = ImageFont.truetype(font, self.font_size)
        self.text_size = self.draw.textsize(self.name, font=self.font)

    def get_text_size(self):
        if self.text_size:
            # if not self.rotate:
            return self.text_size[0], self.text_size[1]
            # if self.rotate:
            #     return 11 * self.weight, self.text_size[0]
        else:
            raise Exception('No text_size parameters')

class Cloud():

    def __init__(self, max_width, max_height, color):
        self.max_width = max_width * 2
        self.max_height = max_height
        self.color = color

    def create_cloud(self):
        img = Image.new("RGB", (self.max_width, self.max_height), self.color)
        return img

world_tuple = Company.get_companies()
text_size = 0
picture = 0
text_list = []

for world in world_tuple:
    worlds = Text(world.name, world.weight, world.avg_color)
    text_list.append(worlds)  # worlds,
    w, h = worlds.get_text_size()
    text_size += w*h

cloud = Cloud(math.ceil(math.sqrt(text_size))*2, math.ceil(math.sqrt(text_size)), (120, 120, 120))
# img = Image.new("RGB", (math.ceil(math.sqrt(text_size))*2, math.ceil(math.sqrt(text_size))), (120, 120, 120))
img = cloud.create_cloud()
draw = ImageDraw.Draw(img)
MAX_HEIGHT = cloud.max_height  # math.ceil(math.sqrt(text_size))
MAX_WIDTH = cloud.max_width  # .ceil(math.sqrt(text_size))*2
min_fontsize = Text.MIN_FONTSIZE

height = 0
print(height)
width = 0
row_height = []
for i in text_list:
    text_content = i.name
    font = ImageFont.truetype("arial.ttf", min_fontsize+(i.weight*2))
    text_size = draw.textsize(text_content, font=font)
    # draw.text((x, y),text_content,(r,g,b))
    print(text_size)
    if width + text_size[0] > MAX_WIDTH:
        height += max([i for i in row_height])
        row_height = []
        width = 0

    draw.text((width, height), text_content, i.color, font=font)
    row_height.append(min_fontsize+(i.weight*2))
    width += text_size[0]


img.show()
img.save('sample-out.png')
