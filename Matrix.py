class Matrix:

    @staticmethod
    def subtract(vector_1, vector_2):
        v1x, v1y, v1z = vector_1
        v2x, v2y, v2z = vector_2
        
        return(v1x-v2x, v1y-v2y, v1z-v2z)

    @staticmethod
    def dot_product(vector_1, vector_2):
        v1x, v1y, v1z = vector_1
        v2x, v2y, v2z = vector_2
        product = (v1x * v2x +
                   v1y * v2y +
                   v1z * v2z)
        return product