""" Grocery List
    Rachel Remick
    The purpose of this class is to represent the users in the grocery list.
    9/27/25
"""
class UserList:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)
