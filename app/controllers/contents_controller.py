from datetime import datetime

from fastapi import HTTPException
from app.models.contents import Contents


class ContentsController:
    @staticmethod
    def post(repository, content: Contents):
        local = datetime.now()
        content.created_date = local.strftime("%d-%m-%Y:%H:%M:%S")
        content.updated_date = local.strftime("%d-%m-%Y:%H:%M:%S")
        content.cid = Contents.get_cid()
        ok = repository.insert(content)
        if not ok:
            raise HTTPException(status_code=500, detail="Error saving")
        return content

    @staticmethod
    def get(repository, author_uid=None, tid=None, cid=None):
        result = repository.get(author_uid=author_uid, tid=tid, cid=cid)
        if len(result) == 0 and cid is not None:
            raise HTTPException(status_code=404, detail="Item not found")

        if cid:
            return result[0]
        return result
