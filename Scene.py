# a collection of objects and their positions/rotations.
#NOTE: WORLDSPACE IS RIGHT-HANDED (facing negative Z), and vertices are COUNTERCLOCKWISE
class Scene:
    meshes = []
    
    def insert_object(self, mesh, origin):
        x, y, z = origin
        for triangle in range(len(mesh.faces)):
            for vertex in range(len(mesh.faces[triangle])):
                mesh.faces[triangle][vertex] = (
                    mesh.faces[triangle][vertex][0] + x,
                    mesh.faces[triangle][vertex][1] + y,
                    mesh.faces[triangle][vertex][2] + z)
                
        self.meshes.append(mesh)