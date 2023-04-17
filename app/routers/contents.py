from typing import List

from fastapi import APIRouter

from app import config
from app.controllers.contents_controller import ContentsController
from app.models.contents import Contents
from app.repositories.contents_repository import ContentsRepository

router = APIRouter()

# Repository
contents_repository = ContentsRepository(config.DATABASE_URL, config.DATABASE_NAME)


@router.post("/contents/", tags=["contents"], response_model=Contents, status_code=201)
async def create_user(content: Contents):
    return ContentsController.post(contents_repository, content)


@router.get("/contents/", tags=["contents"], response_model=List[Contents])
async def list_users(author_uid: str = None, tid: str = None):
    return ContentsController.get(contents_repository, author_uid, tid)


@router.get("/contents/{cid}", tags=["contents"], response_model=Contents)
async def read_user(cid: str):
    return ContentsController.get(contents_repository, cid=cid)
