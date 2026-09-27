from __future__ import annotations

import uuid
from datetime import date, datetime, timezone
from typing import TYPE_CHECKING

from models.enums import Gender, StudentStatus

if TYPE_CHECKING:
    from models.program import Program


class Student:
    def __init__(
        self,
        student_no: str,
        national_id: str,
        first_name: str,
        last_name: str,
        birth_date: date,
        gender: Gender,
        email: str,
        phone: str,
        address: str,
        program: Program,
        enrollment_year: int,
        class_year: int,
        status: StudentStatus = StudentStatus.ACTIVE,
        photo_url: str | None = None,
        created_at: datetime | None = None,
        id: uuid.UUID | None = None,
    ) -> None:
        self._id = id or uuid.uuid4()
        self._student_no = student_no
        self._national_id = national_id
        self._first_name = first_name
        self._last_name = last_name
        self._birth_date = birth_date
        self._gender = gender
        self._email = email
        self._phone = phone
        self._address = address
        self._program = program
        self._enrollment_year = enrollment_year
        self._class_year = class_year
        self._status = status
        self._photo_url = photo_url
        self._created_at = created_at or datetime.now(timezone.utc)

    @property
    def id(self) -> uuid.UUID:
        return self._id

    @id.setter
    def id(self, value: uuid.UUID) -> None:
        self._id = value

    @property
    def student_no(self) -> str:
        return self._student_no

    @student_no.setter
    def student_no(self, value: str) -> None:
        self._student_no = value

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
    def birth_date(self) -> date:
        return self._birth_date

    @birth_date.setter
    def birth_date(self, value: date) -> None:
        self._birth_date = value

    @property
    def gender(self) -> Gender:
        return self._gender

    @gender.setter
    def gender(self, value: Gender) -> None:
        self._gender = value

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, value: str) -> None:
        self._email = value

    @property
    def phone(self) -> str:
        return self._phone

    @phone.setter
    def phone(self, value: str) -> None:
        self._phone = value

    @property
    def address(self) -> str:
        return self._address

    @address.setter
    def address(self, value: str) -> None:
        self._address = value

    @property
    def program(self) -> Program:
        return self._program

    @program.setter
    def program(self, value: Program) -> None:
        self._program = value

    @property
    def enrollment_year(self) -> int:
        return self._enrollment_year

    @enrollment_year.setter
    def enrollment_year(self, value: int) -> None:
        self._enrollment_year = value

    @property
    def class_year(self) -> int:
        return self._class_year

    @class_year.setter
    def class_year(self, value: int) -> None:
        self._class_year = value

    @property
    def status(self) -> StudentStatus:
        return self._status

    @status.setter
    def status(self, value: StudentStatus) -> None:
        self._status = value

    @property
    def photo_url(self) -> str | None:
        return self._photo_url

    @photo_url.setter
    def photo_url(self, value: str | None) -> None:
        self._photo_url = value

    @property
    def created_at(self) -> datetime:
        return self._created_at

    @created_at.setter
    def created_at(self, value: datetime) -> None:
        self._created_at = value

    def __str__(self) -> str:
        return (
            f"Student(id={self._id}, student_no={self._student_no}, "
            f"national_id={self._national_id}, first_name={self._first_name}, "
            f"last_name={self._last_name}, birth_date={self._birth_date}, "
            f"gender={self._gender.value}, email={self._email}, "
            f"phone={self._phone}, address={self._address}, "
            f"program={self._program.name}, "
            f"enrollment_year={self._enrollment_year}, "
            f"class_year={self._class_year}, status={self._status.value}, "
            f"photo_url={self._photo_url or '-'}, created_at={self._created_at})"
        )
