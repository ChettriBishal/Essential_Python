'''
Ask the user for a list of 3 friends
For each friend, we'll tell the user whether they are nearby
For each nearby friend, we'll save their name to nearby_friends.txt

'''

people = open('people.txt','r')
people_list = people.readlines()

nearby_friends = open('nearby_friends.txt','a+')

for person in people_list:
    response = input(f"Is {person} nearby? y/n: ")
    if response == 'y':
        nearby_friends.write(f'{person}')

#now list the nearby friends

print("Nearby friends are as follows")
for friend in nearby_friends.readlines():
    print(friend)

people.close() 
nearby_friends.close() 
