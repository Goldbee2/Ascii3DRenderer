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

    _ascii_grayscale = " ->:il?%$&#B@@"
    _output_string=""
    camera = None

    def display_frame(self):
        print(self._output_string)


    def generate_output_string(self):
        self._output_string="\n\n\n\n"
        for i in range(len(self.camera.view)):
            for j in range(len(self.camera.view[0])):
                brightness_index=int(self.camera.view[i][j]*13)
                self._output_string += self._ascii_grayscale[brightness_index]
            self._output_string += " \n"



if __name__ == '__main__':
    window = Window()
    scene = Scene()
    
    camera_width = input("Please enter the camera width: ")
    camera_height = input("Please enter the camera height: ")
    window.camera = Camera(int(camera_width), int(camera_height), scene, 100)
    
    # tree = ObjectProcessing.parse_into_meshes("Assets/lowpolytree.obj")[2]
    # window.camera.scene.insert_object(tree, (0, 0, -30))

    # sphere = ObjectProcessing.parse_into_meshes("Assets/default_sphere.obj")[0]
    # window.camera.scene.insert_object(sphere, (0, 0, -4))
    
    unit_square = DefaultObject.UnitSquare()
    unit_square.scale((2, 2, 2))
    window.camera.scene.insert_object(unit_square, (0, 0, -12))

    window.camera.generate_frame()
    window.generate_output_string()
    window.display_frame()
    os.system('setterm -cursor off')

    while 1:
        try:
            unit_square.rotate_x(1)

            window.camera.generate_frame()
            window.generate_output_string()
            window.display_frame()
            time.sleep(0.01)

        except KeyboardInterrupt:
            print('Closing...')
            sys.exit(0)

