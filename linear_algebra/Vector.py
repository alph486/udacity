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
            raise ZeroDivisionError('Cannot normalize the zero Vector.')

    def dotproduct(self, v):
        if v.dimension != self.dimension:
            raise Exception("Vectors must be the same dimensionality")
        sum = 0
        for k, i in enumerate(self.coordinates):
            sum += i * v.coordinates[k]
        return round(sum, 3)

    def angle_between_rads(self, v):
        dp = self.dotproduct(v)
        m1 = self.magnitude()
        m2 = v.magnitude()
        return math.acos(dp/(m1*m2))

    def angle_between_degrees(self, v):
        return math.degrees(self.angle_between_rads(v))

    def is_parallel_to(self, v):
        try:
            u1 = [round(abs(x), 3) for x in self.get_unit_vector().coordinates]
            u2 = [round(abs(x), 3) for x in v.get_unit_vector().coordinates]
        except ZeroDivisionError:
            return True
        return Vector(u1) == Vector(u2)

    def is_orthogonal_to(self, v):
        return self.dotproduct(v) == 0

if __name__ == "__main__":
    v1 = Vector([-7.579, -7.88])
    v2 = Vector([22.737, 23.64])

    v3 = Vector([-2.029, 9.97, 4.172])
    v4 = Vector([-9.231, -6.639, -7.245])

    v5 = Vector([-2.328, -7.284, -1.214])
    v6 = Vector([-1.821, 1.072, -2.94])

    v7 = Vector([2.118, 4.827])
    v8 = Vector([0, 0])

    print(v1.is_parallel_to(v2))
    print(v1.is_orthogonal_to(v2))

    print(v3.is_parallel_to(v4))
    print(v3.is_orthogonal_to(v4))

    print(v5.is_parallel_to(v6))
    print(v5.is_orthogonal_to(v6))

    print(v7.is_parallel_to(v8))
    print(v7.is_orthogonal_to(v8))
