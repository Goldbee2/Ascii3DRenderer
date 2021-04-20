import math

class Camera :
    
    # stores view as array of brightness values.
    camera_view = []
    scene = None
    max_rendering_depth = 999

    def __init__(self, width, height, scene) :
        self.scene = scene
        for i in range(height):
            new_row = []
            for i in range(width):
               new_row.append(0) 
            self.camera_view.append(new_row)

     #casts primary ray through center of each pixel
    def generate_frame(self):
        for x in range(len(self.camera_view)):
            for y in range(len(self.camera_view[0])):
                ray = primary_ray(x, y)
                camera_view[x][y] = brightness_from_cast(ray, scene)
    
    
    # returns a brightness value
    #NOTE: in total, the brightness of a pixel consists of: angle to light, distance from light->light's distance function,
    #           if it's in shadow, and distance from origin
    def brightness_from_cast(self, ray):
        # shoots primary ray, look for intersection
        intersection, intersection_normal, depth = find_nearest_intersection(ray)
        # shoot shadow ray from intersection to light
        
        #for light in scene:
        #    pass
            #cast ray to light
            #if it's not obstructed, brightness of light = brightness of light -> individual light's distance function.
            #if intersection, is in shadow. ?brightness *= 0.5?
        return (1 / (0.2 * depth + 1)) if depth >= 0 else 0

    #returns point, its normal, and its distance as a tuple
    def find_nearest_intersection(self, ray, scene) :
        nearest_intersection = (-1, -1, -1)
        closest_distance = self.max_rendering_depth
        for object in scene:
            for triangle in object: #for each face
                # compute plane's normal
                normal = None
                # if normal is not facing away from us, or if normal is not at orthogonal angle,
                #    (angle between ray and normal is between pi/2 and 3pi/2,)
                #    ?and if at least one point within distance cutoff?:
                this_intersection = ray_intersects(ray, triangle, normal)
                if this_intersection[2] < closest_distance:
                    nearest_intersection = this_intersection
                        #NOTE: should be stored as a point in space, its face normal, distance to origin.
        return (nearest_intersection)


    #ray_intersects: returns point as (point, normal, distance to origin).
    def ray_intersects(self, ray, triangle, normal):
        # check if ray and plane are parallel
        # compute distance from origin to point being checked
        # compute distance from origin to plane(parallel to plane's normal)
        # check if triangle is behind the ray
        # compute intersection point using distances calculated prev.
        # inside-outside test with polygon's edges.    
        return self.max_rendering_depth

    def primary_ray(self, x, y) :
        #return vector representing ray through center of pixel (x,y)?
        pass

    def shadow_ray(self, pointA, pointB):
        pass

    # row-major ordered. X, Y, Z, Translation
    # defaults to identity matrix (no change)
    # thank you to songho.ca/opengl/gl_camera for help understanding camera transformation matrices.
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

