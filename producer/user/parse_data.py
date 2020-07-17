import csv


def get_users(csv_filepath):
    """
    Gets all users data and parses them
    """
    with open(csv_filepath, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        users_list = [{'name': row[0], 'email': row[1]} for row in csv_reader]
        return users_list
