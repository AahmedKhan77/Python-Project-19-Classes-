class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = Point()
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()
point1.move()

point2 = Point()
point2.x = 20
print(point2.x)
