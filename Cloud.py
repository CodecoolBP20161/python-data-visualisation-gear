from PIL import Image
# from PIL import ImageFont
# from PIL import ImageDraw
# from model import Database
# from company import Company
# import random
import math

class Cloud():

    def __init__(self, max_width, max_height, color):
        self.max_width = max_width * 2
        self.max_height = max_height
        self.color = color

    def create_cloud(self):
        # img = Image.new("RGB", (self.max_width, self.max_height), self.color)
        img = Image.open("image.jpg")
        img = img.resize((self.max_width, self.max_height), Image.ADAPTIVE)
        return img