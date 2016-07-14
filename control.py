import os.path
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from model import Database
from company import Company
from project import Project
from Cloud import Cloud
from Text import Text
from free_grids import FreeGrid
import random
import math


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
        tag_cloud_4 = """(3) Generates tag cloud that shows the names of the manager:
        - font size based on the budget of the project (the older, the smaller)
        - font color is based on the company they work for"""

        for i in range(1, 3):
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
                cls.database = Project.get_projects()
                break
            if user_input == "3":
                break
            if user_input == "4":
                break
            else:
                print("Unavailable, please try again.")

    def __init__(self):
        self.text_size = 0
        self.picture = 0
        self.min_x = 0
        self.min_y = 0
        self.free_places = []
        self.img = 0

    def text_instances(self):

        for world in self.database:
            worlds = Text(world.name, world.weight, world.avg_color)
            self.text_list.append(worlds)  # worlds,
            h, w = worlds.get_text_size()
            self.text_size += h * w

        self.min_x = min([i.get_text_size()[0] for i in self.text_list])
        self.min_y = min([i.get_text_size()[1] for i in self.text_list])

        self.picture = Cloud(self.min_x, self.min_y, self.text_size, len(self.text_list))
        self.free_places = self.picture.grid()
        # self.sq_multi = self.picture.get_multi()
        self.img = self.picture.create_cloud()
        print(*self.free_places)

    def place_pictures(self):
        for picture in self.text_list:
            pic = picture.get_text()
            # pic.show()
            xy, yx = picture.get_text_size()
            x = math.ceil(xy / self.min_x) + 1
            v = int(yx / self.min_y) + 1

            for i in range(1000):
                k = random.choice([*range(len(self.free_places))])
                if self.free_places[k][0] + xy < self.picture.get_max_xy()[0]:
                    if self.free_places[k][1] + yx < self.picture.get_max_xy()[1]:
                        self.img.paste(pic, tuple(self.free_places[k]))
                        break
                if self.free_places[k][0] + xy > self.picture.get_max_xy()[0] and self.free_places[k][1] + yx < self.picture.get_max_xy()[1]:
                    picture.get_rotate_xy()
                    if self.free_places[k][0] + yx < self.picture.get_max_xy()[0] and self.free_places[k][1] + xy < self.picture.get_max_xy()[1]:
                        self.img.paste(pic, tuple(self.free_places[k]))
                    else:
                        continue
            used_indexes_y = []
            used_indexes_x = []
            for i in range(v):
                used_indexes_y.append(self.free_places[k+i][1])
                print("y", k, used_indexes_y)
            for j in range(x):
                used_indexes_x.append(self.free_places[k+j][0])
                print("x", k, used_indexes_x)

            for x in used_indexes_x:
                for y in used_indexes_y:
                    try:
                        self.free_places.remove([x, y])
                    except:
                        print("value error")
                        continue




                        # # print("x freeplace: ", self.free_places[0][0], "y freeplace: ", self.free_places[0][1])
                    # try:
                    #     print("x getlist_x_i: ", self.picture.get_list_x(i), "y get_list_j: ", self.picture.get_list_y(j))
                    #     self.free_places.pop(k)
                    #     # free_places.remove([free_places[k + i][0], free_places[k + j][1]])
                    # except:
                    #     print("value error")
                    #     continue

        print(*self.free_places)

    def process_method(self):
        self.input_ceck()
        self.menu()
        self.text_instances()
        self.place_pictures()
        self.img.show()

first = Control()
first.process_method()


