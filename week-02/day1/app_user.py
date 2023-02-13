class User:
    pass

    def __init__(self, name, email, country, relationship_status):
        self.name = name
        self.email = email
        self.country = country
        self.relationship_status = relationship_status

user1 = User('Rich', 'rich.man@gmail.com', 'Switzerland', 'single')
user2 = User('Poor', 'poor.man@gmail.com', 'Somalia', 'single')
user3 = User('Happy', 'happy.man@gmail.com', 'USA', 'single')
user4 = User('Stressed', 'stressed.man@gmail.com', 'Russia', 'married')
print(user1)