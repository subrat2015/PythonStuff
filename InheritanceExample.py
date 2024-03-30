class Animal:
    def __int__(self):
        self.num_eyes = 2

    def breath(self):
        print("Inhale Exhale")


class Fish(Animal):
    def __int__(self):
        super().__int__()

    def breath(self):
        super().breath()
        print("Doing it under water")

    def swim(self):
        print("Moving in water")


nemo = Fish()
nemo.breath()
nemo.swim()
print(nemo.num_eyes)
