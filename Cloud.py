from PIL import Image
# from PIL import ImageFont
# from PIL import ImageDraw
# from model import Database
# from company import Company
# import random
import math

class Cloud():

    def __init__(self, max_width, max_height, color, image):
        self.max_width = max_width
        self.max_height = max_height
        self.color = color
        self.image = image

    def create_cloud(self):
        # img = Image.new("RGB", (self.max_width, self.max_height), self.color)
        img = Image.open(self.image)
        img = img.resize((self.max_width, self.max_height), Image.ADAPTIVE)
        return img