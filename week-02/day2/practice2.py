class ContactList:

    def __init__(self, name, contact_list):
        self.name = name
        self.contact_list = contact_list

    def add_contact(self, contact_info):
            return self.contact_list.append(contact_info)
    
    def remove_contact(self, name):
         for name in self.contact_list:
              
              
friends = [{'name':'Alice','number':'867-5309'},{'name':'Bob', 'number':'555-5555'}]
work_buddies = [{'name':'Alice','number':'867-5309'},{'name':'Carlos', 'number':'555-5555'}]

my_friends_list = ContactList('My Friends', friends)
my_work_buddies = ContactList('Work Buddies', work_buddies)
dave = {'name':'Dave','number':'345-43443'}
print(my_friends_list.contact_list)
print(my_work_buddies.contact_list)
self.contact_list.add_contact({'name':'Dave','number':'345-43443'}))

dave = {'name': 'Dave', 'number': '345-43443'}
# my_friends_list.add_contact(dave)

# friends_i_work_with = my_friends_list.find_shared_contacts(my_work_buddies)