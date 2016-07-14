from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import random

class Cloud():

    world_tuple = [("one", 40), ("two", 9), ("three", 15), ("four", 40), ("fff", 5)]

    MAX_HEIGHT = 540
    MAX_WIDTH = 960

    def __init__(self, max_height, max_width):
        self.max_height = max_height
        self.max_width = max_width
        self.wolds = 0

    @classmethod
    def grids(cls):
        weight = 0
        grid_x_list = []
        grid_y_list = []


        for i in cls.world_tuple:
            weight += i[1] * len(i[0])
        print(weight)
        ds = (cls.MAX_HEIGHT * cls.MAX_WIDTH) / weight
        dt = ds / (cls.MAX_WIDTH/cls.MAX_HEIGHT)
        print(dt)
        grid_y = cls.MAX_HEIGHT / (weight/2)
        grid_x = cls.MAX_WIDTH / (weight/2)
        # grid_x_list = [*range(0, cls.MAX_WIDTH, grid_x)]
        # grid_y_list = [*range(0, cls.MAX_HEIGHT, grid_y)]
        print(grid_y, grid_x)

Cloud.grids()
