import string

import pytest
from injector import Injector

from ddd_posts.application.post import PostApplicationService
from ddd_posts.in_memory_infrastructure.post import InMemoryPostModule


@pytest.fixture
def service():
    injector = Injector([InMemoryPostModule])
    return injector.get(PostApplicationService)


def test_one_post(service):
    post_id1 = service.post(string.ascii_uppercase)
    post_id2 = service.post(string.ascii_lowercase)
    result1 = service.detail(post_id1)
    result2 = service.detail(post_id2)
    assert post_id1 == result1.post_id
    assert post_id2 == result2.post_id
    assert string.ascii_uppercase == result1.post_content.value
    assert string.ascii_lowercase == result2.post_content.value
    assert len(service.list_()) == 2