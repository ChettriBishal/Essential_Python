friends = ["Rolf", "John","Anna"]

index = 0

for friend in friends:
    print(index, friend)
    index += 1


# To avoid doing this we'll enumerate which combines index with the element

for index, friend in enumerate(friends):
    print(index, friend)

#list of enumerate of friends
print(list(enumerate(friends)))


#changing the start value for enumeration
for index, friend in enumerate(friends, start = 1):
    print(index, friend)

#also use it to create dictionaries
friends_dict = dict(enumerate(friends))  # {0: 'Rolf', 1: 'John', 2: 'Anna'}
print(friends_dict)
