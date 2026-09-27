from __future__ import annotations

import uuid
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.faculty import Faculty
    from models.instructor import Instructor


class Department:
    def __init__(
        self,
        code: str,
        name: str,
        faculty: Faculty,
        phone: str,
        email: str,
        head_instructor: Instructor | None = None,
        is_active: bool = True,
        id: uuid.UUID | None = None,
    ) -> None:
        self._id = id or uuid.uuid4()
        self._code = code
        self._name = name
        self._faculty = faculty
        self._head_instructor = head_instructor
        self._phone = phone
        self._email = email
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
    def faculty(self) -> Faculty:
        return self._faculty

    @faculty.setter
    def faculty(self, value: Faculty) -> None:
        self._faculty = value

    @property
    def head_instructor(self) -> Instructor | None:
        return self._head_instructor

    @head_instructor.setter
    def head_instructor(self, value: Instructor | None) -> None:
        self._head_instructor = value

    @property
    def phone(self) -> str:
        return self._phone

    @phone.setter
    def phone(self, value: str) -> None:
        self._phone = value

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, value: str) -> None:
        self._email = value

    @property
    def is_active(self) -> bool:
        return self._is_active

    @is_active.setter
    def is_active(self, value: bool) -> None:
        self._is_active = value

    def __str__(self) -> str:
        head_name = (
            f"{self._head_instructor.first_name} {self._head_instructor.last_name}"
            if self._head_instructor
            else "-"
        )
        return (
            f"Department(id={self._id}, code={self._code}, name={self._name}, "
            f"faculty={self._faculty.name}, head_instructor={head_name}, "
            f"phone={self._phone}, email={self._email}, is_active={self._is_active})"
        )
