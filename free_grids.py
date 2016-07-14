class FreeGrid:

    def __init__(self, x, y, is_available):
        self.x = x
        self.y = y
        self.is_available = is_available

    def get_xy(self):
        return (self.x, self.y)