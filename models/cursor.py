class Cursor:
    def __init__(self, max_x, max_y):
        self.__x = 0
        self.__y = 0
        self.__max_x = max_x
        self.__max_y = max_y

    def move_down(self):
        self.__x = min(self.__max_x, self.__x+1)

    def move_up(self):
        self.__x = max(0, self.__x-1)

    def move_left(self):
        self.__y = max(0, self.__y-1)

    def move_right(self):
        self.__y = min(self.__max_y, self.__y+1)

    def get_pos(self):
        return (self.__x, self.__y)
