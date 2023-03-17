class Player:
    def __init__(self, name):
        self.name = name
        self.position = 1

    def move(self, spaces):
        self.position += spaces

    def get_position(self):
        return self.position

    def set_position(self, new_position):
        self.position = new_position

    def __str__(self):
        return self.name

