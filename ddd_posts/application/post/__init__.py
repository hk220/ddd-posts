from typing import List
from dataclasses import dataclass

import inject

from ddd_posts.domain.model.post import PostFactoryInterface, PostRepositoryInterface
from ddd_posts.domain.model.post import PostID, Post


@dataclass
class PostApplicationService:
    factory: PostFactoryInterface
    repository: PostRepositoryInterface

    @inject.autoparams()
    def __init__(self, factory: PostFactoryInterface, repository: PostRepositoryInterface):
        self.factory = factory
        self.repository = repository

    def post(self, content: str) -> PostID:
        if not isinstance(content, str):
            raise ValueError("contentがないよ")
        post: Post = self.factory.create(content)
        self.repository.save(post)
        return post.post_id

    def detail(self, post_id: PostID) -> Post:
        return self.repository.find(post_id)

    def list_(self) -> List[Post]:
        return self.repository.find_all()
