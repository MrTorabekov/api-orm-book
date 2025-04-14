from pydantic import BaseModel
from typing import Optional, Any, List


class BaseResponse(BaseModel):
    status: bool = True
    data: Optional[Any] = None
    errors: Optional[List[dict]] = None


class BookIn(BaseModel):
    title: str
    author: str

class BookOut(BookIn):
    id: int
