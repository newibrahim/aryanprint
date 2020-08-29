import webbrowser
# class with methods
class Walk:
    def walk(self):
        print("walk")


# class with attributes
class Color:
    color = "red"


# creating object
col = Color()
walk1 = Walk()
# using clases
print(col.color)
walk1.walk()

# Self
x = input("Do you want to see video? ")
if x == "yes":
    webbrowser.open("file:///C:/Users/Aryan/Pictures/Camera%20Roll/WIN_20200728_13_09_27_Pro.mp4")






