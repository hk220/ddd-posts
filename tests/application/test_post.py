import string

import pytest
from injector import Injector

from ddd_posts.domain.model.post import PostFactoryInterface, PostRepositoryInterface
from ddd_posts.in_memory_infrastructure.post import InMemoryPostModule
from ddd_posts.application.post import PostApplicationService


@pytest.fixture
def service():
    injector = Injector([InMemoryPostModule])
    factory: PostFactoryInterface = injector.get(PostFactoryInterface)
    repository: PostRepositoryInterface = injector.get(PostRepositoryInterface)
    return PostApplicationService(factory, repository)


def test_one_post(service):
    post_id = service.post(string.ascii_letters)
    result = service.detail(post_id)
    assert post_id == result.post_id
    assert string.ascii_letters == result.post_content.value
    assert len(service.list_()) == 1