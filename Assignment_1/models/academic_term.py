from __future__ import annotations

import uuid
from datetime import date

from models.enums import Semester


class AcademicTerm:
    def __init__(
        self,
        code: str,
        name: str,
        academic_year: str,
        semester: Semester,
        start_date: date,
        end_date: date,
        registration_start: date,
        registration_end: date,
        add_drop_end: date,
        is_active: bool = True,
        id: uuid.UUID | None = None,
    ) -> None:
        self._id = id or uuid.uuid4()
        self._code = code
        self._name = name
        self._academic_year = academic_year
        self._semester = semester
        self._start_date = start_date
        self._end_date = end_date
        self._registration_start = registration_start
        self._registration_end = registration_end
        self._add_drop_end = add_drop_end
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
    def academic_year(self) -> str:
        return self._academic_year

    @academic_year.setter
    def academic_year(self, value: str) -> None:
        self._academic_year = value

    @property
    def semester(self) -> Semester:
        return self._semester

    @semester.setter
    def semester(self, value: Semester) -> None:
        self._semester = value

    @property
    def start_date(self) -> date:
        return self._start_date

    @start_date.setter
    def start_date(self, value: date) -> None:
        self._start_date = value

    @property
    def end_date(self) -> date:
        return self._end_date

    @end_date.setter
    def end_date(self, value: date) -> None:
        self._end_date = value

    @property
    def registration_start(self) -> date:
        return self._registration_start

    @registration_start.setter
    def registration_start(self, value: date) -> None:
        self._registration_start = value

    @property
    def registration_end(self) -> date:
        return self._registration_end

    @registration_end.setter
    def registration_end(self, value: date) -> None:
        self._registration_end = value

    @property
    def add_drop_end(self) -> date:
        return self._add_drop_end

    @add_drop_end.setter
    def add_drop_end(self, value: date) -> None:
        self._add_drop_end = value

    @property
    def is_active(self) -> bool:
        return self._is_active

    @is_active.setter
    def is_active(self, value: bool) -> None:
        self._is_active = value

    def __str__(self) -> str:
        return (
            f"AcademicTerm(id={self._id}, code={self._code}, name={self._name}, "
            f"academic_year={self._academic_year}, "
            f"semester={self._semester.value}, "
            f"start_date={self._start_date}, end_date={self._end_date}, "
            f"registration_start={self._registration_start}, "
            f"registration_end={self._registration_end}, "
            f"add_drop_end={self._add_drop_end}, is_active={self._is_active})"
        )
