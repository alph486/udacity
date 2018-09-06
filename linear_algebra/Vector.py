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

    def cross_product(self, w):
        if self.dimension != 3 or w.dimension != 3:
            raise ValueError("Vectors must be 3 dimensional.")
        v_coords = self.coordinates
        w_coords = w.coordinates
        x = (v_coords[1]*w_coords[2] - w_coords[1]*v_coords[2])
        y = -(v_coords[0]*w_coords[2] - w_coords[0]*v_coords[2])
        z = (v_coords[0]*w_coords[1] - w_coords[0]*v_coords[1])
        return Vector([x, y, z])

    def area_parallelogram(self, w):
        c = self.cross_product(w)
        return c.magnitude()

    def area_triangle(self, w):
        return self.area_parallelogram(w) / 2


if __name__ == "__main__":
    v1 = Vector([8.462, 7.893, -8.187])
    v2 = Vector([6.984, -5.975, 4.778])

    v3 = Vector([-8.987, -9.838, 5.031])
    v4 = Vector([-4.268, -1.861, -8.866])

    v5 = Vector([1.5, 9.547, 3.691])
    v6 = Vector([-6.007, 0.124, 5.772])

    print(v1.cross_product(v2))
    print(v3.area_parallelogram(v4))
    print(v5.area_triangle(v6))