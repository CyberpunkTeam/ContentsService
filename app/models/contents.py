import uuid
from json import loads
from typing import Optional

from pydantic import BaseModel


class Contents(BaseModel):
    cid: Optional[str]
    title: str
    author_uid: str
    tid: Optional[str]
    href: str
    created_date: Optional[str]
    updated_date: Optional[str]
    cover_image: Optional[str]

    def to_json(self):
        return loads(self.json(exclude_defaults=True))

    @staticmethod
    def get_schema():
        return {
            "cid": str,
            "author_uid": str,
            "tid": str,
            "href": str,
            "created_date": str,
            "updated_date": str,
            "title": str,
            "cover_image": str,
        }

    @staticmethod
    def get_cid():
        myuuid = uuid.uuid4()
        return str(myuuid)

    def get_id(self):
        return self.tid
