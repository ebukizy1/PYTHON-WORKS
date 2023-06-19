class MyClass:

    def __init__(self, lst):
        self.__lst = lst

    def change_element_in_lst(self):
            self.__lst[0] = 0
            self.__lst[-1] = 0
            return self.__lst




