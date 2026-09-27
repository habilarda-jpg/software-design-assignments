from __future__ import annotations

import uuid
from typing import TYPE_CHECKING

from models.enums import PrerequisiteType

if TYPE_CHECKING:
    from models.course import Course


class CoursePrerequisite:
    def __init__(
        self,
        course: Course,
        prerequisite_course: Course,
        type: PrerequisiteType,
        min_grade: str,
        id: uuid.UUID | None = None,
    ) -> None:
        self._id = id or uuid.uuid4()
        self._course = course
        self._prerequisite_course = prerequisite_course
        self._type = type
        self._min_grade = min_grade

    @property
    def id(self) -> uuid.UUID:
        return self._id

    @id.setter
    def id(self, value: uuid.UUID) -> None:
        self._id = value

    @property
    def course(self) -> Course:
        return self._course

    @course.setter
    def course(self, value: Course) -> None:
        self._course = value

    @property
    def prerequisite_course(self) -> Course:
        return self._prerequisite_course

    @prerequisite_course.setter
    def prerequisite_course(self, value: Course) -> None:
        self._prerequisite_course = value

    @property
    def type(self) -> PrerequisiteType:
        return self._type

    @type.setter
    def type(self, value: PrerequisiteType) -> None:
        self._type = value

    @property
    def min_grade(self) -> str:
        return self._min_grade

    @min_grade.setter
    def min_grade(self, value: str) -> None:
        self._min_grade = value

    def __str__(self) -> str:
        return (
            f"CoursePrerequisite(id={self._id}, course={self._course.code}, "
            f"prerequisite_course={self._prerequisite_course.code}, "
            f"type={self._type.value}, min_grade={self._min_grade})"
        )
