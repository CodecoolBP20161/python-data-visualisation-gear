from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
# from model import Database
# from company import Company
# from Cloud import Cloud
# import random
# import math

class Text():

    MIN_FONTSIZE = 10
    img = Image.new("RGB", (5, 5), "red")
    draw = ImageDraw.Draw(img)

    def __init__(self, name, weight, color, font="steelfish rg.ttf"):
        self.name = name
        self.weight = int(weight)
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


