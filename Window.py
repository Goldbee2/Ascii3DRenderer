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

    camera = None


    def _create_kernel(self) :
        for row in range(self._character_height):
            for column in range(self._character_width):
                self._kernel.append(1/(self._character_height*self._character_width))


    def generate_output_string(self):
        self._output_string="\n\n\n\n"
        for i in range(len(self.camera.view)):
            for j in range(len(self.camera.view[0])):
                brightness_index=int(self.camera.view[i][j]*13)
                self._output_string += self._ascii_grayscale[brightness_index]
            self._output_string += " \n"



    def display_frame(self):
        #TODO: set cursor to the back
        print(self._output_string)


if __name__ == '__main__':
    window = Window()
    scene = Scene()
    
    camera_width = input("Please enter the camera width: ")
    camera_height = input("Please enter the camera height: ")
    window.camera = Camera(int(camera_width), int(camera_height), scene, 100)
    
    # tree = ObjectProcessing.parse_into_meshes("Assets/lowpolytree.obj")[2]
    # tree.scale((1, -1, 1))
    # window.camera.scene.insert_object(tree, (0, 0, -30))

    # sphere = ObjectProcessing.parse_into_meshes("Assets/default_sphere.obj")[0]
    # sphere.scale((1, 1, 1))
    # window.camera.scene.insert_object(sphere, (0, 0, -4))
    
    unit_square = DefaultObject.UnitSquare()
    unit_square.scale((2, 2, 2))
    window.camera.scene.insert_object(unit_square, (0, 0, -12))
    # unit_square.rotate_y(45)
    # unit_square_5 = DefaultObject.UnitSquare()
    # unit_square_5.scale((8, 8, 8))
    # window.camera.scene.insert_object(unit_square_5, (0, 0, -40))




    unit_square_3 = DefaultObject.UnitSquare()
    unit_square_3.scale((16, 6, 6))
    # window.camera.scene.insert_object(unit_square_3, (0, -16, -30))

    # unit_square_2 = DefaultObject.UnitSquare()
    # unit_square_2.scale((24, 8, 8))
    # window.camera.scene.insert_object(unit_square_2, (0, 0, -40))

    # unit_square_4 = DefaultObject.UnitSquare()
    # unit_square_4.scale((16, 6, 6))
    # window.camera.scene.insert_object(unit_square_4, (0, 16, -30))

    # tt = ObjectProcessing.Mesh()
    # tt.faces = [[(0.0, -1.495895, -4.0), 
    #             (0.636238, -1.272489, -3.537751), 
    #             (-0.243016, -1.27249, -3.25206)]]
    
    # window.camera.scene.insert_object(tt, (0, 0, -8))
    
    # RAY:       (0.13097691563960823, 0.8251545685295318, -0.5495134080296649)
    # TRIANGLE:  [(0.0, -1.495895, -12.0), 
    #             (0.636238, -1.272489, -11.537751), 
    #             (-0.243016, -1.27249, -11.25206)]
    # INTERSECT: (7.621534986157959, 48.015670412795146, -31.976135979449396) 
    # NORMAL:    (0.29291763632754786, 0.31862688007667905, 0.9014855348927591)
    window.camera.ray_intersects((0.13097691563960823, 0.8251545685295318, -0.5495134080296649),
                                    [(0.0, -1.495895, -12.0),
                                    (0.636238, -1.272489, -11.537751),
                                    (-0.243016, -1.27249, -11.25206)],
                                    (0.29291763632754786, 0.31862688007667905, 0.9014855348927591))

    window.camera.generate_frame()
    window.generate_output_string()
    window.display_frame()
    os.system('setterm -cursor off')

    while 1:
        # break
        try:
            unit_square.rotate_x(1)
            # unit_square_5.rotate_z(6)


            # unit_square_2.rotate_y(6)
            unit_square_3.rotate_y(-7)
            # unit_square_4.rotate_y(-5)
            # tt.rotate_x(2)
            # sphere.rotate_x(6)
            

            window.camera.generate_frame()
            window.generate_output_string()
            window.display_frame()
            time.sleep(0.01)

        except KeyboardInterrupt:
            print('Closing...')
            sys.exit(0)

