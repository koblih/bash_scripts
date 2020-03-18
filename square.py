class Square:
    def __init__(self, side):
        self.side = side
        self.square = self.side ** 2
        print(self.square)
       
    def __pow__(square1, square2):
        return(square1.square ** square2.square)

square1 = Square(3)
square1
square2 = Square(2)
square2
print("The power of the two squares is {}".format(square1 ** square2))
