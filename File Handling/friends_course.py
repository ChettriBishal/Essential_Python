# read from people first
'''
Here we use sets to make our life easier
'''
import os

people = open("people.txt", "r")
people_list = people.readlines()

#remove \n from people_list

people_list = [person.strip() for person in people_list]
print(people_list)

friends = input("Enter three friends who stay nearby: ").split(',')


people_set = set(people_list)
friends_set = set(friends)

print(people_set)
print(friends_set)


friend_nearby_set = friends_set.intersection(people_set)

near = open("nearby_friends.txt", "a+")

for friend in friend_nearby_set:
    print(f"{friend} is nearby!")
    near.write(f'{friend}\n')

print("Intersection here: ")
print(near.readlines())

near.close()
people.close()
