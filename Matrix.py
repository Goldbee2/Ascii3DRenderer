import math

class Matrix:

    @staticmethod
    def subtract(vector_1, vector_2):
        v1x, v1y, v1z = vector_1
        v2x, v2y, v2z = vector_2
        return(v1x-v2x, v1y-v2y, v1z-v2z)



    @staticmethod
    def scale(vector, scalar):
        return(vector[0]*scalar, vector[1]*scalar, vector[2]*scalar)



    @staticmethod
    def normalize(vector):
        x, y, z = vector
        magnitude = Matrix.magnitude(vector)
        if(magnitude == 0):
            return(0, 0, 0)
        return (x/magnitude, y/magnitude, z/magnitude)



    @staticmethod
    def dot_product(vector_1, vector_2):
        v1x, v1y, v1z = vector_1
        v2x, v2y, v2z = vector_2
        product = (v1x * v2x +
                   v1y * v2y +
                   v1z * v2z)
        return product



    @staticmethod
    def cross_product(vector_1, vector_2):
        v1x, v1y, v1z = vector_1
        v2x, v2y, v2z = vector_2
        product_x = (v1y*v2z - v1z*v2y)
        product_y = (v1z*v2x - v2z*v2x)
        product_z = (v1x*v2y - v1y*v2x)

        return (product_x, product_y, product_z)

    @staticmethod
    def magnitude(vector):
        x, y, z = vector
        return math.sqrt(x**2 + y**2 + z**2)