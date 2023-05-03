import csv

class Cat:
    
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

class Dog:
    
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

animal_type = input("cats or dogs? \n")
try:
    data = open (f'./data/{animal_type}.csv')
    reader = csv.DictReader(data)
    animals = []
    for row in reader:
        if animal_type == 'cats':
            new_animal = Cat(row['name'], row['age'], row['breed'])
        elif animal_type == 'dogs':
            new_animal = Dog(row['name'], row[ 'age'], row['breed'])
    animals.append(new_animal)
    for animal in animals:
        print (animal)
    data.close ()
except:
    print (f"Sorry, we don't have any {animal_type} here.")