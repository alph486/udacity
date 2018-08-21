import math

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

    def magnitude(self):
        m = 0
        for x in self.coordinates: #Could have used list comprehension and ** operator.
            m += math.pow(x, 2) # Could have used math sum() function here.
        return math.sqrt(m)

    def get_unit_vector(self):
        try:
            m = 1 / self.magnitude()
            return self.scalar_multiply(m)
        except ZeroDivisionError:
            raise Exception('Cannot normalize the zero Vector.')

    def dotproduct(self, v):
        if v.dimension != self.dimension:
            raise Exception("Vectors must be the same dimensionality")
        sum = 0
        for k, i in enumerate(self.coordinates):
            sum += i * v.coordinates[k]
        return sum

    def angle_between_rads(self, v):
        dp = self.dotproduct(v)
        m1 = self.magnitude()
        m2 = v.magnitude()
        return math.acos(dp/(m1*m2))

    def angle_between_degrees(self, v):
        return math.degrees(self.angle_between_rads(v))


if __name__ == "__main__":
    v1 = Vector([7.887, 4.138])
    v2 = Vector([-8.802, 6.776])
    v3 = Vector([-5.955, -4.904, -1.874])
    v4 = Vector([-4.496, -8.755, 7.103])
    v5 = Vector([3.183, -7.627])
    v6 = Vector([-2.668, 5.319])
    v7 = Vector([7.35, 0.221, 5.188])
    v8 = Vector([2.751, 8.259, 3.985])
    print(v1.dotproduct(v2))
    print(v3.dotproduct(v4))
    print(v5.angle_between_rads(v6))
    print(v7.angle_between_degrees(v8))
