from PIL import Image, ImageDraw


class Dataset:
    def __init__(self):
        self.__data = list()

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, coord):
        self.__data.append(tuple(coord))


data = Dataset()

with open("DS2.txt") as dataset:
    for line in dataset:
        data.data = int(line.split(" ")[0]), int(line.split(" ")[1])

image = Image.new("RGB", (540, 960), (255, 255, 255))
draw = ImageDraw.Draw(image)

for coord in data.data:
    draw.point(coord, (0, 0, 0))
image.show()
image.save("result.jpg", "JPEG")