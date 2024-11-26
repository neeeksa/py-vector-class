import math
from typing import Any


class Vector:
    def __init__(self, x_co: float, y_co: float) -> None:
        self.x = round(x_co, 2)
        self.y = round(y_co, 2)

    def __add__(self, other: Any) -> "Vector":
        return Vector(round(self.x + other.x, 2), round(self.y + other.y, 2))

    def __sub__(self, other: Any) -> "Vector":
        return Vector(round(self.x - other.x, 2), round(self.y - other.y, 2))

    def __mul__(self, other: Any) -> "Vector":
        if isinstance(other, (int, float)):
            return Vector(round(self.x * other, 2), round(self.y * other, 2))
        else:
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: Any, end_point: Any) -> Any:
        x_coordinates = round(end_point[0] - start_point[0], 2)
        y_coordinates = round(end_point[1] - start_point[1], 2)
        return cls(x_coordinates, y_coordinates)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Any:
        length = self.get_length()
        return Vector(round(self.x / length, 2), round(self.y / length, 2))

    def angle_between(self, second_vector: Any) -> float:
        scalar = (self.x * second_vector.x) + (self.y * second_vector.y)
        vector_1 = self.get_length()
        vector_2 = second_vector.get_length()
        cos_a = max(-1, min(1, scalar / (vector_1 * vector_2)))
        return math.ceil(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        v_constant = self.get_length()
        cos_a = self.y / v_constant
        return int(math.degrees(math.acos(cos_a)))

    def rotate(self, degrees: int) -> "Vector":
        angle_radians = math.radians(degrees)
        x2 = round(self.x * math.cos(angle_radians)
                   - self.y * math.sin(angle_radians), 2)
        y2 = round(self.x * math.sin(angle_radians)
                   + self.y * math.cos(angle_radians), 2)
        return Vector(x2, y2)
