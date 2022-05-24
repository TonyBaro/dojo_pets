class Pet:
    def __init__(self,data):
        self.name = data['name']
        self.type = data['type']
        self.tricks = data['tricks']
        self.health = 0
        self.energy = 0
    def sleep(self):
        self.health += 25
        return self
    def eat(self):
        self.health += 10
        self.energy += 5
        return self
    def play(self):
        self.health += 5
        return self
    def noise(self):
        if self.type == 'Dog':
            print ("woof")
        elif self.type == 'Cat':
            print ("MMMMMMMEEEEEEOOOOOOOWWWWWWWWWWWW!!!!!!!!!!!!")
        return self


class Ninja:
    def __init__(self,data):
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.pet = Pet(data)
        self.treats = data['treats']
        self.pet_food = data['pet_food']
    def walk(self):
        self.pet.play()
        print (self.pet.health)
        return self
    def feed(self):
        if self.pet_food >= 1:
            self.pet_food -= 1
            self.pet.eat()
            print (f'{self.pet.name} is well fed has {self.pet.energy} energy')
            return self
        elif self.pet_food <= 0:
            print (f'{self.pet.name} goes hungry')
            return self
    def bathe(self):
        self.pet.noise()




tony = Ninja({'first_name':'Tony','last_name':'Baro','treats':10,'pet_food':10,'name':'Cheebo','type':'Dog','tricks':'woof'})
ben = Ninja({'first_name':'Ben','last_name':'Reyes','treats':10,'pet_food':10,'name':'Franky','type':'Cat','tricks':'hide'})
print (tony.first_name)
print (tony.pet.name)
tony.walk()
tony.feed().feed().feed().feed().feed().feed().feed().feed().feed().feed().feed().feed().bathe()
ben.walk().feed().bathe()