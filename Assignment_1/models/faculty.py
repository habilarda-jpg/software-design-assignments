from __future__ import annotations

import uuid
from datetime import datetime, timezone
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.instructor import Instructor


class Faculty:
    def __init__(
        self,
        code: str,
        name: str,
        phone: str,
        email: str,
        dean: Instructor | None = None,
        is_active: bool = True,
        created_at: datetime | None = None,
        id: uuid.UUID | None = None,
    ) -> None:
        self._id = id or uuid.uuid4()
        self._code = code
        self._name = name
        self._dean = dean
        self._phone = phone
        self._email = email
        self._is_active = is_active
        self._created_at = created_at or datetime.now(timezone.utc)

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
    def dean(self) -> Instructor | None:
        return self._dean

    @dean.setter
    def dean(self, value: Instructor | None) -> None:
        self._dean = value

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

    @property
    def created_at(self) -> datetime:
        return self._created_at

    @created_at.setter
    def created_at(self, value: datetime) -> None:
        self._created_at = value

    def __str__(self) -> str:
        dean_name = (
            f"{self._dean.first_name} {self._dean.last_name}" if self._dean else "-"
        )
        return (
            f"Faculty(id={self._id}, code={self._code}, name={self._name}, "
            f"dean={dean_name}, phone={self._phone}, email={self._email}, "
            f"is_active={self._is_active}, created_at={self._created_at})"
        )
