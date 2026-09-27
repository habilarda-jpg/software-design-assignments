from __future__ import annotations

import uuid
from typing import TYPE_CHECKING

from models.enums import DegreeLevel

if TYPE_CHECKING:
    from models.department import Department


class Program:
    def __init__(
        self,
        code: str,
        name: str,
        department: Department,
        degree_level: DegreeLevel,
        total_credits: int,
        duration_years: int,
        language: str,
        is_active: bool = True,
        id: uuid.UUID | None = None,
    ) -> None:
        self._id = id or uuid.uuid4()
        self._code = code
        self._name = name
        self._department = department
        self._degree_level = degree_level
        self._total_credits = total_credits
        self._duration_years = duration_years
        self._language = language
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
    def degree_level(self) -> DegreeLevel:
        return self._degree_level

    @degree_level.setter
    def degree_level(self, value: DegreeLevel) -> None:
        self._degree_level = value

    @property
    def total_credits(self) -> int:
        return self._total_credits

    @total_credits.setter
    def total_credits(self, value: int) -> None:
        self._total_credits = value

    @property
    def duration_years(self) -> int:
        return self._duration_years

    @duration_years.setter
    def duration_years(self, value: int) -> None:
        self._duration_years = value

    @property
    def language(self) -> str:
        return self._language

    @language.setter
    def language(self, value: str) -> None:
        self._language = value

    @property
    def is_active(self) -> bool:
        return self._is_active

    @is_active.setter
    def is_active(self, value: bool) -> None:
        self._is_active = value

    def __str__(self) -> str:
        return (
            f"Program(id={self._id}, code={self._code}, name={self._name}, "
            f"department={self._department.name}, "
            f"degree_level={self._degree_level.value}, "
            f"total_credits={self._total_credits}, "
            f"duration_years={self._duration_years}, language={self._language}, "
            f"is_active={self._is_active})"
        )
