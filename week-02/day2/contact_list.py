# Let's create a class for creating contact lists. 
# Each contact list should store its contacts as a list of dictionaries, 
# containing name and phone number. 
# The list should be sorted by the contacts' name. 
# The contact list should also have a name that distinguishes it, 
# e.g. "School Friends", "Extended Family", or "Work Buddies". 
# The contact list should have 3 instance methods:

# add_contact({}) 
    # - should add a new contact to the list, 
    # - while keeping the list sorted
# remove_contact('Alice') should remove a contact from the list by name.
# find_shared_contacts(ContactList) should accept another contact list as an argument, and then return a new ContactList to indicate all the contacts that appear in both lists (exact same name and phone number).
# For example:

class ContactList:

    def __init__(self, name, initial_contacts):
        self._name = name
        self._contacts = initial_contacts

    def add_contact(self, contact):
        self._contacts.append(contact)
        self._contacts = sorted(self._contacts, key=lambda d: d['name'])
        return self._contacts
    
    def remove_contact(self, contact):
        for i in range(len(self._contacts)-1):
            if self._contacts[i]['name'] == contact:
                del self._contacts[contact]
            return self._contacts


friends = [
    {'name':'Alice','number':'867-5309'},
    {'name':'Bob', 'number':'555-5555'},
]
print()
work_buddies = [{'name':'Alice','number':'867-5309'},{'name':'Carlos', 'number':'555-5555'}]

my_friends_list = ContactList('My Friends', friends)
my_work_buddies = ContactList('Work Buddies', work_buddies)

add_friend = my_friends_list.add_contact({'name':'April','number':'555-5309'})
print(add_friend)
remove_friend = my_friends_list.remove_contact({'name':'Bob', 'number':'555-5555'})
print(remove_friend)

# friends_i_work_with = my_friends_list.find_shared_contacts(my_work_buddies)
