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

    @staticmethod
    def delete(repository, cid):
        repository.remove(cid)
        return {"message": "content deleted"}

    @staticmethod
    def put(repository, cid, content_update):
        content_update.cid = cid
        local = datetime.now()
        content_update.updated_date = local.strftime("%d-%m-%Y:%H:%M:%S")
        if repository.put(content_update):
            result = repository.get(cid=cid)
            return result[0]
        else:
            raise HTTPException(status_code=500, detail="Error to update content")
