from array import *
import signal
import sys
from Camera import Camera

class Window :

    #ASCII grayscale march, credit to Paul Bourke
    _ascii_grayscale="$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
    #goes like this: if >previousbrightness and LE next one, it gets that ones character#
    #The string to be printed to the console.
    _output_string=""

    #The windows dimensions in pixels TODO: accommodate resizing of window
    _window_width=800
    _window_height=600

    #Each character's width in internal pixels cast.
    _character_width=4
    _character_height=6
    
    window = []

    _kernel = []

    def __init__(self):
        self._create_kernel()
        for row in range(self._window_height):
            thisRow = []
            for column in range(self._window_width):
                thisRow.append(0)
            self.window.append(thisRow)
    
    def _create_kernel(self) :
        for row in range(self._character_height):
            for column in range(self._character_width):
                self._kernel.append(1/(self._character_height*self._character_width))

    def compute_characters_from_pixels(self):
        return(
            self._window_height//self._character_height, 
            self._window_width//self._character_width)

    def display_frame(self):
        #TODO: set cursor to the back
        print(self._output_string)


    # getters and setters

    def get_window_width(self):
        return _window_width
    
    def get_window_height(self):
        return _window_height

    def set_character_height(self, new_height):
        self._character_height = new_height
    
    def set_character_width(self, new_width):
        self._character_width = new_width


if __name__ == '__main__':
    window = Window()
    camera = Camera(800, 600)
    while True:
        try:
            window.display_frame()
            
        except KeyboardInterrupt:
            print('Closing...')
            sys.exit(0)