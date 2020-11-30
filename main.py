from PIL import Image, ImageDraw


class Dataset:
    def __init__(self):

        self.__data = list()
        self.__P = []

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, coord):
        self.__data.append(tuple(coord))

    def __jarvismarch(self):
        n = len(self.__data)
        p = range(n)
        for i in range(1, n):
            if self.__data[p[i]][0] < self.__data[p[0]][0]:
                p[i], p[0] = p[0], p[i]
        self.__P = list(p)

    @staticmethod
    def __rotate(A, B, C):
        return (B[0] - A[0]) * (C[1] - B[1]) - (B[1] - A[1]) * (C[0] - B[0])

    def jarvis(self):
        self.__jarvismarch()
        h = [self.__P[0]]
        del self.__P[0]
        self.__P.append(h[0])
        while True:
            right = 0
            for i in range(1, len(self.__P)):
                if self.__rotate(self.__data[h[-1]], self.__data[self.__P[right]], self.__data[self.__P[i]]) < 0:
                    right = i
            if self.__P[right] == h[0]:
                break
            else:
                h.append(self.__P[right])
                del self.__P[right]
        point_of_convex_hull = []
        for i in h:
            point_of_convex_hull.append(self.__data[i])
        return point_of_convex_hull


if __name__ == '__main__':
    data = Dataset()

    with open("DS2.txt") as dataset:
        for line in dataset:
            data.data = int(line.split(" ")[0]), int(line.split(" ")[1])

    image = Image.new("RGB", (540, 960), (255, 255, 255))
    draw = ImageDraw.Draw(image)
    points = data.jarvis()
    j = 0
    while j < len(points) - 1:
        draw.line((points[j][0], points[j][1], points[j + 1][0], points[j + 1][1]),(0,0,255))
        j += 1
    for coord in data.data:
        draw.point(coord, (0, 0, 0))
    image.show()
    image.save("result_convex_hull.jpg", "JPEG")
