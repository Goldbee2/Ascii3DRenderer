# a collection of objects and their positions/rotations.
#NOTE: WORLDSPACE IS RIGHT-HANDED (facing negative Z), and vertices are COUNTERCLOCKWISE
class Scene:
    objects = []
    
    def insert_object(self, object, origin):
        x, y, z = origin
        for triangle in object:
            for vertex in triangle:
                vertex[0] += x
                vertex[1] += y
                vertex[2] += z
        self.objects.append(object)