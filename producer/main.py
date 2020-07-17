import time

from user.parse_data import get_users
from user.publish import publish


time.sleep(20)
users_list = get_users('./data/data_example.csv')
print('users_list: ', users_list)
for value in users_list:
    publish(value)
