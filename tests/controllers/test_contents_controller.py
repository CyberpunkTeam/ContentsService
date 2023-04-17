from unittest.mock import Mock

import pytest
from fastapi import HTTPException

from app.controllers.contents_controller import ContentsController
from app.models.contents import Contents


def test_get_all_contents():
    repository = Mock()
    repository.get.return_value = [
        Contents(
            cid="12",
            tid="444",
            title="Agile methodologies",
            href="aksdoasdkas.com/gfidgfd",
            author_uid="43234",
        ),
        Contents(
            cid="132",
            tid="444",
            title="Agile methodologies 2",
            href="aksdoasdkas.com/gfidgfd",
            author_uid="43234",
        ),
    ]
    result = ContentsController.get(repository)
    assert len(result) == 2


def test_get_content_by_cid():
    repository = Mock()
    repository.get.return_value = [
        Contents(
            cid="12",
            tid="444",
            title="Agile methodologies",
            href="aksdoasdkas.com/gfidgfd",
            author_uid="43234",
        )
    ]
    result = ContentsController.get(repository, cid="12")
    assert result.title == "Agile methodologies"


def test_error_user_not_found():
    repository = Mock()
    repository.get.return_value = []
    with pytest.raises(HTTPException):
        ContentsController.get(repository, cid="12")


def test_create_content():
    repository = Mock()
    repository.insert.return_value = True
    content = Contents(
        cid="12",
        tid="444",
        title="Agile methodologies",
        href="aksdoasdkas.com/gfidgfd",
        author_uid="43234",
    )

    result = ContentsController.post(repository, content)
    assert result.cid == content.cid


def test_error_create_user():
    repository = Mock()
    repository.insert.return_value = False
    content = Contents(
        cid="12",
        tid="444",
        title="Agile methodologies",
        href="aksdoasdkas.com/gfidgfd",
        author_uid="43234",
    )
    with pytest.raises(HTTPException):
        ContentsController.post(repository, content)
