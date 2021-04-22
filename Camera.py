import math
import array
from Matrix import Matrix

class Camera :
    
    # stores view as array of brightness values.
    camera_view = []
    width = 0
    width = 0
    scene = None
    max_rendering_depth = 600
    _field_of_view = math.pi/2 # dictates how far away projection screen should be from camera
    # row-major ordered. X, Y, Z, Translation
    # defaults to identity matrix (no change)
    # thank you to songho.ca/opengl/gl_camera for help understanding camera transformation matrices.
    camera_transformation_matrix = [[1, 0, 0, 0],
                                    [0, 1, 0, 0],
                                    [0, 0, 1, 0],
                                    [0, 0, 0, 1]]



    def __init__(self, width, height, scene) :
        self.scene = scene
        self.width = width
        self.height = height
        for i in range(height):
            new_row = []
            for i in range(width):
               new_row.append(0) 
            self.camera_view.append(new_row)



     #casts primary ray through center of each pixel
    def generate_frame(self):
        pixel = 0
        max_frames = len(self.camera_view) * len(self.camera_view[0])
        for x in range(len(self.camera_view)):
            this_line = array.array('f')
            for y in range(len(self.camera_view[0])):
                pixel += 1
                ray = self.primary_ray(x, y)
                brightness_at_pixel = self.brightness_from_cast(ray)
                this_line.append(brightness_at_pixel)
                if(pixel%100==0):
                    print("generating pixel %d out of %d" % (pixel, max_frames))
            self.camera_view[x] = (this_line)
            



    # NAME:
    # INPUTS:
    # OUTPUTS:
    def primary_ray(self, x, y) :
        #return vector representing ray through center of pixel (x,y)?
        x = ( 2* (x + 0.5)/(self.width-1))
        y = (1 - 2 * (y + 0.5)/(self.height))
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
        for object in self.scene.objects:
            for triangle in object:
                normal = self.calculate_normal(triangle) # vector cross product
                this_intersection = self.ray_intersects(ray, triangle, normal)
                if this_intersection[1] < closest_distance:
                    closest_distance = this_intersection[1]
                    nearest_intersection = this_intersection
                        #NOTE: should be stored as a point in 
                        # space, its face normal, distance to origin.
        return (nearest_intersection)



    def calculate_normal(self, triangle) :
        
        vertex_0, vertex_1, vertex_2 = triangle
        
        edge_1 = Matrix.subtract(vertex_1, vertex_0)
        edge_2 = Matrix.subtract(vertex_2, vertex_0)

        normal = Matrix.cross_product(edge_1, edge_2)
        
        return normal



    def ray_intersects(self, ray, triangle, normal):
    
        no_intersection = ((0, 0, self.max_rendering_depth+1), self.max_rendering_depth)
    
        vertex_0 = triangle[0]
        vertex_1 = triangle[1]
        vertex_2 = triangle[2]
        # check if ray and plane are parallel
        dot_product = Matrix.dot_product(ray, normal)
        if dot_product < 0.01:
            return no_intersection
        # compute distance from origin to point being checked
        # dot product normal with vertex zero
        distance_from_origin = Matrix.dot_product(vertex_0, normal)

        # compute distance from origin to plane(parallel to plane's normal)
        distance_to_plane = distance_from_origin / dot_product
        # if triangle is behind the ray
        if distance_to_plane < 0 :
            return no_intersection

        intersection_point =  Matrix.scale(ray, distance_to_plane) #scales vector --
       
        
        edge_0 = Matrix.subtract(vertex_1, vertex_0)
        perpendicular_vector_0 = Matrix.subtract(intersection_point, vertex_0)
        C = Matrix.cross_product(edge_0, perpendicular_vector_0)
        N = Matrix.dot_product(C, normal)
        if(N < 0) :
            return no_intersection
        
        edge_1 = Matrix.subtract(vertex_2, vertex_1)
        perpendicular_vector_1 = Matrix.subtract(intersection_point, vertex_1)
        C = Matrix.cross_product(edge_1, perpendicular_vector_1)
        N = Matrix.dot_product(C, normal)
        if(N < 0) :
            return no_intersection
        
        edge_2 = Matrix.subtract(vertex_0, vertex_2)
        perpendicular_vector_2 = Matrix.subtract(intersection_point, vertex_2)
        C = Matrix.cross_product(edge_2, perpendicular_vector_2) 
        N = Matrix.dot_product(C, normal)
        if(N < 0) :
            return no_intersection
        
        return (intersection_point, distance_from_origin)


    def shadow_ray(self, pointA, pointB):
        pass



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

