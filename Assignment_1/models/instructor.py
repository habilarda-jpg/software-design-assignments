from __future__ import annotations

import uuid
from datetime import date
from typing import TYPE_CHECKING

from models.enums import InstructorTitle

if TYPE_CHECKING:
    from models.department import Department


class Instructor:
    def __init__(
        self,
        employee_no: str,
        national_id: str,
        first_name: str,
        last_name: str,
        email: str,
        department: Department,
        title: InstructorTitle,
        specialization: str,
        hire_date: date,
        is_active: bool = True,
        id: uuid.UUID | None = None,
    ) -> None:
        self._id = id or uuid.uuid4()
        self._employee_no = employee_no
        self._national_id = national_id
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._department = department
        self._title = title
        self._specialization = specialization
        self._hire_date = hire_date
        self._is_active = is_active

    @property
    def id(self) -> uuid.UUID:
        return self._id

    @id.setter
    def id(self, value: uuid.UUID) -> None:
        self._id = value

    @property
    def employee_no(self) -> str:
        return self._employee_no

    @employee_no.setter
    def employee_no(self, value: str) -> None:
        self._employee_no = value

    @property
    def national_id(self) -> str:
        return self._national_id

    @national_id.setter
    def national_id(self, value: str) -> None:
        self._national_id = value

    @property
    def first_name(self) -> str:
        return self._first_name

    @first_name.setter
    def first_name(self, value: str) -> None:
        self._first_name = value

    @property
    def last_name(self) -> str:
        return self._last_name

    @last_name.setter
    def last_name(self, value: str) -> None:
        self._last_name = value

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, value: str) -> None:
        self._email = value

    @property
    def department(self) -> Department:
        return self._department

    @department.setter
    def department(self, value: Department) -> None:
        self._department = value

    @property
    def title(self) -> InstructorTitle:
        return self._title

    @title.setter
    def title(self, value: InstructorTitle) -> None:
        self._title = value

    @property
    def specialization(self) -> str:
        return self._specialization

    @specialization.setter
    def specialization(self, value: str) -> None:
        self._specialization = value

    @property
    def hire_date(self) -> date:
        return self._hire_date

    @hire_date.setter
    def hire_date(self, value: date) -> None:
        self._hire_date = value

    @property
    def is_active(self) -> bool:
        return self._is_active

    @is_active.setter
    def is_active(self, value: bool) -> None:
        self._is_active = value

    def __str__(self) -> str:
        return (
            f"Instructor(id={self._id}, employee_no={self._employee_no}, "
            f"national_id={self._national_id}, first_name={self._first_name}, "
            f"last_name={self._last_name}, email={self._email}, "
            f"department={self._department.name}, title={self._title.value}, "
            f"specialization={self._specialization}, "
            f"hire_date={self._hire_date}, is_active={self._is_active})"
        )
