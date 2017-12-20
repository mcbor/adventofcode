"""
    vector.py
    ~~~~~~~~~
    N-dimensional vector

    :copyright: (c) 2017 by Martin Bor.
    :license: MIT, see LICENSE for more details.
"""

import math


class Vector(tuple):
    def __new__(cls, *components):
        """Create new n-dimensional vector.

        >>> Vector(1)
        (1)
        >>> Vector(1, 2, 3)
        (1, 2, 3)
        """
        return tuple.__new__(cls, components)

    def left(self):
        """Rotate a 2D vector 90 degrees anticlockwise.

        >>> Vector(0, 1).left()
        (-1, 0)
        >>> Vector(-1, 0).left()
        (0, -1)
        >>> Vector(2, 3).left()
        (-3, 2)
        """
        assert len(self) == 2
        return Vector(-self[1], self[0])

    def right(self):
        """Rotate a 2D vector 90 degress clockwise

        >>> Vector(0, 1).right()
        (1, 0)
        >>> Vector(1, 0).right()
        (0, -1)
        >>> Vector(2, 3).right()
        (3, -2)
        """
        assert len(self) == 2
        return Vector(self[1], -self[0])

    def __add__(self, other):
        """Add two vectors, having the same dimension.

        >>> a = Vector(1, 2)
        >>> b = Vector(2, 3)
        >>> a + b
        (3, 5)
        """
        assert isinstance(other, Vector)
        assert len(self) == len(other)
        return Vector(*[a + b for a, b in zip(self, other)])

    def __abs__(self):
        """Length of the vector.

        >>> abs(Vector(0, 0))
        0.0
        >>> abs(Vector(10, 0))
        10.0
        >>> abs(Vector(0, -12))
        12.0
        """
        return math.sqrt(sum(a**2 for a in self))

    def __mul__(self, other):
        """Dot product if other is a vector, scalar multiplication if other
        is a scalar.

        >>> a = Vector(1, 2)
        >>> b = Vector(2, 3)
        >>> a * b
        8
        >>> a * 3
        (3, 6)
        >>> 3 * b
        (6, 9)
        """
        if isinstance(other, Vector):
            assert len(self) == len(other)
            return sum(a * b for a, b in zip(self, other))
        return Vector(*[a * other for a in self])

    def __rmul__(self, other):
        # other should be a scalar
        return self * other

    def __sub__(self, other):
        assert isinstance(other, Vector)
        return Vector(*[a - b for a, b in zip(self, other)])

    def __getattr__(self, attr):
        """Convenience method to get vector coords by name (up to 6 dimensions)

        >>> a = Vector(1, 2, 3)
        >>> a.x
        1
        >>> a.y
        2
        >>> a.z
        3
        """
        assert 0 < len(self) < 7
        if attr in 'xyzuvw':
            return self['xyzuvw'.index(attr)]
        else:
            raise AttributeError(f"Vector has no attribute '{attr}'")

    def __repr__(self):
        return "(" + ", ".join(str(a) for a in self) + ")"
