class Dog:

    def __init__(self, name, breed, color, sound):
        self.name = name
        self.breed = breed
        self.color = color
        self.sound = sound

    def speak(self): # example of an *instance method*
        print(f">> {self.sound}")
        
    def fetch(self, item):
        print(f">> {self.name} fetched the {item}")

fido = Dog("Fido", "Pointer", "white", "woof!")
bullet = Dog("Bullet", "Pug", "tan", "rark")
print(fido.speak())
print(fido.fetch("ball"))
print(bullet.speak())

class Snake:
    def __init__(self, name, motion):
        self.name = name
        self.motion = motion

cobra = Snake("Cobra", "slithers")
print(cobra)



