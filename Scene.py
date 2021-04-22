# a collection of objects and their positions/rotations.
#NOTE: WORLDSPACE IS RIGHT-HANDED (facing negative Z), and vertices are COUNTERCLOCKWISE
class Scene:
    meshes = []
    
    def insert_object(self, mesh, origin):
        x, y, z = origin
        for triangle in mesh.faces:
            for vertex in triangle:
                vertex[0] += x
                vertex[1] += y
                vertex[2] += z
        self.meshes.append(mesh)