from app.models.contents import Contents


def test_create_content():
    content = Contents(
        cid="12",
        tid="444",
        title="Agile methodologies",
        href="aksdoasdkas.com/gfidgfd",
        author_uid="43234",
    )
    assert content.cid == "12"
    assert content.tid == "444"
    assert content.title == "Agile methodologies"
    assert content.href == "aksdoasdkas.com/gfidgfd"
    assert content.author_uid == "43234"
