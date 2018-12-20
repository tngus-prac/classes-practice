class User:
    pass

user1 = User()
# user1 is an "instance" of user
# user1 is an "object"
user1.first_name = "Dave"
user1.last_name = "Bowman"
# Field: Data attached to an object

print(user1.first_name)
print(user1.last_name)

first_name = "Arthur"
last_name = "Clarke"

print(first_name, last_name)

print(user1.first_name, user1.last_name)

user2 = User()
user2.first_name = "Frank"
user2.last_name = "Poole"
# values are attacked to user2
# each object can have different values for the same variale names

user1.age = 37
user2.favorite_book = "2001: A Space Odyssey"

print(user1.age)
