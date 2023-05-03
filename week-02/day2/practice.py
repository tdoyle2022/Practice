
# lst = [{'name': 'Terry', 'number': 98784738}, {'name': 'Alice', 'number': 938473974}]
# l = sorted(lst, key=lambda d: d['name'])
# print(l)

# lst = ['kldfj', 'ldkjfd']
# print(id(lst))
class Food:
    def __init__(self, name, shape):
        self.name = name
        self.shape = shape
    
class Fruit(Food):
    @property
    def say_fruit(self):
        return 'Fruit!'

fruit1 = Fruit('banana', 'oblong')
print(fruit1.name)
print(fruit1.say_fruit)