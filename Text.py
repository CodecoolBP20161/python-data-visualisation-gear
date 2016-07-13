from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from model import Database
import random
import math

class Text():


    MIN_FONTSIZE = 10
    img = Image.new("RGB", (5, 5), "red")
    draw = ImageDraw.Draw(img)

    def __init__(self, name, weight, color=(), font="arial.ttf"):  #  ,font)
        self.name = name
        self.weight = weight
        self.font_size = self.weight * self.MIN_FONTSIZE
        self.color = color
        self.font = ImageFont.truetype(font, self.font_size)
        self.text_size = []
        self.img2 = 0

        self.text_size = self.draw.textsize(self.name, font=self.font)
        self.img2 = Image.new("RGB", (self.text_size[0], 11*self.weight), self.color)
        draw2 = ImageDraw.Draw(self.img2)
        draw2.text((0, 0), self.name, fill=(255, 255, 255), font=self.font)
        # self.text_size
        # img2.save(self.name)
        # img2.show()


    def get_text_size(self):
        if self.text_size:
            return self.text_size[0], 11*self.weight
        else:
            raise Exception('No text_size parameters')

    def get_text(self):
        # self.img2 = self.img2.rotate(90, resample=Image.BICUBIC, expand=True)
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
        self.multi = math.ceil(math.sqrt(self.max_weight + self.text_number))
        self.max_width = self.grid_x * (self.multi+1)
        self.max_height = self.grid_y * (self.multi+1)
        self.list_x = [*range(0, self.max_width, self.grid_x)]
        self.list_y = [*range(0, self.max_height, self.grid_y)]
        for x in self.list_x:
            for y in self.list_y:
                grid_cross.append([x, y])
        return grid_cross


        print(len(list_x), len(list_y), "list_length")
        print(self.max_height, self.max_width, "max")
        print(multi)

    def create_cloud(self):
        img = Image.new("RGB", (self.max_width, self.max_height), "blue")
        return img

    def get_multi(self):
        return self.multi

    def get_list_x(self, i=None):
        if i:
            return self.list_x[i]
        else:
            return self.list_x


    def get_list_y(self, i=None):
        if i:
            return self.list_y[i]
        else:
            return self.list_x




class Controll():
    pass


# static or instence attribute???
text_list = []
weight = 0

# @staticmethod
for world in Database.get_client_and_number_of_projects():
    worlds = Text(world[0], world[1], (120, 120, 120))
    text_list.append(worlds)  # worlds,
    weight += worlds.weight**2

# print(text_list)

min_x = min([i.get_text_size()[0] for i in text_list])
min_y = min([i.get_text_size()[1] for i in text_list])
print(weight)

print(len(text_list))

first = Cloud(min_x, min_y, weight, len(text_list))
free_places = first.grid()
sq_multi = first.get_multi()

print(*free_places)
img = first.create_cloud()
# img.show()
pic = text_list[0].get_text()
pic.show()

x, v = text_list[0].get_text_size()
x = math.ceil(x/min_x)
v = int(v/min_y)

if x > len(first.get_list_x()):
    pass
if v > len(first.get_list_y()):
    pass
img.paste(pic, tuple(free_places[0]))


# delete used grid from the list
pop_item = []
# for i in range(text_list[0].weight):
#     for j in range(text_list[0].weight):
#         pop_item.append([first.get_list_x(i),first.get_list_y(j)])
#
# for item in pop_item:
#     pass

# OR it is mucth better


for i in range(x):
    for j in range(v):
        pop_item.append([first.get_list_x(i), first.get_list_y(j)])

for item in pop_item:
    try:
        idx = free_places.index(item)
        free_places.pop(idx)
    except ValueError:
        print("no index")  # break

print(pop_item)
print(*free_places)


# check the picture edge before place it
# rotation how to use and when
# invert complementer color
# how to controll the flow in a class
# chose random from the object list or from the picture

# print(*free_places)
# print(*pop_item)
img.show()







# MAX_HEIGHT = 740
# MAX_WIDTH = 760
# img = Image.new("RGB", (MAX_WIDTH, MAX_HEIGHT), "red")
#
# draw = ImageDraw.Draw(img)
#
# # font = ImageFont.truetype(<font-file>, <font-size>)
#
#
# min_fontsize = 10
#
# print(world_tuple)
#     # [("one", 1), ("two", 2), ("three", 5), ("four", 10), ("fff", 9),
#     #            ("one", 1), ("two", 2), ("three", 5), ("four", 10), ("fff", 9),
#     #            ("one", 1), ("two", 2), ("three", 5), ("four", 10), ("fff", 9)
#     #            ]
#
# height = 0
# print(height)
# width = 0
# row_height = []
# for i in world_tuple:
#     text_content = i[0]
#     font = ImageFont.truetype("arial.ttf", min_fontsize*i[1])
#     text_size = draw.textsize(text_content, font=font)
#     # draw.text((x, y),text_content,(r,g,b))
#     print(text_size)
#     if width + text_size[0] > MAX_WIDTH:
#         height += max([i for i in row_height])
#         row_height = []
#         width = 0
#     # draw.rectangle(((0, height), (text_size[0], text_size[1])), fill=(55, 125, 100))
#     draw.text((width, height), text_content, fill=(255, 255, 255), font=font)
#     row_height.append(min_fontsize*i[1])
#     width += text_size[0]
#     # draw.text((0, text_size[1]), text_content, **text_options)
# # draw.text((text_size[0], 0), text_content, **text_options)
# # draw.text(text_size, text_content, **text_options)
# # img2 = img.crop((0, 0, 0, height))
# # .crop((0, 30, w, h-30))
#
# img.show()
# img.save('sample-out.png')

