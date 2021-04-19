import math

class Camera :
    
    camera_view = []
    scene = None

    def __init__(self, width, height, scene) :
        self.scene = scene
        for i in range(height):
            new_row = []
            for i in range(width):
               new_row.append(0) 
            self.camera_view.append(new_row)

    

    # stores view as array of brightness values.

    # okay I have a bunch of objects with points relative to their origin, and where there origin is located relative to the global origin.
    # thank you to songho.ca/opengl/gl_camera for help understanding camera transformation matrices.


    #casts primary ray through center of each pixel
    def generate_frame(self):
        for x in range(len(self.camera_view)):
            for y in range(len(self.camera_view[0])):
                ray = primary_ray(x, y)
                cast(None)
    
    #checks every object for intersections
    def cast(self, ray):
        for object in scene:
            for polygon in object:
                # if normal is not facing away from us, or if normal is not at orthogonal angle,
                #    (angle between ray and normal is between pi/2 and 3pi/2,)
                #    ?and if at least one point within distance cutoff?:
                #    see if it's within the shape.
                #    how to tell this: if a ray, cast in a single direction, intersects shape boundaries an odd number of times
                # if it is,
                    #closest intersection = max (closest intersection, new intersection)
                        #NOTE: should be stored as a shape struct and a distance between intersection and origin.
                #depth = distance from origin

        #shoot shadow ray from intersection to light
        for light in scene:
            pass
            #cast ray to light
            #if it's not obstructed, brightness of light = brightness of light -> individual light's distance function.
            #if intersection, is in shadow. ?brightness *= 0.5?

#NOTE: in total, the brightness of a pixel consists of: angle to light, distance from light->light's distance function
#           , if it's in shadow, and distance from origin

    

    def primary_ray(self, x, y) :
        #return vector representing ray through center of pixel (x,y)?
        pass

    def shadow_ray(self, pointA, pointB):
        pass

    #row-major ordered. X, Y, Z, Translation
    #defaults to identity matrix (no change)
    camera_transformation_matrix = [[1, 0, 0, 0],
                                    [0, 1, 0, 0],
                                    [0, 0, 1, 0],
                                    [0, 0, 0, 1]]

    _field_of_view = math.pi/2

    def camera_x_axis(self) :
        return self.camera_transformation_matrix[0]
    
    def camera_y_axis(self) :
        return self.camera_transformation_matrix[1]

    def camera_z_axis(self) :
        return self.camera_transformation_matrix[2]
    
    def camera_translation(self) :
        return self.camera_transformation_matrix[3]

    # #probably wrong
    # def compute_ray_direction(self, x, y, z, width, height) :
    #     return((x - width / 2),
    #            (height / 2 - y),
    #            (-(height/2) / math.tan(self._field_of_view*0.5)))


    def create_view(self) :
        pass