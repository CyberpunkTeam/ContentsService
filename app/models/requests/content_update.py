import uuid
from json import loads
from typing import Optional, List

from pydantic import BaseModel

from app.models.states import States


class ContentsUpdate(BaseModel):
    cid: Optional[str]
    title: Optional[str]
    tid: Optional[str]
    href: Optional[str]
    updated_date: Optional[str]
    cover_image: Optional[str]
    likes: Optional[List[str]]
    state: Optional[States]

    def to_json(self):
        return loads(self.json(exclude_defaults=True))
