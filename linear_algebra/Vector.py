
class Vector:

    def __init__(self, coordinates):
        if not coordinates:
            raise ValueError("coordinates cannot be empty")
        self.coordinates = tuple(coordinates)
        self.dimension = len(coordinates)

    def __str__(self):
        return "Vector: {0}".format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def add(self, v):
        if v.dimension != self.dimension:
            raise RuntimeError('Vectors must have same dimensionality.')
        result = []
        for t in enumerate(self.coordinates):
            result.append(t[1] + v.coordinates[t[0]])
        return Vector(result)

    def scalar_multiply(self, s):
        result = []
        for x in self.coordinates:
            result.append(s*x)
        return Vector(result)

    def subtract(self, v):
        return self.add(v.scalar_multiply(-1))
