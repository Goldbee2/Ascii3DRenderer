from array import *

class Window:
    _window_width=80
    _window_height=24
    
    window = []
    
    def __init__(self):
        for row in range(self._window_height):
            thisRow = []
            for column in range(self._window_width):
                thisRow.append(" ")
            self.window.append(thisRow)

    def display_frame(self):
        for row in self.window:
            for pixel in row:
                print(pixel, end="")
            print()
            

    def set_pixel(self, x, y, char):
        self.window[x][y] = char

    def get_window_width(self):
        return _window_width
    
    def get_window_height(self):
        return _window_height

if __name__ == '__main__':
    window = Window()
    window.display_frame()