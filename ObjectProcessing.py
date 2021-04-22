import array



def parse_into_objects(file='') :
    f = open(file)
    objects = []
    object_start_lines = array.array('i')
    verts = {}
    vertex_count = 0
    i = 0
    for line in f.readlines():
        i+=1
        if line.startswith('o '):
            object_start_lines.append(i)
        if line.startswith("v "):
            vertex_count += 1
            x, y, z = line[1:-1].split()
            xyz = array.array('f')
            xyz.append(float(x))
            xyz.append(float(y))
            xyz.append(float(z))
            verts[vertex_count] = xyz 
    for i in object_start_lines:
        objects.append(create_object(file, i, verts))
    return objects



def create_object(file, line, vertices):
    f = open(file)
    faces = []
    line_count = 0
    for line in f.readlines()[line:]:
        if line.startswith("f "):
            line_faces = []
            for item in line.split(' ')[1:]:
                line_faces.append(vertices[int(item.split('/')[0])])
            faces.append(line_faces)
        # if line.startswith("o "):
            #  break
    return faces



 