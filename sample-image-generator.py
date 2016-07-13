from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from model import Database
from PIL import ImageEnhance

class Text():

    MIN_FONTSIZE = 10
    img = Image.new("RGB", (5, 5), "red")
    draw = ImageDraw.Draw(img)

    def __init__(self, name, weight, color=(), font="arial.ttf"):  #  ,font)
        self.name = name
        self.weight = weight
        self.font_size = self.weight * self.MIN_FONTSIZE
        self.color = color
        self.font = ImageFont.truetype(font, self.weight)
        self.text_size = []

        self.text_size = self.draw.textsize(self.name, font=self.font)
        img2 = Image.new("RGB", (self.text_size[0], self.text_size[1]), self.color)
        draw2 = ImageDraw.Draw(img2)
        draw2.text((0, 0), self.name, fill=(255, 255, 255), font=self.font)
        # img2.save(self.name)
        img2.show()


    def get_text_size(self):
        if self.text_size:
            return self.text_size
        else:
            raise Exception('No text_size parameters')

world_tuple = Database.get_client_and_number_of_projects()
text_list = []
for world in world_tuple:
    worlds = Text(world[0], world[1], (120, 120, 120))
    text_list.append((worlds.get_text_size(), worlds.name))
print(text_list)






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

