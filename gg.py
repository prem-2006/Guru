class animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        print("some sound")
    

class dog(animal):
    def speak(self):
        print("woof")

    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

class cat(animal):
    def speak(self):
        print("meow")


og = dog("buddy","pink")


at = cat("kitty")


og.speak()

at.speak()


print(og.name,og.color)

