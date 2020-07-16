from users.parse_data import get_users
from users.publish import publish


users_dict = get_users('producer/data/data_example.csv')
print('users_dict: ', users_dict)
publish(users_dict)
