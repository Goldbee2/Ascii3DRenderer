import math
import array
from Matrix import Matrix

class Camera :

    # stores view as array of brightness values.
    view = []
    width = 0
    height = 0
    aspect_ratio = 0
    fov = 0
    scene = None
    max_rendering_depth = 60



    def __init__(self, width, height, scene, fov) :
        self.scene = scene
        self.width = width
        self.height = height
        self.aspect_ratio = height/width
        self.fov = fov
        for i in range(height):
            new_row = []
            for j in range(width):
               new_row.append(0) 
            self.view.append(new_row)



    def generate_frame(self):
        for row in range(len(self.view)):
            this_line = array.array('f')

            for col in range(len(self.view[0])):
                ray = self.primary_ray(row, col, -1)
                brightness_at_pixel = self.brightness_from_cast(ray)
                
                this_line.append(brightness_at_pixel)

            self.view[row] = (this_line)



    def primary_ray(self, x, y, z) :
        x, y = self.matrix_to_xy(x, y)
        x, y = self.xy_to_canvas(x, y)
        magnitude = Matrix.magnitude((x, y, z))
        return (x/magnitude, y/magnitude, z/magnitude)



    def matrix_to_xy(self, row, column):

        x = column - (self.width / 2)
        y = (row * -1) + (self.height / 2)

        return x, y



    def xy_to_canvas(self, x, y):
        
        canvas_distance = 1 #here to clarify math in case a different distance is used
        canvas_width = 2*(math.tan(math.radians(self.fov) / 2 * canvas_distance))
        canvas_height = canvas_width * 1.8*self.aspect_ratio

        x = x / self.width * canvas_width
        y = y / self.height * canvas_height

        return x, y
    
    

    def brightness_from_cast(self, ray):
        intersection, depth = self.find_nearest_intersection(ray)
        brightness = 1-(depth/self.max_rendering_depth)
        return brightness 



    def find_nearest_intersection(self, ray) :
        nearest_intersection = ((0, 0, 1), self.max_rendering_depth)
        closest_distance = self.max_rendering_depth
        
        for mesh in self.scene.meshes:
            
            for triangle in mesh.faces:
                normal = self.calculate_normal(triangle) # vector cross product
                this_intersection = self.ray_intersects(ray, triangle, normal)
                
                if this_intersection[1] < closest_distance:
                    closest_distance = this_intersection[1]
                    nearest_intersection = this_intersection
        
        return (nearest_intersection)



    def calculate_normal(self, triangle) :
        
        vertex_0, vertex_1, vertex_2 = triangle
        
        edge_1 = Matrix.subtract(vertex_1, vertex_0)
        edge_2 = Matrix.subtract(vertex_2, vertex_0)
        normal = Matrix.cross_product(edge_1, edge_2)
        normal = Matrix.normalize(normal)
        return normal



    def ray_intersects(self, ray, triangle, normal):
        """
        A method to detect ray-triangle intersection.
        """

        no_intersection = ((0, 0, 10), self.max_rendering_depth+1)

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
        A, B, C = normal
        D = Matrix.dot_product(normal, vertex_0)
        
        # check if ray and plane are (almost) parallel
        if abs(Matrix.dot_product(normal, ray)) < 0.01:
            return no_intersection
 
        t = (Matrix.dot_product(normal, origin) + D) / Matrix.dot_product(normal,ray)
        # if the triangle is behind the camera or too far away
        if (t > self.max_rendering_depth+1) or (t < 0):
            return no_intersection

        intersection_point =  Matrix.scale(ray, t)
        
        # Right hand intersection test
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
        
        return (intersection_point, t)


    def shadow_ray(self, pointA, pointB):
        pass