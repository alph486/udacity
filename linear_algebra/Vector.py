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
        return sum

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

    # Returns self's projection onto basis vector b
    def component_parallel_to(self, b):
        ub = b.get_unit_vector()
        return ub.scalar_multiply(self.dotproduct(ub))

    # Returns the orthogonal component of self with respect to basis vector b
    def component_orthogonal_to(self, b):
        # Get the parallel component of v with respect to b.
        vp = self.component_parallel_to(b)
        return self.subtract(vp)

if __name__ == "__main__":
    v1 = Vector([3.039, 1.879])
    v2 = Vector([0.825, 2.036])

    v3 = Vector([-9.88, -3.264, -8.159])
    v4 = Vector([-2.155, -9.353, -9.473])

    v5 = Vector([3.009, -6.172, 3.692, -2.51])
    v6 = Vector([6.404, -9.144, 2.759, 8.718])

    print(v1.component_parallel_to(v2))

    print(v3.component_orthogonal_to(v4))

    print(v5.component_parallel_to(v6))
    print(v5.component_orthogonal_to(v6))