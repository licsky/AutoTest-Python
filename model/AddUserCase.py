class AddUserCase():
    def __init__(self, args):
        self.id = args[0]
        self.userName = args[1]
        self.password = args[2]
        self.sex = args[3]
        self.age = args[4]
        self.permission = args[5]
        self.isDelete = args[6]
        self.expected = args[7]
