class Point:
    default_color = "red"

    def point(self):
        print(f"walk with color")

# Check if the default color is changed using the class name and affects your object
point1 = Point()
Point.default_color = "blue"
print(Point.default_color)

point1.default_color = "red"
print(point1.default_color)
# object does not affect class but class affect object


