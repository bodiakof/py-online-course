from typing import Type
import math


class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        return math.ceil(days / 7)

    @classmethod
    def from_dict(cls: Type["OnlineCourse"],
                  course_dict: dict) -> "OnlineCourse":
        cls.name = course_dict["name"]
        cls.description = course_dict["description"]
        cls.weeks = course_dict["days"]

        cls.weeks = cls.days_to_weeks(cls.weeks)

        return cls(cls.name, cls.description, cls.weeks)
