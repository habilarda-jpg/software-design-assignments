from __future__ import annotations

import uuid
from typing import TYPE_CHECKING

from models.enums import ProgramCourseType

if TYPE_CHECKING:
    from models.course import Course
    from models.program import Program


class ProgramCourse:
    def __init__(
        self,
        program: Program,
        course: Course,
        semester_order: int,
        course_type: ProgramCourseType,
        is_active: bool = True,
        id: uuid.UUID | None = None,
    ) -> None:
        self._id = id or uuid.uuid4()
        self._program = program
        self._course = course
        self._semester_order = semester_order
        self._course_type = course_type
        self._is_active = is_active

    @property
    def id(self) -> uuid.UUID:
        return self._id

    @id.setter
    def id(self, value: uuid.UUID) -> None:
        self._id = value

    @property
    def program(self) -> Program:
        return self._program

    @program.setter
    def program(self, value: Program) -> None:
        self._program = value

    @property
    def course(self) -> Course:
        return self._course

    @course.setter
    def course(self, value: Course) -> None:
        self._course = value

    @property
    def semester_order(self) -> int:
        return self._semester_order

    @semester_order.setter
    def semester_order(self, value: int) -> None:
        self._semester_order = value

    @property
    def course_type(self) -> ProgramCourseType:
        return self._course_type

    @course_type.setter
    def course_type(self, value: ProgramCourseType) -> None:
        self._course_type = value

    @property
    def is_active(self) -> bool:
        return self._is_active

    @is_active.setter
    def is_active(self, value: bool) -> None:
        self._is_active = value

    def __str__(self) -> str:
        return (
            f"ProgramCourse(id={self._id}, program={self._program.code}, "
            f"course={self._course.code}, semester_order={self._semester_order}, "
            f"course_type={self._course_type.value}, is_active={self._is_active})"
        )
