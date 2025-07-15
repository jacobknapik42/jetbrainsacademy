from enum import Enum


class Courses(Enum):
    PYTHON = ("Python", 600, 0)
    DSA = ("DSA", 400, 1)
    DATABASES = ("Databases", 480, 2)
    FLASK = ("Flask", 550, 3)

    def __init__(self, label, required_points, index):
        self.label = label
        self.required_points = required_points
        self.index = index