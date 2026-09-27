from __future__ import annotations

import uuid
from typing import TYPE_CHECKING

from models.enums import CourseType

if TYPE_CHECKING:
    from models.department import Department


class Course:
    def __init__(
        self,
        code: str,
        name: str,
        department: Department,
        credits: int,
        theory_hours: int,
        lab_hours: int,
        course_type: CourseType,
        language: str,
        description: str,
        is_active: bool = True,
        id: uuid.UUID | None = None,
    ) -> None:
        self._id = id or uuid.uuid4()
        self._code = code
        self._name = name
        self._department = department
        self._credits = credits
        self._theory_hours = theory_hours
        self._lab_hours = lab_hours
        self._course_type = course_type
        self._language = language
        self._description = description
        self._is_active = is_active

    @property
    def id(self) -> uuid.UUID:
        return self._id

    @id.setter
    def id(self, value: uuid.UUID) -> None:
        self._id = value

    @property
    def code(self) -> str:
        return self._code

    @code.setter
    def code(self, value: str) -> None:
        self._code = value

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    @property
    def department(self) -> Department:
        return self._department

    @department.setter
    def department(self, value: Department) -> None:
        self._department = value

    @property
    def credits(self) -> int:
        return self._credits

    @credits.setter
    def credits(self, value: int) -> None:
        self._credits = value

    @property
    def theory_hours(self) -> int:
        return self._theory_hours

    @theory_hours.setter
    def theory_hours(self, value: int) -> None:
        self._theory_hours = value

    @property
    def lab_hours(self) -> int:
        return self._lab_hours

    @lab_hours.setter
    def lab_hours(self, value: int) -> None:
        self._lab_hours = value

    @property
    def course_type(self) -> CourseType:
        return self._course_type

    @course_type.setter
    def course_type(self, value: CourseType) -> None:
        self._course_type = value

    @property
    def language(self) -> str:
        return self._language

    @language.setter
    def language(self, value: str) -> None:
        self._language = value

    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, value: str) -> None:
        self._description = value

    @property
    def is_active(self) -> bool:
        return self._is_active

    @is_active.setter
    def is_active(self, value: bool) -> None:
        self._is_active = value

    def __str__(self) -> str:
        return (
            f"Course(id={self._id}, code={self._code}, name={self._name}, "
            f"department={self._department.name}, credits={self._credits}, "
            f"theory_hours={self._theory_hours}, lab_hours={self._lab_hours}, "
            f"course_type={self._course_type.value}, language={self._language}, "
            f"description={self._description}, is_active={self._is_active})"
        )
