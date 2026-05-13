#6-misol
class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password

    def get_password(self):
        return self.__password

    def set_password(self, new_password):
        self.__password = new_password


u1 = User('admin', 12345)
print(u1.username)
print(u1.get_password())
u1.set_password(54321)
print(u1.get_password())
