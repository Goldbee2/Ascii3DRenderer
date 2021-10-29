from array import *
import signal
import sys
from Camera import Camera
from Scene import Scene
from ObjectProcessing import ObjTools
import DefaultObject
import os
import time

class Window :

    _ascii_grayscale = " ->:il?%$&@#BB"
    _output_string=""
    camera = None
    is_numbered = False



    def __init__(self, numbered):
        self.is_numbered = numbered



    def next_frame(self):
        self.camera.generate_frame()
        self.generate_output_string(self.is_numbered)
        self.display_frame()



    def generate_output_string(self, numbered):
        self._output_string="\n\n\n\n"
        for i in range(len(self.camera.view)):
            if(numbered):
                self._output_string += str(i)
            for j in range(len(self.camera.view[0])):
                brightness_index=int(self.camera.view[i][j]*13)
                self._output_string += self._ascii_grayscale[brightness_index]
            self._output_string += " \n"



    def display_frame(self):
        print(self._output_string)





if __name__ == '__main__':
    window = Window(numbered=True)
    scene = Scene()
    
    camera_width = input("Please enter the camera width: ")
    camera_height = input("Please enter the camera height: ")
    window.camera = Camera(int(camera_width), int(camera_height), scene, 100)
    
    # tree = ObjTools.parse_into_meshes("Assets/lowpolytree.obj")[2]
    # window.camera.scene.insert_object(tree, (0, 0, -30))

    # sphere = ObjectProcessing.parse_into_meshes("Assets/default_sphere.obj")[0]
    # window.camera.scene.insert_object(sphere, (0, 0, -4))
    
    cube = ObjTools.parse_into_meshes("Assets/cube.obj")[0]
    scene.insert_object(cube, (0, 0, -8))
    # cube.rotate_y(45)
    # print(cube.faces[0])


    # ut1 = DefaultObject.UnitTriangle1()
    # ut2 = DefaultObject.UnitTriangle2()
    # window.camera.scene.insert_object(ut1, (0, 0, 1))
    # window.camera.scene.insert_object(ut2, (0, 0, 1))

    # unit_square.rotate_y(180)
    
    # print(unit_square.faces)
    # unit_square.rotate_y(90)
    # window.camera.scene.insert_object(unit_square, (0, 0, -1))

    bt = DefaultObject.BorkedTriangle2()
    scene.insert_object(bt, (0, 0, 0))
    bt.translate((0, 0, -10))

    nt = DefaultObject.NormalTriangle2()
    scene.insert_object(nt, (0, 0, 0))

    os.system('setterm -cursor off')
    
    while 1:
        try:
            nt.rotate_x(2)
            cube.rotate_x(3)
            # bt.rotate_x(-2)
            window.next_frame()
            # for object in window.camera.scene.meshes :
            #     print(object.faces)
            time.sleep(0.006)
            

        except KeyboardInterrupt:
            print('\nClosing...')
            print('Object positions:')
            for object in scene.meshes :
                print(object.faces)
            sys.exit(0)

