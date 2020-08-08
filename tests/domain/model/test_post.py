import pytest

import string
from uuid import uuid4

from ddd_posts.domain.model.post import PostID, PostContent, Post


def test_create_post_id_with_none():
    with pytest.raises(ValueError):
        PostID(None)


def test_create_post_content_with_none():
    with pytest.raises(ValueError):
        PostContent(None)


def test_create_post_content_over_141_cahacter():
    with pytest.raises(ValueError):
        PostContent(string.ascii_letters * 3)


def test_create_post_with_none_post_id():
    with pytest.raises(ValueError):
        Post(None, PostContent(string.ascii_letters))


def test_create_post_with_none_post_create():
    with pytest.raises(ValueError):
        Post(PostID(uuid4()), None)


def test_create_post_with_none():
    with pytest.raises(ValueError):
        Post(None, None)

def test_equal_post():
    post_id = PostID(uuid4())
    p1 = Post(post_id, PostContent("AAAAAA"))
    p2 = Post(post_id, PostContent("BBBBBB"))
    assert p1 == p2
