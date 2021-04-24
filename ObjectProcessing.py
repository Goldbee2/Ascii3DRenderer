import array

class Mesh:
    faces = []
    bounding_box = [0, 0, 0]
    
    
    def scale_mesh(self, scale):
        for face in self.faces:
            for vertex in face:
                for i in range(len(vertex)):
                    vertex[i] *= scale
        self.create_bounding_box()



    def translate_mesh(self, translation):
        for i in range(len(self.faces)):
            for j in range(len(self.faces[i])):
                self.faces[i][j] = (
                self.faces[i][j][0] + translation[0],
                self.faces[i][j][1] + translation[1],
                self.faces[i][j][2] + translation[2])
        self.create_bounding_box()


    def create_bounding_box(self):
        x_max = 0.0
        y_max = 0.0
        z_max = 0.0

        x_min = 0.0
        y_min = 0.0
        z_min = 0.0

        for face in self.faces:
            for vertex in face:
                if vertex[0] > x_max:
                    x_max = vertex[0]
                if vertex[1] > y_max:
                    y_max = vertex[1]
                if vertex[2] > z_max:
                    z_max = vertex[2]
                if vertex[0] < x_min:
                    x_min = vertex[0]
                if vertex[1] < y_min:
                    y_min = vertex[1]
                if vertex[2] < z_min:
                    z_min = vertex[2]

        max_coords = (x_max, y_max, z_max)
        min_coords = (x_min, y_min, z_min)
        self.bounding_box = (max_coords, min_coords)



def parse_into_meshes(file='') :
    f = open(file)
    meshes = []
    mesh_start_lines = array.array('i')
    verts = {}
    vertex_count = 0
    i = 0
    for line in f.readlines():
        i+=1
        if line.startswith('o '):
            mesh_start_lines.append(i)
        if line.startswith("v "):
            vertex_count += 1
            x, y, z = line[1:-1].split()
            xyz = array.array('f')
            xyz.append(float(x))
            xyz.append(float(y))
            xyz.append(float(z))
            verts[vertex_count] = xyz 
    for i in mesh_start_lines:
        meshes.append(create_mesh(file, i, verts))
    return meshes



def create_mesh(file, line, vertices):
    new_mesh = Mesh()
    f = open(file)
    faces = []
    line_count = 0
    for line in f.readlines()[line:]:
        if line.startswith("f "):
            line_faces = []
            for item in line.split(' ')[1:-1]:
                line_faces.append(vertices[int(item.split('/')[0])])
            faces.append(line_faces)
        if line.startswith("o "):
             break
    
    new_mesh.faces = faces
    new_mesh.create_bounding_box()
    
    return new_mesh

