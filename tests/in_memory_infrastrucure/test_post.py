import pytest

import string

from ddd_posts.domain.model.post import Post, PostID, PostContent
from ddd_posts.in_memory_infrastructure.post import InMemoryPostRepository, InMemoryPostFactory


@pytest.fixture()
def repository():
    return InMemoryPostRepository()


@pytest.fixture()
def factory():
    return InMemoryPostFactory()


def test_create_post(repository, factory):
    post = factory.create(string.ascii_letters)
    post_id = post.post_id
    repository.save(post)
    result = repository.find(post_id)
    assert post.post_content == result.post_content
