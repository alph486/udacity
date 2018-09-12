#Vectors

Vectors represent a displacement from an origin point. They are different from a "point" in n-dimensional space in that they do not represent a /location/ in space, but represent a /displacement/ from one point to another. In this way, vectors have a direction and magnitude, as they say.

http://geomalgorithms.com/points_and_vectors.html

## Operations

### Scalar Multiplication

### Addition and Subtraction

## Dot Product (Inner Product)

## Parallel and Orthogonal Vectors

## Vector Projections

```
v = v" + vT
v" = projv(b) = (v*ub)ub
```

## Cross Products

> Given two linearly independent vectors `a` and `b`, the cross product, `a x b` is a vector that is perpendicular (Orthogonal) to both `a` and `b` and thus normal to the plane containing them...It should not be confused with dot product (projection product).

```
Given:
v = [x1, y1, z1]
w = [x2, y2, z2]
v x w = [y1z2 - y2z1, -(x1z2 - x2z1), x1y2 - x2y1]
```

* Cross Products work with 3d vectors. There is not a higher dimensional generalization.

# Intersections

Intersections are important when seeking to find the relationship between two functions that produce a line.

Line in n dimensional space can be represented as: `x(t) = x0 + t*v` where `x0` is the basepoint (vector) and `v` is a direction vector (a second point to show displacement).

This can also be written as `Ax + By = k`.

```
What is the difference between a point and a vector? They both are n-dimensional coordinates.

A: A vector can be considered a _transition_ of a point; it has magnitude and direction. Therefore, you must consider a vector in relation to another point in space, like the origin or other coordinates.
```

## Intersetions of Lines in 2D

Two parallel lines are *equal (coincident)* if-and-only-if the vector connecting one point on each line is orthogonal to the lines' normal vectors. In this case they intersect at every possible point.

The intersection of two non-parallel lines can be defined as:

```
x = Dk1 - Bk2 / AD-BC
y = -Ck1 + Ak2 / AD-BC
```
