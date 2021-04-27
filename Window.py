from array import *
import signal
import sys
from Camera import Camera
from Scene import Scene
import ObjectProcessing
import DefaultObject
import os
import time

class Window :

    #ASCII grayscale march, credit to Paul Bourke
    #_ascii_grayscale="$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1\{\}[]?-_+~<>i!lI;:,\"^`'. "
    # _ascii_grayscale=" .'`^\",:;Il!i><~+_-?][\}\{1)(|\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
    _ascii_grayscale = " .:-=+*#%@"
    _ascii_grayscale = " ->:il?%$&#B@@"
    #goes like this: if >previousbrightness and LE next one, it gets that ones character#
    #The string to be printed to the console.
    _output_string=""

    #The windows dimensions in pixels TODO: accommodate resizing of window
    _window_width=800
    _window_height=600

    #Each character's width in internal pixels cast.
    _character_width=4
    _character_height=6

    _kernel = []

    camera = None


    def _create_kernel(self) :
        for row in range(self._character_height):
            for column in range(self._character_width):
                self._kernel.append(1/(self._character_height*self._character_width))


    def generate_output_string(self):
        self._output_string="\n\n\n\n"
        for i in range(len(self.camera.view)):
            for j in range(len(self.camera.view[0])):
                # mean = (1/24) * (self.window[i  ][j] + self.window[i  ][j+1] + self.window[i  ][j+2] + self.window[i  ][j+3]+
                                #  self.window[i+1][j] + self.window[i+1][j+1] + self.window[i+1][j+2] + self.window[i+1][j+3]+
                                #  self.window[i+2][j] + self.window[i+2][j+1] + self.window[i+2][j+2] + self.window[i+2][j+3]+
                                #  self.window[i+3][j] + self.window[i+3][j+1] + self.window[i+3][j+2] + self.window[i+3][j+3]+
                                #  self.window[i+4][j] + self.window[i+4][j+1] + self.window[i+4][j+2] + self.window[i+4][j+3]+
                                #  self.window[i+5][j] + self.window[i+5][j+1] + self.window[i+5][j+2] + self.window[i+5][j+3])
                brightness_index=int(self.camera.view[i][j]*13)
                self._output_string += self._ascii_grayscale[brightness_index]
                # self._output_string += str(mean)
            self._output_string += " \n"



    def display_frame(self):
        #TODO: set cursor to the back
        print(self._output_string)


if __name__ == '__main__':
    window = Window()
    scene = Scene()
    
    camera_width = input("Please enter the camera width: ")
    camera_height = input("Please enter the camera height: ")
    window.camera = Camera(int(camera_width), int(camera_height), scene, 90)
    
    # tree = ObjectProcessing.parse_into_meshes("Assets/lowpolytree.obj")[2]
    # print(tree.faces)
    # tree.scale_mesh(0.1)
    # window.camera.scene.insert_object(tree, (0, -20, -30))

    sphere = ObjectProcessing.parse_into_meshes("Assets/default_sphere.obj")[0]
    sphere.scale((1, 1, 1))
    # window.camera.scene.insert_object(sphere, (0, 0, -5))
    # sphere.create_bounding_box()
    # print(sphere.bounding_box)
    
    unit_square = DefaultObject.UnitSquare()
    unit_square.scale((2, 2, 2))
    window.camera.scene.insert_object(unit_square, (0, 0, -10))

    unit_square_2 = DefaultObject.UnitSquare()
    unit_square_2.scale((8, 8, 8))
    window.camera.scene.insert_object(unit_square_2, (0, 0, -20))

    window.camera.generate_frame()
    window.generate_output_string()
    window.display_frame()
    os.system('setterm -cursor off')
    while True:
        try:
            # sphere.translate_mesh((0, 0, -2))
            # sphere.create_bounding_box()
            # print(sphere.bounding_box)
            # unit_square.scale((1, -1, 1))
            
            # sphere.scale((0.1, 0.1, 0.1))
            # sphere.translate((0, -2, 0))
            unit_square.rotate_x(-2)
            unit_square_2.rotate_x(2)
            # for mesh in window.camera.scene.meshes:
                # mesh.translate((0, 0, -0.02))
                # mesh.rotate_x(2)
            #print(window.window)
            # print(window.camera.view)
            # sphere.translate_mesh((1, 0, 0))
            # test_triangle.translate_mesh((0, 0, 1))
            window.camera.generate_frame()
            
            window.generate_output_string()
            window.display_frame()
            
            time.sleep(0.1)
        except KeyboardInterrupt:
            print('Closing...')
            sys.exit(0)

