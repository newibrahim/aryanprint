import webbrowser
class accounts():
    def __init__(self, a = "aryan ibrahim", b = 9, c = "aryanibrahimion@gmail.com"):
        self.a = a
        self.b = b
        self.c = c
    def check(self):
        x = str(input("enter your name: ")).lower()
        s = int(input("enter your age: "))
        e = str(input("enter your email: "))
        if x == self.a and s == self.b and e == self.c:
            print("you got the name correct")
            print("you got the age correct")
            print("you got the email correct")
            print("Lets sign you in!")
            webbrowser.open("https://mail.google.com/mail/u/2/?ogbl#inbox")
        else:
            print("Invalid!")


test = accounts()
test2 = accounts()
test.check()



