from cpunk_mongo.db import DataBase

from app.models.contents import Contents
from app.models.requests.content_update import ContentsUpdate


class ContentsRepository(DataBase):
    COLLECTION_NAME = "contents"

    def __init__(self, url, db_name):
        if db_name == "test":
            import mongomock

            self.db = mongomock.MongoClient().db
        else:
            super().__init__(url, db_name)

    def get(self, author_uid=None, tid=None, cid=None, state=None):
        filters = {}

        if cid is not None:
            filters["cid"] = cid
        if author_uid is not None:
            filters["author_uid"] = author_uid
        if tid is not None:
            filters["tid"] = tid
        if state is not None:
            filters["state"] = state

        return self.filter(self.COLLECTION_NAME, filters, output_model=Contents)

    def insert(self, content: Contents):
        return self.save(self.COLLECTION_NAME, content)

    @staticmethod
    def create_repository(url, database_name):
        return ContentsRepository(url, database_name)

    def remove(self, cid):
        return self.delete(self.COLLECTION_NAME, "cid", cid)

    def put(self, content: ContentsUpdate):
        return self.update(self.COLLECTION_NAME, "cid", content.cid, content)

    def search(self, fields, value):
        return self.ilike(self.COLLECTION_NAME, fields, value, output_model=Contents)
