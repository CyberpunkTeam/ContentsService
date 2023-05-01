from datetime import datetime

from fastapi import HTTPException
from app.models.contents import Contents
from app.requests.content_update import ContentsUpdate


class ContentsController:
    @staticmethod
    def post(repository, content: Contents):
        local = datetime.now()
        content.created_date = local.strftime("%d-%m-%Y:%H:%M:%S")
        content.updated_date = local.strftime("%d-%m-%Y:%H:%M:%S")
        content.cid = Contents.get_cid()
        content.likes = []
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

    @staticmethod
    def add_like(repository, cid, uid):
        results = repository.get(cid=cid)
        content = results[0]
        content.likes.append(uid)

        content_update = ContentsUpdate(cid=content.cid, likes=content.likes)
        return ContentsController.put(repository, cid, content_update)

    @staticmethod
    def remove_like(repository, cid, uid):
        results = repository.get(cid=cid)
        content = results[0]
        content.likes.remove(uid)
        content_update = ContentsUpdate(cid=content.cid, likes=content.likes)
        return ContentsController.put(repository, cid, content_update)
