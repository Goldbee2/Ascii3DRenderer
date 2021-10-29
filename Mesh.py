# -*- coding: utf-8 -*-

import array
import math

from Matrix import Matrix

class Mesh:

    faces = []
    bounding_box = [0, 0, 0]

    def __init__(self, array):
        for face in array:
            self.faces.append(face)
    
    def scale(self, scale):
        for i in range(len(self.faces)):
            for j in range(len(self.faces[i])):
                self.faces[i][j] = (
                    self.faces[i][j][0] * scale[0],
                    self.faces[i][j][1] * scale[1],
                    self.faces[i][j][2] * scale[2])
        self.create_bounding_box()



    def translate(self, translation):
        for i in range(len(self.faces)):
            for j in range(len(self.faces[i])):
                self.faces[i][j] = (
                self.faces[i][j][0] + translation[0],
                self.faces[i][j][1] + translation[1],
                self.faces[i][j][2] + translation[2])
        self.create_bounding_box()


    def rotate_x(self, angle):
        angle = math.radians(angle)
        for i in range(len(self.faces)):
            for j in range(len(self.faces[i])):
                self.faces[i][j] = Matrix.rotate_x(self.faces[i][j], angle)


    #   | cos t    0   sin t| |x|   | x cos t + z sin t|   |x'|
    #   |   0      1       0| |y| = |         y        | = |y'|
    #   |−sin t    0   cos t| |z|   |−x sin t + z cos t|   |z'|
    # credit: stackoverflow user legends2k
    def rotate_y(self, angle):
        angle = math.radians(angle)
        for i in range(len(self.faces)):
            for j in range(len(self.faces[i])):
                self.faces[i][j] = Matrix.rotate_y(self.faces[i][j], angle)


    #   |cos t   −sin t   0| |x|   |x cos t − y sin t|   |x'|
    #   |sin t    cos t   0| |y| = |x sin t + y cos t| = |y'|
    #   |  0       0      1| |z|   |        z        |   |z'|
    # credit: stackoverflow user legends2k
    def rotate_z(self, angle):
        angle = math.radians(angle)
        for i in range(len(self.faces)):
            for j in range(len(self.faces[i])):

                x, y, z = self.faces[i][j]
                x2 =  x * math.cos(angle) - y * math.sin(angle)
                y2 =  x * math.sin(angle) + y * math.cos(angle)
                z2 =  z

                self.faces[i][j] = (x2, y2, z2)



    def create_bounding_box(self):
        x_max = 0.0
        y_max = 0.0
        z_max = 0.0

        x_min = 0.0
        y_min = 0.0
        z_min = 0.0

        for face in self.faces:
            for vertex in face:
                if vertex[0] > x_max:
                    x_max = vertex[0]
                if vertex[1] > y_max:
                    y_max = vertex[1]
                if vertex[2] > z_max:
                    z_max = vertex[2]
                if vertex[0] < x_min:
                    x_min = vertex[0]
                if vertex[1] < y_min:
                    y_min = vertex[1]
                if vertex[2] < z_min:
                    z_min = vertex[2]

        max_coords = (x_max, y_max, z_max)
        min_coords = (x_min, y_min, z_min)
        self.bounding_box = (max_coords, min_coords)