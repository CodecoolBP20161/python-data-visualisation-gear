from PIL import Image
# from PIL import ImageFont
# from PIL import ImageDraw
# from model import Database
# from company import Company
# import random
import math

class Cloud():

    def __init__(self, grid_x, grid_y, max_weight, text_number):
        self.grid_x = grid_x
        self.grid_y = grid_y
        self.max_weight = max_weight
        self.text_number = text_number
        self.max_width = 0
        self.max_height = 0
        self.multi = 0
        self.list_x = 0
        self.list_y = 0

    def grid(self):
        grid_cross = []
        self.multi = math.ceil(math.sqrt(self.max_weight + (self.text_number)))
        self.max_width = math.ceil(math.sqrt(self.max_weight))
        self.max_height = math.ceil(math.sqrt(self.max_weight))
        self.list_x = [*range(0, self.max_width, self.grid_x)]
        self.list_y = [*range(0, self.max_height, self.grid_y)]
        for x in self.list_x:
            for y in self.list_y:
                grid_cross.append([x, y])
        return grid_cross

    def create_cloud(self):
        img = Image.new("RGB", (self.max_width, self.max_height), "blue")
        print(len(self.list_x), len(self.list_y), "list_length")
        print(self.max_height, self.max_width, "max")
        print(self.multi)
        return img

    def get_multi(self):
        return self.multi

    def get_list_x(self, i=-1):
        if i != -1:
            return self.list_x[i]
        else:
            return self.list_x

    def get_list_y(self, i=-1):
        if i != -1:
            return self.list_y[i]
        else:
            return self.list_x

    def get_max_xy(self):
        return self.max_width, self.max_height
