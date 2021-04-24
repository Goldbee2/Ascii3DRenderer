from array import *
import signal
import sys
from Camera import Camera
from Scene import Scene
import ObjectProcessing

class Window :

    #ASCII grayscale march, credit to Paul Bourke
    #_ascii_grayscale="$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1\{\}[]?-_+~<>i!lI;:,\"^`'. "
    # _ascii_grayscale=" .'`^\",:;Il!i><~+_-?][\}\{1)(|\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
    _ascii_grayscale = " .:-=+*#%@"
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

    def __init__(self):
        self._create_kernel()


    def _create_kernel(self) :
        for row in range(self._character_height):
            for column in range(self._character_width):
                self._kernel.append(1/(self._character_height*self._character_width))


    def generate_output_string(self):
        self._output_string += "\n\n\n\n"
        for i in range(len(self.camera.view)):
            for j in range(len(self.camera.view[0])):
                # mean = (1/24) * (self.window[i  ][j] + self.window[i  ][j+1] + self.window[i  ][j+2] + self.window[i  ][j+3]+
                                #  self.window[i+1][j] + self.window[i+1][j+1] + self.window[i+1][j+2] + self.window[i+1][j+3]+
                                #  self.window[i+2][j] + self.window[i+2][j+1] + self.window[i+2][j+2] + self.window[i+2][j+3]+
                                #  self.window[i+3][j] + self.window[i+3][j+1] + self.window[i+3][j+2] + self.window[i+3][j+3]+
                                #  self.window[i+4][j] + self.window[i+4][j+1] + self.window[i+4][j+2] + self.window[i+4][j+3]+
                                #  self.window[i+5][j] + self.window[i+5][j+1] + self.window[i+5][j+2] + self.window[i+5][j+3])
                brightness_index=int(self.camera.view[i][j]*10)
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
    window.camera = Camera(int(camera_width), int(camera_height), scene)
    

    # tree = ObjectProcessing.parse_into_meshes("Assets/lowpolytree.obj")[2]
    # print(tree.faces)
    # tree.scale_mesh(0.1)
    # window.camera.scene.insert_object(tree, (0, -20, -30))
    
    # test_triangle = ObjectProcessing.Mesh()
    # test_triangle.faces = [[[-20, -20, 0],[20, -20, 0],[-20, 20, 0]]]
    # window.camera.scene.insert_object(test_triangle, (0, 0, -4))
    # print(test_triangle.faces)

    sphere = ObjectProcessing.parse_into_meshes("Assets/mit_sphere.obj")[0]
    # sphere.scale_mesh(0.2)
    window.camera.scene.insert_object(sphere, (0, 0, 0))
    sphere.create_bounding_box()
    print(sphere.bounding_box)
    
    # test_ray = window.camera.primary_ray(0, 20)
    # test_ray = (0, 0, -1)
    # print("TEST RAY %s: " % str(test_ray))

    # print(window.camera.matrix_to_world(20, 20))
    # test_normal = window.camera.calculate_normal(test_triangle.faces[0])
    # print("TEST NORMAL %s: " % str(test_normal))
    # print(window.camera.ray_intersects(test_ray, test_triangle.faces[0], (0, 0, -1)))
    
    # unit_triangle_ll = ObjectProcessing.Mesh()
    # unit_triangle_ll.faces = [[[-1, -1, 0], [1, -1, 0], [-1, 1, 0]]]
    # unit_triangle_ll.scale_mesh(10)
    # window.camera.scene.insert_object(unit_triangle_ll, (0, 0, -1))

    # unit_triangle_ur = ObjectProcessing.Mesh()
    # unit_triangle_ur.faces = [[[-1, 1, 0], [1, -1, 0], [1, 1, 0]]]
    # unit_triangle_ur.scale_mesh(10)
    # window.camera.scene.insert_object(unit_triangle_ur, (0, 0, -1))


    window.camera.generate_frame()
    window.generate_output_string()
    window.display_frame()

     
    while True:
        try:
            sphere.translate_mesh((0, 0, -2))
            # sphere.create_bounding_box()
            # print(sphere.bounding_box)
            window.camera.generate_frame()
            #print(window.window)
            # print(window.camera.view)
            # sphere.translate_mesh((1, 0, 0))
            # test_triangle.translate_mesh((0, 0, 1))
            window.generate_output_string()
            window.display_frame()
        except KeyboardInterrupt:
            print('Closing...')
            sys.exit(0)

