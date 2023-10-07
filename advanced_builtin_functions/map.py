friends = ['Snowden', 'Oppenheimer', 'Zuckerberg', 'Jobs', 'Seneca']

friends_lower = map(lambda x: x.lower(), friends)
# friends_lower = (friend.lower() for friend in friends)

print(friends_lower)  # map object
print(next(friends_lower))


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    def from_dict(cls, data):
        return cls(data['username'], data['password'])


users = [
    {'username': 'Snowden','password': '123'},
    {'username': 'Oppenheimer','password': 'einstien'}
]

# users = [User.from_dict(user) for user in users]
users = map(User.from_dict, users)