import math
import array
from Matrix import Matrix

class Camera :
    
    # stores view as array of brightness values.
    view = []
    width = 0
    height = 0
    scene = None
    max_rendering_depth = 50
    _field_of_view = math.pi/2 # dictates how far away projection screen should be from camera
    # row-major ordered. X, Y, Z, Translation
    # defaults to identity matrix (no change)
    # thank you to songho.ca/opengl/gl_camera for help understanding camera transformation matrices.
    transformation_matrix = [[1, 0, 0, 0],
                                    [0, 1, 0, 0],
                                    [0, 0, 1, 0],
                                    [0, 0, 0, 1]]



    def __init__(self, width, height, scene) :
        self.scene = scene
        self.width = width
        self.height = height
        for i in range(height):
            new_row = []
            for j in range(width):
               new_row.append(0) 
            self.view.append(new_row)



     #casts primary ray through center of each pixel
    def generate_frame(self):
        # pixel = 0
        # max_frames = len(self.camera_view) * len(self.camera_view[0])
        for row in range(len(self.view)):
            this_line = array.array('f')
            for col in range(len(self.view[0])):
                # pixel += 1
                x, y = self.matrix_to_world(row, col)
                ray = self.primary_ray(x, y)
                brightness_at_pixel = self.brightness_from_cast(ray)
                this_line.append(brightness_at_pixel)
                # if(pixel%100==0):
                    # print("generating pixel %d out of %d" % (pixel, max_frames))
            self.view[row] = (this_line)
            
    def matrix_to_world(self, row, column):
        width = self.width
        height = self.height
        x = column - (width/2)
        y = ((row * -1) + (height/2)) * 1.8
        return x, y


    # NAME:
    # INPUTS:
    # OUTPUTS:
    def primary_ray(self, x, y) :
        #return vector representing ray through center of pixel (x,y)?
        out_x = (y-(self.width/2))
        out_y = ((self.height/2)-x)
        z = -1
        #each vector has [x.5, y.5, -1]
        magnitude = math.sqrt(x**2 + y**2 + z**2)
        #divide x, y, -1 by magnitude to get direction(unit) vector.
        return (x/magnitude, y/magnitude, z/magnitude)



    # returns a brightness value
    #NOTE: in total, the brightness of a pixel consists of: angle to light, distance from light->light's distance function,
    #           if it's in shadow, and distance from origin
    def brightness_from_cast(self, ray):
        intersection, depth = self.find_nearest_intersection(ray)
        #for light in scene:
        #    pass
            #cast ray to light
            #if it's not obstructed, brightness of light = brightness of light -> individual light's distance function.
            #if intersection, is in shadow. ?brightness *= 0.5?
        # brightness = (1 / (0.2 * depth + 1)) if depth >= 0 else 0
        brightness = 1-(depth/self.max_rendering_depth)
        return brightness 



    #returns point, its normal, and its distance as a tuple
    def find_nearest_intersection(self, ray) :
        nearest_intersection = ((-1, -1, -1), self.max_rendering_depth)
        closest_distance = self.max_rendering_depth
        for mesh in self.scene.meshes:
            for triangle in mesh.faces:
                normal = self.calculate_normal(triangle) # vector cross product
                this_intersection = self.ray_intersects(ray, triangle, normal)
                # print(this_intersection)
                if this_intersection[1] < closest_distance:
                    closest_distance = this_intersection[1]
                    nearest_intersection = this_intersection
                        #NOTE: should be stored as a point in 
                        # space, its face normal, distance to origin.
        # print("ray: %s intersection: %s" % (str(ray), str(nearest_intersection)))
        return (nearest_intersection)



    def calculate_normal(self, triangle) :
        
        vertex_0, vertex_1, vertex_2 = triangle
        
        edge_1 = Matrix.subtract(vertex_1, vertex_0)
        edge_2 = Matrix.subtract(vertex_2, vertex_0)
        normal = Matrix.cross_product(edge_1, edge_2)
        normal = Matrix.normalize(normal)
        return normal


#FIXME: depth from origin calculated incorrectly. It should be the magnitude of the intersection vector.
    def ray_intersects(self, ray, triangle, normal):
    
        no_intersection = ((0, 0, 10), self.max_rendering_depth)
    
        vertex_0 = triangle[0]
        vertex_1 = triangle[1]
        vertex_2 = triangle[2]
        

        origin = (0, 0, 0)
        # The following lines use the equations:
        #    P = O + tR
        # where P is the intersection of the ray and triangle,
        # O is the origin, t is the distance from O to P, 
        # and R is the directional vector
        #    Ax + By + Cz + D = 0  
        # where A, B, and C are the components of the normal to the plane
        # and x, y, and z are the coordinates of any point on the plane
        # and D is the distance from the origin to the plane, parallel to the normal,
        D = Matrix.dot_product(normal, vertex_0)
        # print("D: %s" % str(D))
        A, B, C = normal
        # check if ray and plane are (almost) parallel
        # if D < 0:
        #     return no_intersection
        
        t = (Matrix.dot_product(normal, origin) + D) / Matrix.dot_product(normal, ray)
        # print("t: %s" % str(t))
        # if the triangle is behind the camera or too far away
        if (t > self.max_rendering_depth) or (t < 0):
            return no_intersection

        intersection_point =  Matrix.scale(ray, t)
        # print("intersection point: %s" % str(intersection_point))
        
        edge_0 = Matrix.subtract(vertex_1, vertex_0)
        perpendicular_vector_0 = Matrix.subtract(intersection_point, vertex_0)
        C = Matrix.cross_product(edge_0, perpendicular_vector_0)
        N = Matrix.dot_product(C, normal)
        if(N < 0) :
            # print("Case 1 failed")
            return no_intersection
        
        edge_1 = Matrix.subtract(vertex_2, vertex_1)
        perpendicular_vector_1 = Matrix.subtract(intersection_point, vertex_1)
        C = Matrix.cross_product(edge_1, perpendicular_vector_1)
        N = Matrix.dot_product(C, normal)
        if(N < 0) :
            # print("Case 2 failed")
            return no_intersection
        
        edge_2 = Matrix.subtract(vertex_0, vertex_2)
        perpendicular_vector_2 = Matrix.subtract(intersection_point, vertex_2)
        C = Matrix.cross_product(edge_2, perpendicular_vector_2) 
        N = Matrix.dot_product(C, normal)
        if(N < 0) :
            # print("Case 3 failed")
            return no_intersection
        
        return (intersection_point, t)


    def shadow_ray(self, pointA, pointB):
        pass



    def camera_x_axis(self) :
        return self.transformation_matrix[0]
    
    def camera_y_axis(self) :
        return self.transformation_matrix[1]

    def camera_z_axis(self) :
        return self.transformation_matrix[2]
    
    def camera_translation(self) :
        return self.transformation_matrix[3]



    # #probably wrong
    # def compute_ray_direction(self, x, y, z, width, height) :
    #     return((x - width / 2),
    #            (height / 2 - y),
    #            (-(height/2) / math.tan(self._field_of_view*0.5)))

