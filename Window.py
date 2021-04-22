from array import *
import signal
import sys
from Camera import Camera
from Scene import Scene
import ObjectProcessing

class Window :

    #ASCII grayscale march, credit to Paul Bourke
    #_ascii_grayscale="$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1\{\}[]?-_+~<>i!lI;:,\"^`'. "
    _ascii_grayscale=" .'`^\",:;Il!i><~+_-?][\}\{1)(|\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
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


    def generate_output_string(self):
        for i in range(0, len(self.window), 6):
            for j in range(0, len(self.window[0]), 4):
                mean = (1/24) * (self.window[i  ][j] + self.window[i  ][j+1] + self.window[i  ][j+2] + self.window[i  ][j+3]+
                                 self.window[i+1][j] + self.window[i+1][j+1] + self.window[i+1][j+2] + self.window[i+1][j+3]+
                                 self.window[i+2][j] + self.window[i+2][j+1] + self.window[i+2][j+2] + self.window[i+2][j+3]+
                                 self.window[i+3][j] + self.window[i+3][j+1] + self.window[i+3][j+2] + self.window[i+3][j+3]+
                                 self.window[i+4][j] + self.window[i+4][j+1] + self.window[i+4][j+2] + self.window[i+4][j+3]+
                                 self.window[i+5][j] + self.window[i+5][j+1] + self.window[i+5][j+2] + self.window[i+5][j+3])
                mean = int(mean*70)
                self._output_string += self._ascii_grayscale[mean]
                # self._output_string += str(mean)
            self._output_string += "\n"



    def display_frame(self):
        #TODO: set cursor to the back
        print(self._output_string)


if __name__ == '__main__':
    window = Window()
    scene = Scene()
    camera = Camera(96, 96, scene)
    

    tree = ObjectProcessing.parse_into_objects("Assets/lowpolytree.obj")[2]
    test = []
    test.append(tree[0])
    print(test)
    # ObjectProcessing.scale_object(tree, 0)
    camera.scene.insert_object(tree, (1000, 1000, -30))
    # camera.scene.insert_object(default_triangle, (4, 2, -6))


    camera.generate_frame()
    window.window = camera.camera_view
    window.generate_output_string()
    window.display_frame()
    # while True:
    #     try:
    #         camera.generate_frame()
    #         window.window = camera.camera_view
    #         #print(window.window)
    #         window.generate_output_string()
    #         window.display_frame()
    #     except KeyboardInterrupt:
    #         print('Closing...')
    #         sys.exit(0)

