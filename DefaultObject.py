from ObjectProcessing import Mesh

class UnitSquare(Mesh) :
    def __init__(self):
        self.faces = [
            [[-1, -1, 0], [1, -1, 0], [-1, 1, 0]],
            [[-1,  1, 0], [1, -1, 0], [ 1, 1, 0]]]


class UnitTriangle(Mesh):
    def __init__(self):
        self.faces = [
            [[-1, -1, 0], [1, -1, 0], [-1, 1, 0]]]
