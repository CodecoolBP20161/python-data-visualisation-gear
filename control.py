import os.path
from PIL import ImageFont
from PIL import ImageDraw
from company import Company
from project import Project, Image2, Image3
from Cloud import Cloud
from manager import Manager
from Text import Text
import math
import random

class Control():

    database = []
    text_list = []


    @staticmethod
    def input_ceck():
        if not os.path.isfile("user.txt"):
            print("Creating user.txt...")
            with open("user.txt", "w") as f:
                f.write(input("dbname="))
                f.write("\n" + input("user="))
                f.write("\n" + input("password="))
            print("user.txt created successfully")

    @classmethod
    def menu(cls):

        cls.input_ceck()

        tag_cloud_1 = """(1) Generates tag cloud that shows the company names:
        - font size based on number of projects (the more, the bigger)
        - font color are a mixture of their project colors"""
        tag_cloud_2 = """(2) Generates tag cloud that shows the project names:
        - font size based on the budget of the project (the more, the bigger)
        - font color based on the project colors"""
        tag_cloud_3 = """(3) Generates tag cloud that shows the project names:
        - font size based on the due date of the project (the older, the smaller)
        - font color based on whether the project requires maintenance or not"""
        tag_cloud_4 = """(4) Generates tag cloud that shows the names of the manager:
        - font size based on the budget of the project (the older, the smaller)
        - font color is based on the company they work for"""

        for i in range(1, 5):
            print("(%d) Generate tag cloud. Type 'info %d' for more information." % (i, i))


        user_input = input("").lower()
        while True:
            if user_input == "info 1":
                print(tag_cloud_1)
                user_input = input("").lower()
            if user_input == "info 2":
                print(tag_cloud_2)
                user_input = input("").lower()
            if user_input == "info 3":
                print(tag_cloud_3)
                user_input = input("").lower()
            if user_input == "info 4":
                print(tag_cloud_4)
                user_input = input("").lower()
            if user_input == "1":
                cls.database = Company.get_companies()
                break
            if user_input == "2":
                cls.database = Image2.get_image2()
                break
            if user_input == "3":
                cls.database = Image3.get_image3()
                break
            if user_input == "4":
                cls.database = Manager.get_all()
                break
            else:
                print("Unavailable, please try again.")

    def __init__(self):
        self.text_size = 0
        self.picture = 0
        self.free_places = []
        self.img = 0

    def text_instances(self):

        for world in self.database:
            if int(world.weight) > 1000:
                weight = int(world.weight)//1000
            elif int(world.weight) > 100 and int(world.weight) < 1000:
                weight = int(world.weight)//100
            else:
                weight =int(world.weight)
            worlds = Text(world.name, weight, world.avg_color)
            self.text_list.append(worlds)
            h, w = worlds.get_text_size()
            self.text_size += h * w
        self.picture = Cloud(math.ceil(math.sqrt(self.text_size))*2, math.ceil(math.sqrt(self.text_size)), (0, 0, 0))
        self.img = self.picture.create_cloud()

    def place_pictures(self):

        draw = ImageDraw.Draw(self.img)
        MAX_HEIGHT = self.picture.max_height  # math.ceil(math.sqrt(text_size))
        MAX_WIDTH = self.picture.max_width  # .ceil(math.sqrt(text_size))*2
        min_fontsize = Text.MIN_FONTSIZE
        height = 0
        width = 0
        row_height = []
        random.shuffle(self.text_list)
        for i in self.text_list:
            text_content = i.name
            font = ImageFont.truetype("arial.ttf", min_fontsize + (i.weight * 2))
            text_size = draw.textsize(text_content, font=font)
            # draw.text((x, y),text_content,(r,g,b))
            print(text_size)
            if width + text_size[0] > MAX_WIDTH:
                height += max([i for i in row_height])
                row_height = []
                width = 0
            draw.text((width, height), text_content, i.color, font=font)
            row_height.append(min_fontsize + (i.weight * 2))
            width += text_size[0]



    def process_method(self):
        self.input_ceck()
        self.menu()
        self.text_instances()
        self.place_pictures()
        self.img.show()

first = Control()
first.process_method()


