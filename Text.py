from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from model import Database
from company import Company
import random
import math

class Text():


    MIN_FONTSIZE = 10
    img = Image.new("RGB", (5, 5), "red")
    draw = ImageDraw.Draw(img)

    def __init__(self, name, weight, color=(), font="steelfish rg.ttf"):  #  ,font)
        self.name = name
        self.weight = weight
        self.font_size = self.weight * self.MIN_FONTSIZE
        self.color = color
        self.font = ImageFont.truetype(font, self.font_size)
        self.text_size = []
        self.img2 = 0
        self.rotate = False

        self.text_size = self.draw.textsize(self.name, font=self.font)
        self.img2 = Image.new("RGB", (self.text_size[0], self.text_size[1]), self.color)
        draw2 = ImageDraw.Draw(self.img2)
        draw2.text((0, 0), self.name, fill=(255, 255, 255), font=self.font)
        # self.text_size
        # img2.save(self.name)
        # self.img2.show()


    def get_text_size(self):
        if self.text_size:
            # if not self.rotate:
            return self.text_size[0], self.text_size[1]
            # if self.rotate:
            #     return 11 * self.weight, self.text_size[0]
        else:
            raise Exception('No text_size parameters')

    def get_rotate_xy(self):
        self.img2 = self.img2.rotate(90, resample=Image.BICUBIC, expand=True)
        self.rotate = True
        self.get_text_size()

    def get_text(self):
        return self.img2


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
        self.max_width = self.grid_x * (self.multi+1)
        self.max_height = self.grid_y * (self.multi+1)
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


class Controll():
    pass


# static or instence attribute???
text_list = []
text_size = 0
weight = 0

# @staticmethod
for world in Company.get_companies():
    worlds = Text(world.company_name, world.weight, world.avg_color)
    text_list.append(worlds)  # worlds,
    h, w = worlds.get_text_size()
    text_size += h * w
    weight += worlds.weight**2+(2*worlds.weight)
print("textsize", text_size)



# print(text_list)

min_x = min([i.get_text_size()[0] for i in text_list])
min_y = min([i.get_text_size()[1] for i in text_list])
print(min_x, min_y)

first = Cloud(min_x, min_y, weight, len(text_list))
free_places = first.grid()
sq_multi = first.get_multi()

# print(*free_places)
img = first.create_cloud()
# img.show()
# text_list.sort()
for picture in text_list:
    pic = picture.get_text()
    pic.show()

    xy, yx = picture.get_text_size()
    x = math.ceil(xy/min_x)+1
    v = int(yx/min_y)+1

    for i in range(len(free_places)):
        k = random.randint(0, len(free_places)-1)
        if free_places[k][0] + xy < first.get_max_xy()[0]:
            if free_places[k][1] + yx < first.get_max_xy()[1]:
                img.paste(pic, tuple(free_places[k]))
                break
        if free_places[i][0] + xy > first.get_max_xy()[0] and free_places[k][1] + yx < first.get_max_xy()[1]:
            picture.get_rotate()
            if free_places[i][0] + yx < first.get_max_xy()[0] and free_places[k][1] + xy < first.get_max_xy()[1]:
                img.paste(pic, tuple(free_places[k]))
            else:
                continue

    # if free_places[i][0] + xy > first.get_max_xy()[0]:
    #     img.paste(pic, tuple(free_places[i]))
    # print("x ", x, "y ", v)

    for i in range(x):
        for j in range(v):
            print("x freeplace: ", free_places[0][0], "y freeplace: ", free_places[0][1])
            try:
                print("x getlist_x_i: ", first.get_list_x(i), "y get_list_j: ", first.get_list_y(j))
                free_places.remove([free_places[k+i][0], free_places[k+j][1]])

            except:
                print("value error")
                continue


print(*free_places)


# check the picture edge before place it
# rotation how to use and when
# invert complementer color
# how to controll the flow in a class
# chose random from the object list or from the picture

# print(*free_places)
# print(*pop_item)
img.show()




