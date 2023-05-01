from typing import List

from fastapi import APIRouter

from app import config
from app.controllers.contents_controller import ContentsController
from app.models.contents import Contents
from app.repositories.contents_repository import ContentsRepository
from app.requests.content_update import ContentsUpdate

router = APIRouter()

# Repository
contents_repository = ContentsRepository(config.DATABASE_URL, config.DATABASE_NAME)


@router.post("/contents/", tags=["contents"], response_model=Contents, status_code=201)
async def create_content(content: Contents):
    return ContentsController.post(contents_repository, content)


@router.get("/contents/", tags=["contents"], response_model=List[Contents])
async def list_contents(author_uid: str = None, tid: str = None):
    return ContentsController.get(contents_repository, author_uid, tid)


@router.get("/contents/{cid}", tags=["contents"], response_model=Contents)
async def read_content(cid: str):
    return ContentsController.get(contents_repository, cid=cid)


@router.delete("/contents/{cid}", tags=["contents"])
async def remove_content(cid: str):
    return ContentsController.delete(contents_repository, cid=cid)


@router.put("/contents/{cid}", tags=["contents"], response_model=Contents)
async def put_content(cid: str, content_update: ContentsUpdate):
    return ContentsController.put(
        contents_repository, cid=cid, content_update=content_update
    )


@router.post(
    "/contents/{cid}/likes/{uid}",
    tags=["contents"],
    response_model=Contents,
    status_code=201,
)
async def add_like(cid: str, uid: str):
    return ContentsController.add_like(contents_repository, cid=cid, uid=uid)


@router.delete(
    "/contents/{cid}/likes/{uid}", tags=["contents"], response_model=Contents
)
async def remove_like(cid: str, uid: str):
    return ContentsController.remove_like(contents_repository, cid=cid, uid=uid)
