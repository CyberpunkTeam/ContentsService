import mongomock

from app import config
from app.models.contents import Contents
from app.repositories.contents_repository import ContentsRepository


@mongomock.patch(servers=(("server.example.com", 27017),))
def test_save_content():
    url = config.DATABASE_URL
    db_name = config.DATABASE_NAME
    repository = ContentsRepository(url, db_name)

    content = Contents(
        cid="12",
        tid="444",
        title="Agile methodologies",
        href="aksdoasdkas.com/gfidgfd",
        author_uid="43234",
    )

    ok = repository.insert(content)

    assert ok


@mongomock.patch(servers=(("server.example.com", 27017),))
def test_get_content():
    url = config.DATABASE_URL
    db_name = config.DATABASE_NAME
    repository = ContentsRepository(url, db_name)

    content = Contents(
        cid="12",
        tid="444",
        title="Agile methodologies",
        href="aksdoasdkas.com/gfidgfd",
        author_uid="43234",
    )

    ok = repository.insert(content)

    assert ok

    contents_found = repository.get(author_uid="43234")

    assert len(contents_found) == 1

    contents_found = contents_found[0]

    assert contents_found.cid == "12"
    assert contents_found.tid == "444"
    assert contents_found.title == "Agile methodologies"
    assert contents_found.href == "aksdoasdkas.com/gfidgfd"
    assert contents_found.author_uid == "43234"
