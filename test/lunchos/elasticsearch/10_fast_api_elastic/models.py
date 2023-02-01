from datetime import date
from typing import Optional

from pydantic import BaseModel


class CreateUserRequest(BaseModel):
    name: str  # имя обьязательній параметр
    surname: Optional[str]  # фамилия НЕ обьязательній параметр и может отсутсовать (Optional), как и остальньіе
    date_of_birth: Optional[date]
    interests: Optional[list[str]]   # список строк
