class User:
    users = 0
    all_users = []
    all_posts = []

    def __init__(self, name, email, country, relationship_status):
        self.name = name
        self.email = email
        self.country = country
        self.relationship_status = relationship_status
        self._post = ''
        self._all_posts = []

        User.users += 1
        User.all_users.append([self.name, self.email, self.country, self.relationship_status])
    
    @property
    def post(self):
        return self._post
    
    @post.setter
    def post(self, user_input):
        self._post = user_input
        self._all_posts.append(user_input)

        User.all_posts.append([self.name, user_input])
        print(user_input)
    
user1 = User('Rich', 'rich.man@gmail.com', 'Switzerland', 'single')
user2 = User('Poor', 'poor.man@gmail.com', 'Somalia', 'single')
user3 = User('Happy', 'happy.man@gmail.com', 'USA', 'single')
user4 = User('Stressed', 'stressed.man@gmail.com', 'Russia', 'married')

print(User.users)
print(User.all_users)
user1.post = "hello"
user2.post = "hey"
print(user1._post)
print(user2._post)
print(User.all_posts)


